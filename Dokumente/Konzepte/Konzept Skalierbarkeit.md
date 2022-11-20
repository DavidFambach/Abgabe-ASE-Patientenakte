# Skalierbarkeit

Skalierbarkeit ist die Fähigkeit eines Systems zum Wachstum. Wachstum kann sowohl horizontal als auch vertikal stattfinden. Konkret bedeutet das, dass sich die Menge an Anfragen (_vertikal_) an das System und der geografische Raum (_horizontal_), aus dem Anfragen gestellt werden, vergrößern können.

## vertikale Skalierbarkeit
Vertikale Skalierung hat zwangsläufig zur Folge das die Hardware mitskaliert. Auch diese kann vertikal und horizontal skalieren, also die Hardwareressourcen auf dem System erhöhen oder einfach neue Systeme in das bestehende Cluster aufnehmen.
![Scalability](https://www.scaleuptech.com/de/wp-content/uploads/2016/09/ScaleUp_und_ScaleOut_2.png)
Mit dem aktuellen Funktionsumfang ist die Hauptaufgabe unserer Anwendung das Hoch-, Herunterladen und Speichern von Daten. Damit sind die am höchsten beanspruchten Ressourcen das Netzwerk und der Massenspeicher der Systeme. Diese beiden Lasten skalieren linear, bei doppelter Leistung werden doppelt so viele Ressourcen benötigt.

## horizontale Skalierbarkeit
Soll unsere Anwendung horizontal skalierbar sein, sprich ihren geografischen Einflussbereich ohne Einschränkungen der NFA's (Nichtfunktionalen Anforderungen) vergrößern können, so spielen viele Eigenschaften eine Rolle. Ein hauptsächliches Problem sind die Ländergrenzen, mit denen andere Sprachen und andere Gesetze hinsichtlich Datensicherheit und Informationssicherheit einhergehen.
Mit der Annahme, dass ein Austausch von medizinischen Daten über Ländergrenzen hinweg selten ausgetauscht werden (Eine Ausnahme bildet dabei die EU), ist es sinnvoll ein unabhängiges, von einer örtlichen Institution, System pro Region (Länder(-verbünde) in denen sich die Datenschutz- und Informationssicherheitsgesätze vereinen lassen und der Austausch von medizinischen Daten üblich ist) zu hosten.

## Zusammenfassung
In beiden Fällen hilft uns die Microservice Architektur, mit der wir unsere Anwendung Entwickeln. Sollte ein Microservice überlastet sein, kann dieser in der Regel sowohl vertikal als auch horizontal skalieren:

 - **vertikal:** Dem Dienst werden entsprechend mehr Ressourcen zugewiesen.
 - **horizontal:** Eine zweite Instanz des Dienstes wird auf einem anderen System betrieben.
