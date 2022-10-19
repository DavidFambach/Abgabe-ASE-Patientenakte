# Anwendungsfälle 

## #01 - Authentifizierung mit Benutzername und Passwort

### 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt den Authentifizierungsvorgang eines Benutzers am System mithilfe seines Benutzernamens und eines Passwortes.

### 2 Beteiligte
- Benutzer

### 3 Vorbedingung
- Eine Netzwerkverbindung zu dem Applikationsserver ist vorhanden.
- Der Browser unterstützt HTML5, CSS3 und JavaScript.

### 4 Standardablauf
1. Der Anwendungsfall beginnt, wenn der Benutzer die Anmeldeseite aufruft.
2. Die Landingpage zeigt eine Anmeldemaske. Auf der Anmeldemaske wird Authentifizierung mittels Benutzername und Passwort ermöglicht und der Login über den Google IDP angeboten.
3. In diesem Anwendungsfall wählt der Benutzer immer die Anmeldung mittels Benutzername und Passwort.
4. Der Benutzer gibt seinen Benutzernamen und sein Passwort in die dafür vorgesehenen Felder ein.
5. Der Benutzer bestätigt die Eingabe.
6. Die Anmeldedaten werden zur Validierung an den Access Manager übermittelt.

### 5 Alternativer Ablauf
#### 5.1 Der Benutzer ruft nicht direkt die Anmeldeseite auf
  1. Ist der Benutzer noch nicht an der Anwendung angemeldet, wird er auf die Anmeldeseite weitergeleitet.
 
#### 5.2 Benutzername oder Passwort inkorrekt
  1. Gibt eine Fehlermeldung aus, dass der Benutzername nicht vorhanden ist.
  2. Dekrementieren die Anzahl von möglichen Anmeldeversuchen um 1.
  3. Wenn die möglichen Anmeldeversuche 0 beträgt, wird dem Browser für 5 Minuten die Anmeldung verwehrt.
  4. Der Anwendungsfall endet mit einem Fehlerzustand

### 6 Schlüsselszenario
[comment]: <> (TODO: Schlüsselszenario)

### 7 Nachbedingung
#### 7.1 Erfolgreicher Abschluss
- Wenn die Authentifizierung erfolgreich ist, wird eine Sitzungs-ID zugewiesen und der User zur Main Page weitergeleitet.
    
#### 7.2 Fehlerzustand
- Die Logdaten werden entsprechend aktualisiert.

### 8 Spezielle Voraussetzungen
[comment]: <> (TODO: Spezielle Voraussetzungen)


## #02 - Authentifizierung mit Google IDP

### 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt den Authentifizierungsvorgang eines Benutzers am System über den Google IDP.

### 2 Beteiligte
- Benutzer
- Google IDP

### 3 Vorbedingung
- Eine Netzwerkverbindung zu dem Applikationsserver ist vorhanden.
- Eine verbindung mit dem Internet ist vorhanden.
- Der Benutzer muss im besitz eines Google-Kontos sein.
- Der Browser unterstützt HTML5, CSS3 und JavaScript.

### 4 Standardablauf
1. Der Anwendungsfall beginnt, wenn der Benutzer die Anmeldeseite aufruft.
2. Die Landingpage zeigt eine Anmeldemaske. Auf der Anmeldemaske wird Authentifizierung mittels Benutzername und Passwort ermöglicht und der Login über den Google IDP angeboten.
3. In diesem Anwendungsfall wählt der Benutzer immer die Anmeldung über den Google IDP.
4. Der Benutzer wird an den Google Sign-In weitergeleitet.
5. Dort gibt der User seine Google-Anmeldedaten ein und übermittelt sie an Google.
6. Googles IdP überprüft die eingegebenen Anmeldedaten.

### 5 Alternativer Ablauf
5.1 Der Benutzer ruft nicht direkt die Anmeldeseite auf
1. Ist der Benutzer noch nicht an der Anwendung angemeldet, wird er auf die Anmeldeseite weitergeleitet.

