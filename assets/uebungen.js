/* =========================================================
   Übungsbausteine für Biologie Klasse 8
   Eine Übung wird so in eine Seite eingebaut:

   <div class="uebung" data-typ="quiz">
     <script type="application/json"> { ...Inhalt... } </script>
   </div>

   Typen: quiz, zuordnen, sortieren, lueckentext
   Es werden keine Daten gespeichert oder verschickt.
   ========================================================= */
(function () {
  "use strict";

  function el(tag, attrs, kinder) {
    var e = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === "text") e.textContent = attrs[k];
        else if (k === "html") e.innerHTML = attrs[k];
        else if (k === "class") e.className = attrs[k];
        else if (k.indexOf("on") === 0) e.addEventListener(k.slice(2), attrs[k]);
        else e.setAttribute(k, attrs[k]);
      });
    }
    (kinder || []).forEach(function (k) { if (k) e.appendChild(k); });
    return e;
  }

  function mischen(liste) {
    var a = liste.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function lob(anteil) {
    if (anteil === 1) return "Alles richtig – stark!";
    if (anteil >= 0.75) return "Sehr gut, fast alles richtig.";
    if (anteil >= 0.5) return "Gut! Schau dir die markierten Stellen noch einmal an.";
    return "Lies den Lerntext noch einmal und versuche es erneut.";
  }

  function punkteleiste(container, text, neustart) {
    var leiste = el("div", { class: "punktestand", role: "status", "aria-live": "polite" }, [
      el("span", { text: text }),
      el("button", { class: "knopf", type: "button", text: "Neu starten", onclick: neustart })
    ]);
    container.appendChild(leiste);
    return leiste;
  }

  /* ---------- Quiz (Multiple Choice) ---------- */
  function quiz(container, daten) {
    var fragen = daten.mischen === false ? daten.fragen : mischen(daten.fragen);
    var beantwortet = 0, richtig = 0;
    var leiste;

    fragen.forEach(function (f, nr) {
      var box = el("div", { class: "frage" });
      box.appendChild(el("h3", {}, [el("span", { class: "nummer", text: (nr + 1) + "." }), document.createTextNode(f.frage)]));
      var opts = el("div", { class: "optionen", role: "group", "aria-label": "Antwortmöglichkeiten" });
      var rueck = el("p", { class: "rueckmeldung", "aria-live": "polite" });
      var reihenfolge = f.optionen.map(function (o, i) { return { text: o, i: i }; });
      reihenfolge = mischen(reihenfolge);
      reihenfolge.forEach(function (o) {
        var b = el("button", { class: "option", type: "button", text: o.text });
        b.addEventListener("click", function () {
          var istRichtig = o.i === f.richtig;
          Array.prototype.forEach.call(opts.children, function (k) { k.disabled = true; });
          b.classList.add(istRichtig ? "ist-richtig" : "ist-falsch");
          if (!istRichtig) {
            Array.prototype.forEach.call(opts.children, function (k, idx) {
              if (reihenfolge[idx].i === f.richtig) k.classList.add("ist-richtig");
            });
          }
          rueck.innerHTML = "";
          rueck.appendChild(el("strong", { class: istRichtig ? "gut" : "schlecht", text: istRichtig ? "Richtig. " : "Leider falsch. " }));
          if (f.erklaerung) rueck.appendChild(document.createTextNode(f.erklaerung));
          beantwortet++; if (istRichtig) richtig++;
          leiste.firstChild.textContent = punkteText();
        });
        opts.appendChild(b);
      });
      box.appendChild(opts); box.appendChild(rueck);
      container.appendChild(box);
    });

    function punkteText() {
      var t = richtig + " von " + fragen.length + " richtig";
      if (beantwortet === fragen.length) t += " – " + lob(richtig / fragen.length);
      else t += " (" + (fragen.length - beantwortet) + " offen)";
      return t;
    }
    leiste = punkteleiste(container, punkteText(), function () { neuAufbauen(container, "quiz", daten); });
  }

  /* ---------- Zuordnen ---------- */
  function zuordnen(container, daten) {
    var paare = mischen(daten.paare);
    var rechts = mischen(daten.paare.map(function (p) { return p.rechts; }));
    var zeilen = [];
    paare.forEach(function (p, nr) {
      var id = "z" + Math.random().toString(36).slice(2, 8) + nr;
      var sel = el("select", { id: id });
      sel.appendChild(el("option", { value: "", text: "– bitte wählen –" }));
      rechts.forEach(function (r) { sel.appendChild(el("option", { value: r, text: r })); });
      var zeile = el("div", { class: "paar" }, [el("label", { class: "begriff", for: id, text: p.links }), sel]);
      zeilen.push({ zeile: zeile, sel: sel, loesung: p.rechts });
      container.appendChild(zeile);
    });
    var rueck = el("p", { class: "rueckmeldung", "aria-live": "polite" });
    var knoepfe = el("div", { class: "knopfreihe" }, [
      el("button", { class: "knopf", type: "button", text: "Prüfen", onclick: pruefen }),
      el("button", { class: "knopf leise", type: "button", text: "Lösung zeigen", onclick: loesung }),
      el("button", { class: "knopf leise", type: "button", text: "Neu starten", onclick: function () { neuAufbauen(container, "zuordnen", daten); } })
    ]);
    container.appendChild(knoepfe); container.appendChild(rueck);

    function pruefen() {
      var n = 0;
      zeilen.forEach(function (z) {
        var ok = z.sel.value === z.loesung;
        z.zeile.classList.toggle("ist-richtig", ok);
        z.zeile.classList.toggle("ist-falsch", !ok);
        if (ok) n++;
      });
      rueck.innerHTML = "";
      rueck.appendChild(el("strong", { class: n === zeilen.length ? "gut" : "schlecht", text: n + " von " + zeilen.length + " richtig. " }));
      rueck.appendChild(document.createTextNode(lob(n / zeilen.length)));
    }
    function loesung() { zeilen.forEach(function (z) { z.sel.value = z.loesung; }); pruefen(); }
  }

  /* ---------- Sortieren in Kategorien ---------- */
  function sortieren(container, daten) {
    var eintraege = mischen(daten.eintraege);
    var zeilen = [];
    eintraege.forEach(function (e) {
      var wahl = el("div", { class: "wahl", role: "group", "aria-label": "Zuordnung für: " + e.text });
      var loesungText = el("div", { class: "loesung", hidden: "" });
      var zeile = el("div", { class: "sortier-eintrag" }, [el("span", { text: e.text }), wahl, loesungText]);
      var z = { zeile: zeile, gewaehlt: null, loesung: e.kategorie, erklaerung: e.erklaerung, loesungText: loesungText, knoepfe: [] };
      daten.kategorien.forEach(function (k) {
        var b = el("button", { type: "button", "aria-pressed": "false", text: k });
        b.addEventListener("click", function () {
          z.gewaehlt = k;
          z.knoepfe.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
          zeile.classList.remove("ist-richtig", "ist-falsch");
          loesungText.hidden = true;
        });
        z.knoepfe.push(b); wahl.appendChild(b);
      });
      zeilen.push(z); container.appendChild(zeile);
    });
    var rueck = el("p", { class: "rueckmeldung", "aria-live": "polite" });
    container.appendChild(el("div", { class: "knopfreihe" }, [
      el("button", { class: "knopf", type: "button", text: "Prüfen", onclick: pruefen }),
      el("button", { class: "knopf leise", type: "button", text: "Neu starten", onclick: function () { neuAufbauen(container, "sortieren", daten); } })
    ]));
    container.appendChild(rueck);

    function pruefen() {
      var n = 0, offen = 0;
      zeilen.forEach(function (z) {
        if (!z.gewaehlt) { offen++; return; }
        var ok = z.gewaehlt === z.loesung;
        z.zeile.classList.toggle("ist-richtig", ok);
        z.zeile.classList.toggle("ist-falsch", !ok);
        if (ok) n++;
        else {
          z.loesungText.textContent = "Richtig wäre: " + z.loesung + (z.erklaerung ? ". " + z.erklaerung : "");
          z.loesungText.hidden = false;
        }
      });
      rueck.innerHTML = "";
      if (offen) { rueck.textContent = "Ordne zuerst alle Aussagen zu (" + offen + " offen)."; return; }
      rueck.appendChild(el("strong", { class: n === zeilen.length ? "gut" : "schlecht", text: n + " von " + zeilen.length + " richtig. " }));
      rueck.appendChild(document.createTextNode(lob(n / zeilen.length)));
    }
  }

  /* ---------- Lückentext ----------
     Lücken im Text: [[Antwort]] oder [[Antwort|andere erlaubte Schreibweise]] */
  function lueckentext(container, daten) {
    var luecken = [];
    var html = daten.text.replace(/\[\[([^\]]+)\]\]/g, function (_, inhalt) {
      var moeglich = inhalt.split("|").map(function (s) { return s.trim(); });
      luecken.push(moeglich);
      return '<input type="text" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Lücke ' + luecken.length + '" data-nr="' + (luecken.length - 1) + '">';
    });
    if (daten.wortspeicher !== false) {
      var speicher = el("div", { class: "wortspeicher", "aria-label": "Wortspeicher" });
      mischen(luecken.map(function (l) { return l[0]; })).forEach(function (w) { speicher.appendChild(el("span", { text: w })); });
      container.appendChild(speicher);
    }
    var text = el("div", { class: "lueckentext", html: html });
    container.appendChild(text);
    var rueck = el("p", { class: "rueckmeldung", "aria-live": "polite" });
    container.appendChild(el("div", { class: "knopfreihe" }, [
      el("button", { class: "knopf", type: "button", text: "Prüfen", onclick: pruefen }),
      el("button", { class: "knopf leise", type: "button", text: "Lösung zeigen", onclick: loesung }),
      el("button", { class: "knopf leise", type: "button", text: "Neu starten", onclick: function () { neuAufbauen(container, "lueckentext", daten); } })
    ]));
    container.appendChild(rueck);

    function norm(s) { return s.toLowerCase().replace(/\s+/g, " ").trim(); }
    function pruefen() {
      var n = 0, felder = text.querySelectorAll("input");
      Array.prototype.forEach.call(felder, function (f) {
        var ok = luecken[+f.dataset.nr].some(function (m) { return norm(m) === norm(f.value); });
        f.classList.toggle("ist-richtig", ok); f.classList.toggle("ist-falsch", !ok);
        if (ok) n++;
      });
      rueck.innerHTML = "";
      rueck.appendChild(el("strong", { class: n === felder.length ? "gut" : "schlecht", text: n + " von " + felder.length + " richtig. " }));
      rueck.appendChild(document.createTextNode(lob(n / felder.length)));
    }
    function loesung() {
      Array.prototype.forEach.call(text.querySelectorAll("input"), function (f) { f.value = luecken[+f.dataset.nr][0]; });
      pruefen();
    }
  }

  var typen = { quiz: quiz, zuordnen: zuordnen, sortieren: sortieren, lueckentext: lueckentext };

  function neuAufbauen(container, typ, daten) {
    container.innerHTML = "";
    typen[typ](container, daten);
  }

  function start() {
    document.querySelectorAll(".uebung[data-typ]").forEach(function (box) {
      var typ = box.getAttribute("data-typ");
      var quelle = box.querySelector('script[type="application/json"]');
      if (!typen[typ] || !quelle) return;
      var daten;
      try { daten = JSON.parse(quelle.textContent); }
      catch (err) { box.textContent = "Diese Übung konnte nicht geladen werden (Fehler im Inhalt)."; return; }
      var ziel = el("div", { class: "uebung-inhalt" });
      box.appendChild(ziel);
      typen[typ](ziel, daten);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
