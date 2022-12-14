# Anwendungsfall: Arzt hinzufügen

## 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Hinzufügen eines Arztes durch einen Patienten, sodass dieser im Benutzerprofil zur Verfügung steht, um Dokumente freizugeben.

## 2 Beteiligte
- Patient

## 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.
- Der Patient ist authentifiziert (vgl. Anwendungsfall: Authentifizierung), es liegt also eine entsprechende gültige Sitzung vor.
- Der Arzt ist registriert und der Patient kennt dessen Identifikationsnummer

## 4 Standardablauf
1. Der Patient befindet sich nach erfolgter Authentifizierung auf der Startseite der Anwendung.
2. Der Patient wechselt zur Seite "Kontakte verwalten".
3. Die Webanwendung zeigt die Seite "Kontakte verwalten".
4. Der Patient wählt "Arzt hinzufügen".
5. Die Webanwendung fragt nach der Identifikationsnummer des Arztes.
6. Der Patient gibt die Identifikationsnummer des Arztes ein.
7. Die Webanwendung sendet die Identifikationsnummer an den Webserver zur Informationsabfrage. Der Webserver gibt zurück, ob die Identifikationsnummer vergeben ist sowie gegebenenfalls Profilinformationen über diesen Arzt, insbesondere Namen. In diesem Anwendungsfall existiert der Arzt und er ist dem Profil des Benutzers noch nicht hinzugefügt.
8. Die Webanwendung zeigt die empfangenen Informationen über den Arzt an und fragt den Benutzer, ob er diesen Arzt hinzufügen möchte.
9. Der Patient bestätigt dies.
10. Die Webanwendung weist den Webserver an, den Arzt zum Profil des Patienten hinzuzufügen. In diesem Anwendungsfall gelingt dies.
11. Die Webanwendung teilt dem Patienten mit, dass die Aktion erfolgreich ausgeführt wurde.
12. Die Webanwendung wechselt zur vorherigen Ansicht
13. Der Anwendungsfall endet als Erfolg.

## 5 Alternativer Ablauf

### 5.1 Bereits hinzugefügter Arzt
Stellt der Webserver in Schritt 7 fest, dass der Arzt dem Profil des Benutzers bereits hinzugefügt ist, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass der Arzt dem Profil bereits hinzugefügt ist und zeigt die Informationen über den Arzt an.
2. Der Patient bestätigt dies.
3. Der Standardablauf wird beginnend mit Schritt 12 fortgesetzt.

### 5.2 Nicht existierender Arzt bei der Informationsabfrage
Stellt der Webserver in Schritt 7 fest, dass kein Arzt zur gegebenen Identifikationsnummer existiert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass der gesuchte Arzt nicht existiert.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 5.3 Nicht existierender Arzt beim Hinzufügeversuch
Stellt der Webserver in Schritt 10 fest, dass kein Arzt zur gegebenen Identifikationsnummer existiert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hinzufügen des Arztes ein Fehler aufgetreten ist und bittet ihn, die von Ihm eingegebene Identifikationsnummer zu prüfen.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 5.4 Abbruch durch Benutzer
Bricht der Patient in einem beliebigen Schritt den Vorgang ab, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung wechselt zur vorherigen Ansicht.
2. Der Anwendungsfall endet als Fehler.

### 5.5 Verbindungsfehler bei der Informationsabfrage
Stellt die Webanwendung in Schritt 7 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass bei der Prüfung der eingegebenen Identifikationsnummer ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 5.5 Verbindungsfehler beim Hinzufügen
Stellt die Webanwendung in Schritt 10 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hinzufügen des Arztes ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

## 6 Schlüsselszenarien
keine

## 7 Nachbedingung

### 7.1 Erfolgreicher Abschluss
Der Arzt wurde dem Profil des Patienten hinzugefügt und steht zur Auswahl bei Freigaben zur Verfügung.

### 7.2 Fehlerzustand
Die Logdaten werden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
keine
