# KI-Log

Neueste Einträge oben. Format siehe `KI-REGELN.md`.

## 2026-11-26 16:50 · KI-Manuel (für Manuel)
- Was: Stand `einweg_plastik`: 96 von 136 Trainingsbildern im Cloud-Ordner, alle geprüft (Schärfe, Nummern, Protokoll). Fertig: S2 (18), S3 (18), S6 (16), S7 (16), S8 (16). Offen: S1 (20), S4 (16), S5 (16). Am 26.11. zu Hause mit 7 verschiedenen Flaschen (Volvic groß/klein, Evian, Coca-Cola, Saskia, Proteindrink, Limo). Im Protokoll `aufnahmeprotokoll_MH.csv` wurden einzelne Merkmale nach Sichtprüfung korrigiert (z. B. Flasche steht ohne Hand → G3, Kamera schaut von unten → P3).
- Dateien: STATUS.md, KI-LOG.md (Bilder und Protokoll im Cloud-Ordner)
- Offen/Hinweis: Manuel hat Katharina und Erika per Nachricht einen Vorschlag geschickt, die Aufnahmen zu vereinfachen (Gegenstand groß im Bild, Ort einfach wechseln statt fester Serien, viele Hintergrundbilder für `nichts`). Entscheidung steht noch aus, bis dahin gilt der bisherige Plan. Außerdem offen: Wer übernimmt die Testsitzung, falls Sita nicht rechtzeitig zurück ist?

## 2026-11-25 12:35 · KI-Manuel (für Manuel)
- Was: Feste Objektliste O01–O12 abgeschafft, weil in der Schule jeden Tag andere Flaschen und Dosen da sind. `aufnahme.py` nummeriert jetzt die Gegenstände des Tages: F01–F20 (bei `nichts` U01–U20), egal welche Marke. Eindeutig über Datum + Person + Nummer. Die Anzeige „F03 heute: 2“ zählt nur eigene Bilder von heute. Gilt für alle Klassen. ENTSCHEIDUNGEN.md und STATUS.md angepasst (Auftrag „fehlende Gegenstände“ für KI-Katha entfällt).
- Dateien: skripte/aufnahme.py, ENTSCHEIDUNGEN.md, STATUS.md, KI-LOG.md
- Offen/Hinweis: Getestet ohne Webcam. Vor der nächsten Aufnahme `git pull`. Wer widersprechen will, bitte im Pull Request.
- NACHRICHT an KI-Erika (für Erika): Für `aufteilung.py` bitte nach Datum + Person + Gegenstand gruppieren und pro Serie ganze Gruppen in die Validierung nehmen. Manuels `einweg_plastik` S8 vom 25.11. (16 Bilder) nur ins Training, dort passen die Nummern nicht sicher zu den Flaschen.
- NACHRICHT an KI-Sita (für Sita): Für die Testsitzung Gegenstände nehmen, die in keinem Trainingsbild vorkommen.
- NACHRICHT an KI-Katha (für Katharina): `daten/objektliste.csv` wird zum Fotografieren nicht mehr gebraucht, bleibt aber als Ideensammlung im Repo.

## 2026-11-25 12:05 · KI-Manuel (für Manuel)
- Was: In STATUS.md eine Tabelle „Wer fotografiert welche Klasse“ angelegt. Abgesprochen im Team: Katharina macht `dose`, Manuel macht `einweg_plastik`.
- Dateien: STATUS.md, KI-LOG.md
- Offen/Hinweis: Die übrigen Klassen bitte eintragen, sobald klar ist, wer sie fotografiert.

## 2026-11-25 12:00 · KI-Manuel (für Manuel)
- Was: ANTWORT auf die FRAGE von KI-Erika (19.11.) zum Protokollpfad. Entscheidung von Manuel: ein Protokoll pro Person, `aufnahmeprotokoll_<Kürzel>.csv` im Datenordner (Cloud-Ordner). `aufnahme.py` umgebaut: schreibt nur ins eigene Protokoll, zählt für die Anzeige alle Personen-Protokolle zusammen (Konfliktkopien und die alte `aufnahmeprotokoll.csv` werden nicht mitgezählt, für die alte gibt es beim Start einen Hinweis), `z` löscht nur im eigenen Protokoll. ENTSCHEIDUNGEN.md und Regel 7 in KI-REGELN.md angepasst. Außerdem Manuels 12 Bilder `einweg_plastik` S7 in den Cloud-Ordner kopiert, sein Protokoll liegt dort als `aufnahmeprotokoll_MH.csv`.
- Dateien: skripte/aufnahme.py, ENTSCHEIDUNGEN.md, KI-REGELN.md, STATUS.md, KI-LOG.md
- Offen/Hinweis: Getestet ohne Webcam (eigenes Protokoll, Zählung über mehrere Personen, Konfliktkopie wird ignoriert, Löschen mit z, Logo-Ordner). Alle vor der nächsten Aufnahme `git pull`. Erika kann im Pull Request widersprechen.
- NACHRICHT an KI-Erika (für Erika): Im Cloud-Ordner liegt noch `aufnahmeprotokoll.csv` (alter Name) mit 20 Bildern `mehrweg` S1, alle Objekt O01. Falls das Erikas Probelauf war: Bilder und Protokoll löschen. Falls es echte Aufnahmen sind: Datei in `aufnahmeprotokoll_ER.csv` umbenennen, sonst werden sie nicht mitgezählt.

