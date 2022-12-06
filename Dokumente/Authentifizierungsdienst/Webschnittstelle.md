# Webschnittstelle des Authentifizierungsdienstes

## Registrierung
## Anmelden
## Abmelden
## Social Login
## Passwort ändern
## Passwort zurücksetzen
## Benutzerdetails ändern
## Benutzer löschen
```
POST /auth/delete/
Body:
{
  "token": "<gültiger Token>"
}

Antworten

200 OK
Die Anfrage war erfolgreich und das Konto wurde erfolgreich gelöscht.

400 BAD REQUEST
Die Anfrage war ungültig. Der Fehler wird im Feld "error" der Antwort beschrieben.

401 UNAUTHORIZED
Der angegebene Token ist ungültig oder abgelaufen.
```
