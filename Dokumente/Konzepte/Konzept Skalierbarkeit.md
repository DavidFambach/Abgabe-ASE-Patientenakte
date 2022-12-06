# Skalierbarkeit

Skalierbarkeit ist die Fähigkeit eines Systems zum Wachstum. Wachstum kann sowohl horizontal als auch vertikal stattfinden. Konkret bedeutet das, dass sich die Menge an Anfragen (_vertikal_) an das System und der geografische Raum (_horizontal_), aus dem Anfragen gestellt werden, vergrößern können.

## vertikale Skalierbarkeit
Vertikale Skalierung hat zwangsläufig zur Folge das die Hardware mitskaliert. Auch diese kann vertikal und horizontal skalieren, also die Hardwareressourcen auf dem System erhöhen oder einfach neue Systeme in das bestehende Cluster aufnehmen.
![Scalability](https://www.scaleuptech.com/de/wp-content/uploads/2016/09/ScaleUp_und_ScaleOut_2.png)
Mit dem aktuellen Funktionsumfang ist die Hauptaufgabe unserer Anwendung das Hoch-, Herunterladen und Speichern von Daten. Damit sind die am höchsten beanspruchten Ressourcen das Netzwerk und der Massenspeicher der Systeme. Diese beiden Lasten skalieren linear, bei doppelter Leistung werden doppelt so viele Ressourcen benötigt.

## horizontale Skalierbarkeit
Soll unsere Anwendung horizontal skalierbar sein, sprich ihren geografischen Einflussbereich ohne Einschränkungen der NFA's (Nichtfunktionalen Anforderungen) vergrößern können, so spielen viele Eigenschaften eine Rolle. Ein hauptsächliches Problem sind die Ländergrenzen, mit denen andere Sprachen und andere Gesetze hinsichtlich Datensicherheit und Informationssicherheit einhergehen.
Mit der Annahme, dass ein Austausch von medizinischen Daten über Ländergrenzen hinweg selten ausgetauscht werden (Eine Ausnahme bildet dabei die EU), ist es sinnvoll ein unabhängiges, von einer örtlichen Institution, System pro Region (Länder(-verbünde) in denen sich die Datenschutz- und Informationssicherheitsgesätze vereinen lassen und der Austausch von medizinischen Daten üblich ist) zu hosten.

## Rechnung

### Benutzerzahl
Die elektronische Patientenakte (ePA) hat in Deutschland rund **380.000** aktive Nutzer. [1] 

In Deutschland gibt es **416.100** berufstätige Ärtzte (stand 2021) [2]

Da die Patientanakten App im Unterschied zur ePA nicht von der Regierung durchgesetzt wird und es mit der ePA zusätzlich ein starkes, bereits akzepktiertes Konkurrenzprodukt gibt, ist es unnwahrscheinlich, dass die Benutzerzahl unserer Anwendung in den ersten 3 Jahren über 1 Million Konten steigt.

[1]:https://www.handelsblatt.com/inside/digital_health/krankenkasse-tk-weit-vorne-bei-elektronischer-patientenakte/28055328.html
[2]:https://de.statista.com/statistik/daten/studie/158869/umfrage/anzahl-der-aerzte-in-deutschland-seit-1990/

### Anfragen
Anzahl der Arztkontakte pro Einwohner in Deutschland im Jahr 2019: 9,8 Arzt-Patienten-Kontakten [3] 

Eine PDF-Datei (eines der beliebtesten Dateiformate für Scans) mit 10 Seiten Scans hat in etwa eine Größe von 3 MB

Im Durschnitt benötigt ein Benutzer 40-60 HTTP Request an unsere Anwendung um eine Datei hochzuladen.

Bei 40-60 Requests pro Benutzung und 1.000.000 Benutzern ist ein Peak von 1.000 Req/sec annehmbar.

Ein HTTP Request hat eine durchschnittliche Größe von 800 bytes. Wenn einer aus 50 Requests ein Dateiabload ist, beträgt die Durschnittliche Größe der Requests 60 kB.  
```
Anfragen im Jahr: Benutzerzahl * Arztkontake_im_Jahr * Benötigte_Requests_für_einen_Upload = 980.000.000 req/Jahr
Paralele Anfragen: Antwortzeit_der_Application * Maximale_Aufrufe_pro_Sekunde = 0.2 sec * 1000 req/sec = 200 req
Speicherbedarf pro Jahr = Benutzerzahl * Arztkontake_im_Jahr * Durchschnittsgröße_PDF_Datei = 29,4 TB/Jahr
```

[3]:https://aerztestellen.aerzteblatt.de/de/redaktion/arzt-patienten-kontakte-im-internationalen-vergleich

### Skalierung
Für die Ausfallsicherheit werden 3 Serverinstanzen mit jeweils 50 % der benötigten Rechenleistung betrieben. Zudem werden die Server in drei örtlich getrennten Rechenzentren untergebracht.

Ein Server:
 - Kerne: 50 Cores (theoretisch 100 Kerne, da diese allerdings nur zum Peak benötigt werden ist eine Reduzierung auf 50 vertretbar)
 - Speicher: 100 TB
 - Netzwerkbandbreite: 60 kB * 200 = 96 Mb


## Zusammenfassung
In beiden Fällen hilft uns die Microservice Architektur, mit der wir unsere Anwendung Entwickeln. Sollte ein Microservice überlastet sein, kann dieser in der Regel sowohl vertikal als auch horizontal skalieren:

 - **vertikal:** Dem Dienst werden entsprechend mehr Ressourcen zugewiesen.
 - **horizontal:** Eine zweite Instanz des Dienstes wird auf einem anderen System betrieben.