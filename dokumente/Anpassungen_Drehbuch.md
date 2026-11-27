# Anpassungen am Drehbuch nach dem Probelauf

Stand: 27.11.2026 · Team Pfandautomat (Erika Rohrmeyer, Katharina Lutzky, Sita Stojan, Manuel Herrmann)

Das Drehbuch vom 18.11.2026 sah 8 Aufnahmeserien mit festgelegtem Hintergrund, Licht, Perspektive, Abstand, Ausrichtung und Haltung vor, dazu eine feste Objektliste (O01–O12 pro Klasse). Nach den ersten Aufnahmen (19.–26.11.) haben wir den Ablauf vereinfacht. Ziel und Umfang (mindestens 150 Bilder pro Klasse laut Lastenheft, getrennte Testbilder, Augmentation nur auf Trainingsdaten) bleiben gleich.

| Was | Drehbuch | Jetzt | Grund |
| --- | --- | --- | --- |
| Gegenstände | feste Objektliste O01–O12 pro Klasse | Gegenstände des Tages, nummeriert F01, F02 … (eindeutig über Datum + Person + Nummer) | In der Schule sind jeden Tag andere Flaschen und Dosen verfügbar. Mehr verschiedene Gegenstände machen das Modell sogar robuster. |
| Aufnahmeserien | 8 Serien S1–S8 mit festen Merkmalen | ein einfacher Modus: Gegenstand groß im Bild, drei Haltungen reihum, regelmäßig den Platz wechseln | Der Aufbau der Serien (Räume, Licht, Hintergründe) kostete sehr viel Zeit. Das Modell braucht die Merkmale nicht, es lernt nur die Klasse. |
| Hintergrund | gezielt nach Serie gewählt | dort fotografieren, wo man gerade ist, nach ca. 20 Bildern Platz wechseln | Das Modell soll unabhängig vom Raum erkennen. Viele zufällige Hintergründe erreichen das mit weniger Aufwand. Zusätzlich lernt die Klasse „Nichts“ aus vielen Räumen, dass Hintergrund allein keine Flasche ist. |
| Licht | gezielt (Tageslicht, Lampe, Gegenlicht …) | nicht mehr eingerichtet | Helligkeit und Kontrast werden durch die Augmentation variiert. Im Winter ist gezieltes Tageslicht kaum planbar. |
| Abstand | drei Abstände | 25–40 cm, Gegenstand füllt etwa die halbe Bildhöhe | Je größer der Gegenstand im Bild, desto weniger Einfluss hat der Hintergrund. |
| Protokoll | ein gemeinsames Protokoll | ein Protokoll pro Person | Keine Schreibkonflikte im gemeinsamen OneDrive-Ordner. |

Bereits nach dem alten Plan aufgenommene Bilder bleiben im Datensatz.

Ob die Vereinfachung reicht, prüfen wir mit der Testsitzung (Gegenstände, die nie im Training vorkamen) und der Verwechslungsmatrix. Klassen, die oft verwechselt werden, fotografieren wir gezielt nach.
