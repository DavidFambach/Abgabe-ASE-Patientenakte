# Anwendungsfall: Datei hochladen

## 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Hochladens einer Datei in das System, sodass es dem Benutzer zur Verfügung steht und er es teilen kann.

## 2 Beteiligte
- Benutzer

## 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.
- Der Patient ist authentifiziert (vgl. Anwendungsfall: Authentifizierung), es liegt also eine entsprechende gültige Sitzung vor.

## 4 Standardablauf
1. Der Patient befindet sich nach erfolgter Authentifizierung auf der Startseite der Anwendung.
2. Der Patient wechselt zur Ansicht "Profileinstellungen".
3.	Der Benutzer interagiert mit der Schaltfläche für das Hochladen einer Datei
4.	Der Benutzer interagiert mit der „Datei suchen“ Schaltfläche und ein Dialogfenster öffnet sich
5.	Der Benutzer wählt die hochzuladende Datei über das Dialogfenster aus
6.	Die Datei wird erfolgreich verschlüsselt und auf den Dateiserver hochgeladen
7.	Der Anwendungsfall wird erfolgreich abgeschlossen


## 5 Alternativer Ablauf

### 5.1 Alternatives Hochladen
•	In Schritt 4 zieht der Benutzer die hochzuladende Datei über die dafür vorgesehene Fläche 
•	Der Anwendungsfall läuft ab Schritt 6 normal weiter

### 5.2 Fehler beim Hochladen der Datei
•	Die Datei kann in Schritt 6 nicht erfolgreich hochgeladen werden
•	Der Anwendungsfall endet in einem Fehler


### 5.3 Die Datei ist zu groß
•	Die Datei in Schritt 6 ist zu groß zum Hochladen
•	Der Anwendungsfall endet in einem Fehler


### 5.4 Die Datei hat ein ungültiges Format
•	Die Datei in Schritt 6 hat ein ungültiges Format
•	Der Anwendungsfall endet in einem Fehler


## 6 Schlüsselszenarien
keine

## 7 Nachbedingung

### 7.1 Erfolgreicher Abschluss
•	 Die Datei wurde erfolgreich auf den Server hochgeladen,
•	 Alle berechtigten Benutzer erhalten Zugriff auf die Datei
•	 Die Logdaten wurden aktualisiert


### 7.2 Fehlerzustand
Die Logdaten werden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
keine