### 6 Schlüsselszenario
[comment]: <> (TODO: Schlüsselszenario)

### 7 Nachbedingung
#### 7.1 Erfolgreicher Abschluss
- Wenn die Authentifizierung erfolgreich ist, wird eine Sitzungs-ID zugewiesen und der User zur Main Page weitergeleitet.
    
#### 7.2 Fehlerzustand
- Die Logdaten werden entsprechend aktualisiert.

### 8 Spezielle Voraussetzungen
[comment]: <> (TODO: Spezielle Voraussetzungen)


## #03 - Anwendungsfall: Arzt hinzufügen

### 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Hinzufügen eines Arztes durch einen Patienten, sodass dieser im Benutzerprofil zur Verfügung steht, um Dokumente freizugeben.

### 2 Beteiligte
- Patient

### 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.
- Der Patient ist authentifiziert (vgl. Anwendungsfall: Authentifizierung), es liegt also eine entsprechende gültige Sitzung vor.
- Der Arzt ist registriert und der Patient kennt dessen Identifikationsnummer

### 4 Standardablauf
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

### 5 Alternativer Ablauf

#### 5.1 Bereits hinzugefügter Arzt
Stellt der Webserver in Schritt 9 fest, dass der Arzt dem Profil des Benutzers bereits hinzugefügt ist, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass der Arzt dem Profil bereits hinzugefügt ist und zeigt die Informationen über den Arzt an.
2. Der Patient bestätigt dies.
3. Der Standardablauf wird beginnend mit Schritt 14 fortgesetzt.

#### 5.2 Nicht existierender Arzt bei der Informationsabfrage
Stellt der Webserver in Schritt 9 fest, dass kein Arzt zur gegebenen Identifikationsnummer existiert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass der gesuchte Arzt nicht existiert.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

#### 5.3 Nicht existierender Arzt beim Hinzufügeversuch
Stellt der Webserver in Schritt 12 fest, dass kein Arzt zur gegebenen Identifikationsnummer existiert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hinzufügen des Arztes ein Fehler aufgetreten ist und bittet ihn, die von Ihm eingegebene Identifikationsnummer zu prüfen.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

#### 5.4 Abbruch durch Benutzer
Bricht der Patient in einem beliebigen Schritt den Vorgang ab, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung wechselt zur vorherigen Ansicht "Profileinstellungen" in der Kategorie "Ärzte verwalten".
2. Der Anwendungsfall endet als Fehler.

#### 5.5 Verbindungsfehler bei der Informationsabfrage
Stellt die Webanwendung in Schritt 9 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass bei der Prüfung der eingegebenen Identifikationsnummer ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

#### 5.5 Verbindungsfehler beim Hinzufügen
Stellt die Webanwendung in Schritt 12 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hinzufügen des Arztes ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 7 fortgesetzt, wobei die vom Benutzer bereits eingegebene Identifikationsnummer im Formular erhalten bleibt.

### 6 Schlüsselszenarien
keine

### 7 Nachbedingung

#### 7.1 Erfolgreicher Abschluss
Der Arzt wurde dem Profil des Patienten hinzugefügt und steht zur Auswahl bei Freigaben zur Verfügung.

#### 7.2 Fehlerzustand
Die Logdaten werden entsprechend aktualisiert.

### 8 Spezielle Voraussetzungen
keine


## #04 - Anwendungsfall: Datei teilen

### 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Hochladen einer Datei durch einen Patienten, sodass die Datei im Benutzerprofil des Patienten gespeichert wird.

### 2 Beteiligte
- Patient

### 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.
- Der Patient ist authentifiziert (vgl. Anwendungsfall: Authentifizierung), es liegt also eine entsprechende gültige Sitzung vor.
- Dem Patienten liegt eine Datei zum Hochladen vor

