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

📁 Datenquelle

https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat
https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat
