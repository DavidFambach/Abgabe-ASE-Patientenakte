# Key concept: Google IdP  
Mithilfe des Google Sign-In wird ein SSO ermöglicht. Das bedeutet, dass die Benutzer unsere Anwendung ihr Google-Konto zur Authentisierung verwenden können. Dadurch sind keine gesonderten Zugangsdaten für unsere Anwendung nötig. Dadurch wird die User Experience verbessert und demzufolge die Akzeptanz gegenüber den Benutzern unserer Anwendung. [Mehr Informationen](https://developers.google.com/identity/sign-in/web/server-side-flow)

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

Der Austausch der Daten zwischen den einzelnen Beteiligten erfolgt über das Hypertext Transfer Protocol (HTTP).