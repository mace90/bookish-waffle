# bookish-waffle

✈️ Flugrouten-Visualisierung mit Plotly (OpenFlights)

Dieses Projekt zeigt eine interaktive Karte mit Flugrouten innerhalb Deutschlands (oder anderen Ländern) basierend auf den öffentlich verfügbaren Daten von OpenFlights. Die Visualisierung wird mit https://plotly.com/python/ erstellt.

🔍 Features

Abruf von Flughafendaten und Flugrouten direkt über die OpenFlights-API (CSV-Dateien via GitHub)
Filterung nach Ländern (z. B. Deutschland, Frankreich)
Darstellung von Flughäfen als Marker
Darstellung von Flugrouten als Linien
Interaktive Karte mit Zoom und Hover-Infos

📦 Abhängigkeiten

pandas
requests
plotly

Installiere sie mit:
Shellpip install pandas requests plotlyWeitere Zeilen anzeigen

🚀 Ausführen

Shellpython flights.pyWeitere Zeilen anzeigen
Die Karte wird im Browser angezeigt und zeigt alle Flugverbindungen zwischen Flughäfen im ausgewählten Land/Länderset.

🛠️ Anpassung

Du kannst die Länder einfach ändern:
Pythondf_selected = df[df["Country"].isin(["Germany", "France"])]

Oder die Karte auf die ganze Welt erweitern:
Pythongeo = dict(scope="world", ...)

<img width="1487" height="801" alt="Bildschirmfoto 2025-10-27 um 14 45 50" src="https://github.com/user-attachments/assets/46c7c4fc-1e77-4040-a7d6-6f95f528b796" />


📁 Datenquelle

https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat
https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat
