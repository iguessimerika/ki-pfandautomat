# KI-Log

Neueste Einträge oben. Format siehe `KI-REGELN.md`.

## 2026-11-19 12:45 · KI-Katha (für Katharina)
- Was: Beschreibungen in `daten/objektliste.csv` gefüllt, auf Wunsch von Katharina mit in Deutschland gängigen Produkten (60 Gegenstände, 12 Umgebungen). O11/O12 sind andere Produkte als O01–O10, damit der Test unbekannte Gegenstände prüft.
- Dateien: daten/objektliste.csv, STATUS.md
- Offen/Hinweis: Das ist eine Sammel- bzw. Einkaufsliste, die Gegenstände liegen noch nicht vor. Wenn Katharina etwas anderes bekommt, wird die Beschreibung angepasst. Vor dem Fotografieren prüfen: Bierflaschen wirklich braun, Mehrweg-Flaschen wirklich 0,15 € Pfand, Einweg-PET mit DPG-Logo. FRAGE an das Team: Das Drehbuch nennt bei `kein_pfand` zusätzlich ca. 20 Bilder sonstiger Gegenstände (Tasse, Handy, Federmäppchen). Sollen diese eigene Objekt-Nummern bekommen (dann statt einiger Verpackungen in O01–O10) oder unter bestehenden Nummern laufen? Bisher stehen nur Verpackungen in der Liste.

## 2026-11-19 12:35 · KI-Katha (für Katharina)
- Was: `daten/objektliste.csv` als Gerüst angelegt, Spalten `objekt,klasse,beschreibung,nur_test`. Pro Klasse O01–O12, bei `nichts` U01–U12 (72 Zeilen). O11/O12 und U11/U12 mit `nur_test = ja`, alle anderen `nein`.
- Dateien: daten/objektliste.csv, STATUS.md
- Offen/Hinweis: Spalte `beschreibung` ist noch leer, Katharina nennt die Gegenstände, danach wird sie gefüllt. Auftrag in STATUS.md deshalb noch nicht abgehakt. U11/U12 als `nur_test` gesetzt wie in `aufnahme.py` (Testsitzung erlaubt U01–U12, S1–S8 nur U01–U10); im Drehbuch ist das nur für O11/O12 ausdrücklich genannt.

## 2026-11-19 12:35 · KI-Manuel (für Manuel)
- Was: Die 17 Ruff-Warnungen in `aufnahme.py` behoben. Aufnahmeplan (Zeilen 66–91) als Dictionary-Literale statt `dict()`, dazu `OSError` statt `IOError` und ein überflüssiger f-String. Funktion unverändert, Tests erneut bestanden.
- Dateien: skripte/aufnahme.py
- Offen/Hinweis: –

## 2026-11-19 12:30 · KI-Manuel (für Manuel)
- Was: Aufträge für KI-Katha, KI-Erika und KI-Manuel in `STATUS.md` (Abschnitt „Aufträge an die KIs“) eingetragen, auf Wunsch von Manuel und nach dem Zeitplan im Drehbuch
- Dateien: STATUS.md
- Offen/Hinweis: VORSCHLAG an das Team: Heute haben KI-Katha und KI-Manuel gleichzeitig Lastenheft und Drehbuch hochgeladen (`dokumente/` und `doku/`), weil eine Anmeldung auf einem Branch erst nach dem Merge sichtbar ist. Vorschlag: Anmeldungen unter „In Arbeit“ direkt auf `main` committen, ohne Pull Request. Nur die eigentliche Arbeit läuft über Branches. Bitte im Team entscheiden.

## 2026-11-19 12:12 · KI-Katha (für Katharina)
- Was: Lastenheft (v1.0, 12.11.2026) und Drehbuch zur Bilderstellung (v1.0, 18.11.2026) als PDF hochgeladen, unverändert von Katharina bereitgestellt
- Dateien: dokumente/Lastenheft_Pfandautomat_v1.0.pdf, dokumente/Drehbuch_Pfandautomat_v1.0.pdf, STATUS.md
- Offen/Hinweis: Bei neuen Versionen bitte neue Datei mit neuer Versionsnummer ablegen, alte nicht überschreiben

## 2026-11-19 12:15 · KI-Manuel (für Manuel)
- Was: Aufnahmeskript geschrieben. Live-Bild, Leertaste speichert ein Bild, Dateiname und Protokollzeile automatisch nach ENTSCHEIDUNGEN.md, Aufnahmeplan S1–S8/T und Logo-Serien hinterlegt (Zielanzahl und erlaubte Merkmale je Serie), Schärfe-Warnung, z = letztes Bild löschen. Logo-Klassen speichern nur den markierten Ausschnitt (320 × 320) unter daten/logo/.
- Dateien: skripte/aufnahme.py, requirements.txt, STATUS.md
- Offen/Hinweis: Logik ohne Webcam getestet, auch Pfade mit Umlauten. Test an echter Webcam steht noch aus. Im Protokoll steht bei S1–S8 split = "offen", aufteilung.py setzt später train/val. Start: `python skripte/aufnahme.py --klasse dose --serie S1 --person MH`

## 2026-11-19 12:00 · KI-Manuel (für Manuel)
- Was: Uni Brain eingerichtet: Regeln, Entscheidungen aus Lastenheft und Drehbuch, Status mit Zeitplan
- Dateien: KI-REGELN.md, ENTSCHEIDUNGEN.md, STATUS.md, KI-LOG.md, CLAUDE.md, AGENTS.md, .gitignore
- Offen/Hinweis: Alle KIs lesen zuerst KI-REGELN.md
