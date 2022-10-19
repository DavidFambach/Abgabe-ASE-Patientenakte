# Authentifizierung mit Google IDP

## 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt den Authentifizierungsvorgang eines Benutzers am System über den Google IDP.

## 2 Beteiligte
- Benutzer
- Google IDP

## 3 Vorbedingung
- Eine Netzwerkverbindung zu dem Applikationsserver ist vorhanden.
- Eine verbindung mit dem Internet ist vorhanden.
- Der Benutzer muss im besitz eines Google-Kontos sein.
- Der Browser unterstützt HTML5, CSS3 und JavaScript.

## 4 Standardablauf
1. Der Anwendungsfall beginnt, wenn der Benutzer die Anmeldeseite aufruft.
2. Die Landingpage zeigt eine Anmeldemaske. Auf der Anmeldemaske wird Authentifizierung mittels Benutzername und Passwort ermöglicht und der Login über den Google IDP angeboten.
3. In diesem Anwendungsfall wählt der Benutzer immer die Anmeldung über den Google IDP.
4. Der Benutzer wird an den Google Sign-In weitergeleitet.
5. Dort gibt der User seine Google-Anmeldedaten ein und übermittelt sie an Google.
6. Googles IdP überprüft die eingegebenen Anmeldedaten.

## 5 Alternativer Ablauf
### 5.1 Der Benutzer ruft nicht direkt die Anmeldeseite auf
1. Ist der Benutzer noch nicht an der Anwendung angemeldet, wird er auf die Anmeldeseite weitergeleitet.

## 6 Schlüsselszenario
[comment]: <> (TODO: Schlüsselszenario)

## 7 Nachbedingung
### 7.1 Erfolgreicher Abschluss
- Wenn die Authentifizierung erfolgreich ist, wird eine Sitzungs-ID zugewiesen und der User zur Main Page weitergeleitet.
    
### 7.2 Fehlerzustand
- Die Logdaten werden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
[comment]: <> (TODO: Spezielle Voraussetzungen)