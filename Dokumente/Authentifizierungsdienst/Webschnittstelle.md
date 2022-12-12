# Webschnittstelle des Authentifizierungsdienstes

## Operation POST /register/
Erstellt ein Benutzerkonto an der Anwendung.
Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
 - username: Der Anzeigename in der Anwendung
 - email: Die Emailadresse, die zur Authentifizierung verwendet wird.
 - password: Das Passwort, das zur Authentifizierung verwendet wird.

Antwortformat:
``` json
{
	"username": <username>,
	"email": <email>
}
```

## Operation POST /login/
Gibt Access und Refresch Tokens für die Anwendung zurück.
Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
 - email: Die Emailadresse, die zur Authentifizierung verwendet wird.
 - password: Das Passwort, das zur Authentifizierung verwendet wird.

Antwortformat:
``` json
{
	"email": <Emailadresse>,
	"tokens": {
		"refresh": <Refresh Token>,
		"access": <Access Token>
	}
}
```

## Operation POST /logout/
Setzt den Refreshtoken auf eine Blacklist. Dieser ist mit sofortiger Wirkung ungültig.
Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
 - token: Benutzerbezogener Refreshtoken im JWT Format.

Antwortformat:
``` json
{
	"success": true,
	"message": "Loged out successfully"
}
```

## Operation GET /email-verify/?token=\<token\>
Wird beim Abschliesen der Registrierung, zur Validierung der Emailadresse aufgerufen.
Anfragetyp: `application/json`
Antworttyp: leerer Antwortkörper

Parameter:
 - token: Ein benutzerbezogener Access Token mit 1 Stunde gültigkeit.

Antwortformat:
```  
```

## Operation POST /password-change/
Ändert das Passwort auf den im Anfragekörper enthaltenen Wert. Die Anfrage ist nur dann gültig, wenn der Token valide und das alte Kennwort korrekt ist. 

Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
- password: Das neue Anmeldekennwort
- token: Benutzerbezogener Refreshtoken im JWT Format.
- old_password: Das bisher gültige Anmeldekennwort

Antwortformat:
``` json
{
	"success": true,
	"message": "Password change success"
}
```

## Operation POST /token/refresh/
Gibt einen aus dem Refresh Token generierten, gültigen Access Token zurück.
Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
 - token: Benutzerbezogener Refresh Token

Antwortformat:
``` json
{
	"access": <Access Token>
}
```

Dabei ist Access Token ein gültiger JWT. 

## Operation POST /delete/
Löscht alle Benutzerbezogenen daten aus dem Authentifizierungsdienst und schreibt eine Message in die user-update-queue. 
Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
 - token: Benutzerbezogener Refreshtoken im JWT Format.

Antwortformat:
``` json
{
	"result": "User was successfully deleted"
}
```

## Operation POST /google/
Authentifiziert einen Benutzer anhand eines vom Google IDP ausgestellten Authentifizierungscodes.
Anfragetyp: `application/json`
Antworttyp: `application/json`

Parameter:
- code: Der vom Google IDP ausgestellte Authentifizierungscode.
- redirect_uri: Zeigt auf das Frontend. Muss gleich der redirect_uri sein, die das Frontend zur Abfrage des Authentifizierungscodes verwendet hat.

Antwortformat:
``` json
{
	"email": <Emailadresse>,
	"tokens": {
		"refresh": <Refresh Token>,
		"access": <Access Token>
	}
}
```

## Operation GET /google/client-id
Gibt die im Authentifizierungsdienst verwendete Google Client ID zurück.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Antwortformat:
``` json
<Client-ID>
```

Dabei ist Client-ID ein JSON-String.
