# Anwendungsfall: Benutzerregistrierung

## 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Registieren eines neuen Benutzers.

## 2 Beteiligte
- Benutzer

## 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.

## 4 Standardablauf
1. Der Benutzer befindet sich auf der Anmeldeseite.
2. Der Patient wählt "Neuen Benutzer registrieren".
3. Die Webanwendung zeigt die Ansicht "Benutzerregistrierung".
4. Der Benutzer gibt die nötigen Angaben an. ( Vorname, Nachname, Anmeldename, Passwort)
5. Die Webanwendung sendet die Informationen dem Webserver zur Überprüfung.
6. Der Webserver sendet die Informationen an den Dateiablagedienst und dieser legt sie in der Datenbank ab.
7. Die Webanwendung teilt dem Benutzer mit das er erfolgreich registriert wurde.
8. Die Webanwendung loggt den User ein und wechselt auf die Startseite.
9. Der Anwendungsfall endet als Erfolg.


## 5 Alternativer Ablauf

### 5.1 Fehler in der Dateneingabe
1. In Schritt 5 schlägt die Datenüberprüfung fehl.
2. Dies wird dem Benutzer rückgemeldet.
3. Der Ablauf wiederholt Schritt 4.

### 5.2 Fehler beim Ablegen der Daten
1. In Schritt 6 schlägt die Ablage der Daten in die Datenbank fehl.
2. Dies wird dem Benutzer rückgemeldet.
3. Der Ablauf wiederholt Schritt 4.

## 6 Schlüsselszenarien
keine

## 7 Nachbedingung

### 7.1 Erfolgreicher Abschluss
Der Benutzer wurde erfolgreich registiert und kann nun wie gewünscht die Anwendung benutzen.

### 7.2 Fehlerzustand
Die Logdaten werden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
keine
