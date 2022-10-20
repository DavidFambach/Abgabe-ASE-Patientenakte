# Key concept: Google IdP  
Mithilfe des Google Sign-In wird ein SSO ermöglicht. Das bedeutet, dass die Benutzer unsere Anwendung ihr Google-Konto zur Authentisierung verwenden können. Der Einsatz von SSO schafft viele Vorteile:

- Die einmalige Anmeldung für den Zugriff auf verschiedene Anwendungen spart Zeit.
- Die Qualität der Zugangsdaten verbessert sich.
- Autorisierungsdienste nutzen sichere Prüfverfahren.
- Die Akzeptanz des Authentisierungsvorgangs steigt.
- Die Benutzerfreundlichkeit für Mitarbeiter wächst.
- Reduzierung der Anmeldungen und Anmeldedaten sorgen für mehr Sicherheit.

Diese Vorteile verbessern die User experience der Benutzer und können die Sicherheit unserer Anwendung verbessern.

```mermaid
sequenceDiagram
autonumber
participant Client
participant Applikationsserver
participant Google API Server
participant OAuth 2.0 Dialog

Client ->> Google API Server: Benutzer klickt auf den Sign-In Button. Die Autorisierungsanfrage <br> wurde an Google's OAuth Server gesendet
Google API Server ->> OAuth 2.0 Dialog: Der OAuth Dialog wird <br> für den Benutzer aufgerufen
OAuth 2.0 Dialog ->> Client: access_token, id_token und ein Einmalcode werden zurückgegeben
Client ->> Applikationsserver: Client sendet <br> den Einmalcode an den Server
Applikationsserver ->> Google API Server: Server tauscht Einmalcode gegen <br> access_token und id_token 
Google API Server ->> Applikationsserver: Google gibt den access_token <br> und den id_token zurück
Applikationsserver -->> Client: Server bestätigt <br> "fully logged in" zum Client
```

Der Austausch der Daten zwischen den einzelnen Beteiligten erfolgt über das Hypertext Transfer Protocol (HTTP).  [Mehr Informationen](https://developers.google.com/identity/sign-in/web/server-side-flow)