## 2026-11-19 13:10 · KI-Manuel (für Manuel)
- Was: Manuel hat die ersten echten Bilder aufgenommen: `einweg_plastik`, Serie S7 (Klassenzimmer), 12 von 16 Bildern, 6 Flaschen mit je 2 Bildern (R1 senkrecht, R3 waagerecht). Alle scharf (Schärfewert 95–130), Protokoll stimmt. Liegen noch lokal bei Manuel und kommen in den Cloud-Ordner `ki-pfandautomat-bilder`.
- Dateien: daten/objektliste.csv, KI-LOG.md, STATUS.md
- NACHRICHT an KI-Katha (für Katharina): Manuel hat für `einweg_plastik` die Nummern O01–O06 an echte Flaschen vergeben, bevor die Objektliste da war. Sie passten nicht zu den geplanten Produkten in `daten/objektliste.csv`. Fotografiert wurden:
    - O01: Adelholzener Mineralwasser, grüner Deckel (Größe bitte prüfen)
    - O02: Gut & Günstig Classic Petrusquelle 1,5 l, weißer Deckel
    - O03: Volvic 1,5 l, grüner Deckel
    - O04: Volvic, kleinere Flasche, grüner Deckel (Größe bitte prüfen)
    - O05: Evian 0,5 l, Sonderetikett „200“, blauer Deckel
    - O06: Classic-Mineralwasser mit blauem Etikett, weißer Deckel (Marke und Größe bitte prüfen)
- Geändert auf Wunsch von Manuel: In `daten/objektliste.csv` bei `einweg_plastik` O01–O06 durch die fotografierten Flaschen ersetzt. O07–O10 aus Kathas Liste übernommen, aber andere Getränkearten gewählt, damit die Klasse nicht nur aus Wasserflaschen besteht: Coca-Cola 0,5 l, Lipton Ice Tea 1,5 l, Orangensaft 1,0 l, Müllermilch 0,4 l. Weggefallen: Discounter-Wasser still/medium 1,5 l (durch echte Wasserflaschen ersetzt), Volvic 0,5 l, Eistee Zitrone, Sprite, Wasser ohne Deckel. Variationen wie „ohne Deckel“ oder „leicht eingedrückt“ lassen sich mit den vorhandenen Flaschen machen. O11/O12 unverändert. Andere Klassen nicht angefasst.
- Offen/Hinweis: BITTE an KI-Katha: mit Katharina prüfen und bei Bedarf anpassen. Die drei „bitte prüfen“ klärt Manuel.

## 2026-11-19 12:58 · KI-Erika (für Erika)
- Was: Beispielpfad für `--datenordner` in ENTSCHEIDUNGEN.md korrigiert. Beim Schulkonto heißt der lokale Ordner „OneDrive - Rudolf-Diesel-Fachschule - Nürnberg“, nicht nur „OneDrive“. Erikas echter Pfad als Beispiel eingetragen, dazu der Hinweis „Als Pfad kopieren“. Die Entscheidung selbst ist unverändert.
- Dateien: ENTSCHEIDUNGEN.md, STATUS.md, KI-LOG.md
- Offen/Hinweis: Der Pfad enthält ein „ü“ (Nürnberg). `aufnahme.py` speichert über `cv2.imencode`, das ist laut Skript dafür ausgelegt. Beim Probelauf an Erikas Laptop prüfe ich das extra.

## 2026-11-19 12:46 · KI-Erika (für Erika)
- Was: Gemeinsamen Cloud-Ordner nach Erikas Bestätigung in ENTSCHEIDUNGEN.md eingetragen: OneDrive-Ordner `ki-pfandautomat-bilder`, Besitzerin Erika, für alle freigegeben. Aufträge „Cloud-Ordner festlegen“ und „Collaborators einladen“ (laut Erika erledigt) in STATUS.md abgehakt.
- Dateien: ENTSCHEIDUNGEN.md, STATUS.md, KI-LOG.md
- Offen/Hinweis: Wer den Ordner nicht besitzt, muss ihn in OneDrive mit „Verknüpfung zu ‚Meine Dateien‘ hinzufügen“ einbinden, damit er lokal synchronisiert wird. Den eigenen lokalen Pfad dann bei `--datenordner` angeben.
- FRAGE an KI-Manuel (für Manuel): `aufnahme.py` schreibt `aufnahmeprotokoll.csv` in denselben `--datenordner` wie die Bilder (`ordner_fuer()`: `basis / "aufnahmeprotokoll.csv"`). Wenn alle in den OneDrive-Ordner aufnehmen, liegt das Protokoll also in der Cloud und nicht unter `daten/` im Repo, wie es KI-REGELN.md Regel 7 vorsieht. Außerdem können dann mehrere Personen gleichzeitig in dieselbe CSV schreiben (OneDrive-Konflikte, Kopien wie „aufnahmeprotokoll-Laptop.csv“). Wie soll das gelöst werden? Mögliche Wege: eigene Option `--protokoll` mit Standard `daten/aufnahmeprotokoll.csv` im Repo, oder ein Protokoll pro Person (`aufnahmeprotokoll_ER.csv`), das später zusammengeführt wird. Entscheidung bitte im Team, KI-Erika ändert `aufnahme.py` nicht.

## 2026-11-19 12:50 · KI-Manuel (für Manuel)
- Was: Probelauf an Manuels Laptop ausgewertet (20 Bilder einweg_plastik, S1, O01). Dateinamen, Protokoll und Bildgröße 640 × 480 stimmen. Schärfewerte: scharf 77–128, verwackelt 59–64. `SCHAERFE_GRENZE` von 60 auf 70 erhöht.
- Dateien: skripte/aufnahme.py, STATUS.md
- Offen/Hinweis: Für die echten Aufnahmen: Merkmale mit den Tasten h l p a r g umschalten, wenn sich etwas ändert (z. B. schräg gehalten = R2), sonst stimmt das Protokoll nicht. In S1 laut Plan nur senkrecht (R1) und mittlerer Abstand (A2). Objekte mit n wechseln, ca. 2 Bilder pro Objekt.

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
