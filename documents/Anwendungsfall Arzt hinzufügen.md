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
2. Der Patient wechselt zur Ansicht "Profileinstellungen".
3. Die Webanwendung zeigt die Ansicht "Profileinstellungen".
4. Der Patient wechselt zur Kategorie "Ärzte verwalten".
5. Die Webanwendung zeigt die Kategorie "Ärzte verwalten".
6. Der Patient wählt "Arzt hinzufügen".
7. Die Webanwendung fragt nach der Identifikationsnummer des Arztes.
8. Der Patient gibt die Identifikationsnummer des Arztes ein.
9. Die Webanwendung sendet die Identifikationsnummer an den Webserver zur Informationsabfrage. Der Webserver gibt zurück, ob die Identifikationsnummer vergeben ist sowie gegebenenfalls Profilinformationen über diesen Arzt, insbesondere Namen, Berufsbezeichnung und Praxisbezeichnung. In diesem Anwendungsfall existiert der Arzt und er ist dem Profil des Benutzers noch nicht hinzugefügt.
10. Die Webanwendung zeigt die empfangenen Informationen über den Arzt an und fragt den Benutzer, ob er diesen Artzt hinzufügen möchte.
11. Der Patient bestätigt dies.
12. Die Webanwendung weise den Webserver an, den Artzt zum Profil des Patienten hinzuzufügen. In diesem Anwendungsfall gelingt dies.
13. Die Webanwendung teilt dem Patienten mit, dass die Aktion erfolgreich ausgeführt wurde.
14. Die Webanwendung wechselt zur vorherigen Ansicht "Profileinstellungen" in der Kategorie "Ärzte verwalten".
15. Der Anwendungsfall endet als Erfolg.

## 5 Alternativer Ablauf

### 5.1 Bereits hinzugefügter Arzt
Stellt der Webserver in Schritt 9 fest, dass der Arzt dem Profil des Benutzers bereits hinzugefügt ist, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass der Arzt dem Profil bereits hinzugefügt ist und zeigt die Informationen über den Arzt an.
2. Der Patient bestätigt dies.
3. Der Standardablauf wird beginnend mit Schritt 14 fortgesetzt.

### 5.2 Nicht existierender Arzt bei der Informationsabfrage
Stellt der Webserver in Schritt 9 fest, dass kein Arzt zur gegebenen Identifikationsnummer existiert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass der gesuchte Arzt nicht existiert.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 5.3 Nicht existierender Arzt beim Hinzufügeversuch
Stellt der Webserver in Schritt 12 fest, dass kein Arzt zur gegebenen Identifikationsnummer existiert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hinzufügen des Arztes ein Fehler aufgetreten ist und bittet ihn, die von Ihm eingegebene Identifikationsnummer zu prüfen.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 5.4 Abbruch durch Benutzer
Bricht der Patient in einem beliebigen Schritt den Vorgang ab, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung wechselt zur vorherigen Ansicht "Profileinstellungen" in der Kategorie "Ärzte verwalten".
2. Der Anwendungsfall endet als Fehler.

### 5.5 Verbindungsfehler bei der Informationsabfrage
Stellt die Webanwendung in Schritt 9 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass bei der Prüfung der eingegebenen Identifikationsnummer ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 5.5 Verbindungsfehler beim Hinzufügen
Stellt die Webanwendung in Schritt 12 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hinzufügen des Arztes ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

## 6 Schlüsselszenarien
keine

## 7 Nachbedingung

### 7.1 Erfolgreicher Abschluss
Der Arzt wurde dem Profil des Patienten hinzugefügt und steht zur Auswahl bei Freigaben zur Verfügung.

### 7.2 Fehlerzustand
Die Logdaten werden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
keine
