
## #01 - Authentifizierung mit Benutzername und Passwort

### 1. Kurzbeschreibung
Dieser Anwendungsfall beschreibt den Authentifizierungsvorgang eines Benutzers am System mithilfe seines Benutzernamens und eines Passwortes.

### 2. Beteiligte
- Benutzer

### 3. Vorbedingung
- Eine Netzwerkverbindung zu dem Applikationsserver ist vorhanden.
- Der Browser unterstützt HTML5, CSS3 und JavaScript.

### 4. Standardablauf
1. Der Anwendungsfall beginnt, wenn der Benutzer die Anmeldeseite aufruft.
2. Die Landingpage zeigt eine Anmeldemaske. Auf der Anmeldemaske wird Authentifizierung mittels Benutzername und Passwort ermöglicht und der Login über den Google IDP angeboten.
3. In diesem Anwendungsfall wählt der Benutzer immer die Anmeldung mittels Benutzername und Passwort.
4. Der Benutzer gibt seinen Benutzernamen und sein Passwort in die dafür vorgesehenen Felder ein.
5. Der Benutzer bestätigt die Eingabe.
6. Die Anmeldedaten werden zur Validierung an den Access Manager übermittelt.

### 5. Alternativer Ablauf
5.1 Der Benutzer ruft nicht direkt die Anmeldeseite auf
  1. Ist der Benutzer noch nicht an der Anwendung angemeldet, wird er auf die Anmeldeseite weitergeleitet.
 
5.2 Benutzername oder Passwort inkorrekt
  1. Gibt eine Fehlermeldung aus, dass der Benutzername nicht vorhanden ist.
  2. Dekrementieren die Anzahl von möglichen Anmeldeversuchen um 1.
  3. Wenn die möglichen Anmeldeversuche 0 beträgt, wird dem Browser für 5 Minuten die Anmeldung verwehrt.
  4. Der Anwendungsfall endet mit einem Fehlerzustand

### 6. Schlüsselszenario
[comment]: <> (TODO: Schlüsselszenario)

### 7. Nachbedingung
7.1 Erfolgreicher Abschluss
- Wenn die Authentifizierung erfolgreich ist, wird eine Sitzungs-ID zugewiesen und der User zur Main Page weitergeleitet.
    
7.2 Fehlerzustand
- Die Logdaten werden entsprechend aktualisiert.

### 8. Spezielle Voraussetzungen
[comment]: <> (TODO: Spezielle Voraussetzungen)


## #02 - Authentifizierung mit Google IDP

### 1. Kurzbeschreibung
Dieser Anwendungsfall beschreibt den Authentifizierungsvorgang eines Benutzers am System über den Google IDP.

### 2. Beteiligte
- Benutzer
- Google IDP

### 3. Vorbedingung
- Eine Netzwerkverbindung zu dem Applikationsserver ist vorhanden.
- Eine verbindung mit dem Internet ist vorhanden.
- Der Benutzer muss im besitz eines Google-Kontos sein.
- Der Browser unterstützt HTML5, CSS3 und JavaScript.

### 4. Standardablauf
1. Der Anwendungsfall beginnt, wenn der Benutzer die Anmeldeseite aufruft.
2. Die Landingpage zeigt eine Anmeldemaske. Auf der Anmeldemaske wird Authentifizierung mittels Benutzername und Passwort ermöglicht und der Login über den Google IDP angeboten.
3. In diesem Anwendungsfall wählt der Benutzer immer die Anmeldung über den Google IDP.
4. Der Benutzer wird an den Google Sign-In weitergeleitet.
5. Dort gibt der User seine Google-Anmeldedaten ein und übermittelt sie an Google.
6. Googles IdP überprüft die eingegebenen Anmeldedaten.

### 5. Alternativer Ablauf
5.1 Der Benutzer ruft nicht direkt die Anmeldeseite auf
1. Ist der Benutzer noch nicht an der Anwendung angemeldet, wird er auf die Anmeldeseite weitergeleitet.

5.2  

### 6. Schlüsselszenario
[comment]: <> (TODO: Schlüsselszenario)

### 7. Nachbedingung
7.1 Erfolgreicher Abschluss
- Wenn die Authentifizierung erfolgreich ist, wird eine Sitzungs-ID zugewiesen und der User zur Main Page weitergeleitet.
    
7.2 Fehlerzustand
- Die Logdaten werden entsprechend aktualisiert.

### 8. Spezielle Voraussetzungen
[comment]: <> (TODO: Spezielle Voraussetzungen)
