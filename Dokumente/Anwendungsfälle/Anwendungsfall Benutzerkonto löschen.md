# Anwendungsfall: Benutzerkonto löschen

## 1 Kurzbeschreibung
Dieser Anwendungsfall beschreibt das Löschen eines bestehenden Benutzerkontos. Damit verbunden ist die Löschung aller Dateien im gelöschten Benutzerkonto.

## 2 Beteiligte
- Patient

## 3 Vorbedingung
- Eine Netzwerkverbindung mit dem Webserver ist vorhanden.
- Der Patient ist authentifiziert (vgl. Anwendungsfall: Authentifizierung), es liegt also eine entsprechende gültige Sitzung vor.

## 4 Standardablauf
1. Der Patient befindet sich nach erfolgter Authentifizierung auf der Startseite der Anwendung.
2. Der Patient wechselt zur Profilansicht.
3. Die Webanwendung zeigt eine Auflistung der möglichen Profilaktionen, einschließlich der Möglichkeit, das Konto zu löschen.
4. Der Patient wählt "Benutzerkonto löschen".
5. Die Webanwendung fragt den Patienten nach einer erneuten Bestätigung und weist darauf hin, dass dadurch alle Daten, die dem Benutzerkonto des Patienten zugeordnet sind, verloren gehen.
6. Der Patient bestätigt dies.
7. Die Löschanfrage wird an den Webserver übermittelt. In diesem Anwendungsfall gelingt dies.
8. Die Webanwendung wechselt zur Anmeldemaske.
9. Der Anwendungsfall endet als Erfolg.

## 5 Alternativer Ablauf

### 5.1 Abbruch durch Benutzer
Bricht der Patient in einem beliebigen Schritt den Vorgang ab, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung wechselt zur vorherigen Ansicht.
2. Der Anwendungsfall endet als Fehler.

### 5.2 Verbindungsfehler
Stellt die Webanwendung in Schritt 7 fest, dass der Webserver nicht erreichbar ist, oder aus anderen Gründen keine verwertbare Antwort liefert, dann läuft der Anwendungsfall wie folgt weiter ab:
1. Die Webanwendung teilt dem Patienten mit, dass beim Löschen des Benutzerkontos ein Verbindungsfehler aufgetreten ist und weist ihn an, den Vorgang zu wiederholen oder die Verbindung zu überprüfen.
2. Die Webanwendung wechselt zur vorherigen Ansicht.
3. Der Anwendungsfall endet als Fehler.

## 6 Schlüsselszenarien
keine

## 7 Nachbedingung

### 7.1 Erfolgreicher Abschluss
Das Benutzerkonto wurde aus der Datenbank des Authentifizierungsdienstes gelöscht und eine entsprechende Nachricht an die übrigen Dienste ausgegeben.

### 7.2 Fehlerzustand
Die Logdaten wurden entsprechend aktualisiert.

## 8 Spezielle Voraussetzungen
keine
