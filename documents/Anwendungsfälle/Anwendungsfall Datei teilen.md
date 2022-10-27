# Anwendungsfall: Datei teilen

## 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Hochladen einer Datei durch einen Patienten, sodass die Datei im Benutzerprofil des Patienten gespeichert wird.

## 2 Beteiligte
- Patient

## 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.
- Der Patient ist authentifiziert (vgl. Anwendungsfall: Authentifizierung), es liegt also eine entsprechende gültige Sitzung vor.
- Dem Patienten liegt eine Datei zum Hochladen vor

## 4 Standardablauf
1. Der Patient befindet sich nach erfolgter Authentifizierung auf der Startseite der Anwendung.
2. Der Patient wechselt zur Ansicht des Verzeichnisses, in das die Datei hochgeladen werden soll. In diesem Anwendungsfall ist das das Stammverzeichnis.
3. Die Webanwendung zeigt eine Auflistung der Elemente des ausgewählten Verzeichnisses an.
4. Der Patient wählt "Datei hochladen"
5. Die Webanwendung fragt nach einer Datei zum Hochladen
6. Der Patient wählt die hochzuladende Datei aus
7. Die Webanwendung überprüft, ob durch die Datei eine maximal zulässige Größe überschritten wird (vgl. RL1, RL2). In diesem Anwendungsfall ist das nicht der Fall.
8. Die Webanwendung erzeugt einen neuen Dateischlüssel, mit dem sie die Datei verschlüsselt. Die verschlüsselte Datei wird gemeinsam mit dem durch den öffentlichen Schlüssel des Benutzers verschlüsselten Dateischlüssel an den Webserver übermittelt. In diesem Anwendungsfall gelingt das.
9. Die Webanwendung teilt dem Patienten mit, dass die Aktion erfolgreich ausgeführt wurde.
10. Die Webanwendung wechselt zur vorherigen Ansicht "Dateiliste" und reflektiert dabei den neuen Zustand.
11. Der Anwendungsfall endet als Erfolg.

## 5 Alternativer Ablauf

### 5.1 Webanwendung stellt zu große Datei fest
Stellt die Webanwendung in Schritt 7 fest, dass durch das Hochladen der Datei eine maximal zulässige Größe überschritten wird (vgl. RL1, RL2), dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass die gewählte Datei zu groß ist beziehungsweise dass dem Benutzerprofil keine ausreichende Menge Speicherplatz zur Verfügung steht.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

### 5.2 Webserver stellt zu große Datei fest
Stellt der Webserver in Schritt 8 fest, dass durch das Hochladen der Datei eine maximal zulässige Größe überschritten wird (vgl. RL1, RL2), dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass die gewählte Datei zu groß ist beziehungsweise dass dem Benutzerprofil keine ausreichende Menge Speicherplatz zur Verfügung steht.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

### 5.3 Ablehnung der Datei durch den Webserver
Stellt der Webserver in Schritt 8 fest, dass das Hochladen der Datei aus anderen als den bisher benannten Gründen nicht akzeptabel ist, zum Beispiel weil für das Abspeichern der Datei nicht ausreichend viel Speicher zur Verfügung steht, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hochladen der Datei ein Fehler aufgetreten ist, der das Hochladen verhindert hat, der Vorgang aber zu einem späteren Zeitpunkt möglicherweise erfolgreich abgeschlossen werden kann.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

### 5.4 Abbruch durch Benutzer
Bricht der Patient in einem beliebigen Schritt den Vorgang ab, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung wechselt zur vorherigen Ansicht "Dateiliste".
2. Der Anwendungsfall endet als Fehler.

### 5.5 Verbindungsfehler beim Hochladen
Stellt die Webanwendung in Schritt 8 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hochladen der Datei ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

## 6 Schlüsselszenarien
keine

## 7 Nachbedingung

### 7.1 Erfolgreicher Abschluss
Die Datei wurde hochgeladen und wird in der Dateiliste des Verzeichnisses, in das die Datei hochgeladen wurde, aufgeführt.

### 7.2 Fehlerzustand
Die Logdaten wurden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
- Maximale Dateigröße (vgl. RL2)
- Maximale Größe aller Dateien eines Patienten (vgl. RL1)