### 4 Standardablauf
1. Der Patient befindet sich nach erfolgter Authentifizierung auf der Startseite der Anwendung.
2. Der Patient wechselt zur Ansicht des Verzeichnisses, in das die Datei hochgeladen werden soll. In diesem Anwendungsfall ist das das Stammverzeichnis.
3. Die Webanwendung zeigt eine Auflistung der Elemente des ausgewählten Verzeichnisses an.
4. Der Patient wählt "Datei hochladen"
5. Die Webanwendung fragt nach einer Datei zum Hochladen
6. Der Patient wählt die hochzuladende Datei aus
7. Die Webanwendung überprüft, ob durch die Datei eine maximal zulässige Größe überschritten wird (vgl. R1, R2). In diesem Anwendungsfall ist das nicht der Fall.
8. Die Webanwendung erzeugt einen neuen Dateischlüssel, mit dem sie die Datei verschlüsselt. Die verschlüsselte Datei wird gemeinsam mit dem durch den öffentlichen Schlüssel des Benutzers verschlüsselten Dateischlüssel an den Webserver übermittelt. In diesem Anwendungsfall gelingt das.
9. Die Webanwendung teilt dem Patienten mit, dass die Aktion erfolgreich ausgeführt wurde.
10. Die Webanwendung wechselt zur vorherigen Ansicht "Dateiliste" und reflektiert dabei den neuen Zustand.
11. Der Anwendungsfall endet als Erfolg.

### 5 Alternativer Ablauf

- ablehnen des speicherns (z. b. kein speicherplatz)
- datei mit demselben namen ist bereits vorhanden
- abbruch durch benutzer

#### 5.1 Webanwendung stellt zu große Datei fest
Stellt die Webanwendung in Schritt 7 fest, dass durch das Hochladen der Datei eine maximal zulässige Größe überschritten wird (vgl. R1, R2), dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass die gewählte Datei zu groß ist beziehungsweise dass dem Benutzerprofil keine ausreichende Menge Speicherplatz zur Verfügung steht.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

#### 5.2 Webserver stellt zu große Datei fest
Stellt der Webserver in Schritt 8 fest, dass durch das Hochladen der Datei eine maximal zulässige Größe überschritten wird (vgl. R1, R2), dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass die gewählte Datei zu groß ist beziehungsweise dass dem Benutzerprofil keine ausreichende Menge Speicherplatz zur Verfügung steht.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

#### 5.3 Ablehnung der Datei durch den Webserver
Stellt der Webserver in Schritt 8 fest, dass das Hochladen der Datei aus anderen als den bisher benannten Gründen nicht akzeptabel ist, zum Beispiel weil für das Abspeichern der Datei nicht ausreichend viel Speicher zur Verfügung steht, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hochladen der Datei ein Fehler aufgetreten ist, der das Hochladen verhindert hat, der Vorgang aber zu einem späteren Zeitpunkt möglicherweise erfolgreich abgeschlossen werden kann.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

#### 5.4 Abbruch durch Benutzer
Bricht der Patient in einem beliebigen Schritt den Vorgang ab, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung wechselt zur vorherigen Ansicht "Dateiliste".
2. Der Anwendungsfall endet als Fehler.

#### 5.5 Verbindungsfehler beim Hochladen
Stellt die Webanwendung in Schritt 8 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Hochladen der Datei ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Der Standardablauf wird beginnend mit Schritt 5 fortgesetzt.

### 6 Schlüsselszenarien
keine

### 7 Nachbedingung

#### 7.1 Erfolgreicher Abschluss
Die Datei wurde hochgeladen und wird in der Dateiliste des Verzeichnisses, in das die Datei hochgeladen wurde, aufgeführt.

#### 7.2 Fehlerzustand
Die Logdaten wurden entsprechend aktualisiert.

### 8 Spezielle Voraussetzungen
- Maximale Dateigröße (vgl. R2)
- Maximale Größe aller Dateien eines Patienten (vgl. R1)
