# Webschnittstelle des Dateiverwaltungsdienstes

## Operation GET /userinfo/\<Benutzer-ID\>
Ruft Informationen über einen Benutzer ab.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, über den Informationen angefordert werden.

Antwortformat:
```  
{
	"status": "<Status>",
	"userinfo": {
		"personalRootDirectory": <Verzeichnis-ID>,
		"ownShares": [<ID einer eigenen Freigabe>, ...],
		"receivedShares": [<ID einer erhaltenen Freigabe>, ...]
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten.

Dabei ist Verzeichnis-ID die ID des Wurzelverzeichnisses der persönlichen Dateiablage des Benutzers. Der Schlüssel `userinfo` ist nur vorhanden, wenn die Aktion erfolgreich war.
Die Liste `ownShares` enthält die IDs der vom Benutzer erstellten Freigaben. Die Reihenfolge der IDs ist undefiniert.
DIe Liste `receivedShares` enthält die IDs der Freigaben, die andere Benutzer dem Benutzer gegenüber eingeräumt haben. Die Reihenfolge der IDs ist undefiniert.

## Operation GET /file/\<Datei-ID\>?user=\<Benutzer-ID\>
Gibt den gespeicherten Dateiinhalt zurück.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/octet-stream` oder `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, der die Datei anfragt. Das sollte der Dateibesitzer oder ein Benutzer, demgenüber Leseberechtigungen für die Datei eingeräumt wurden, sein.
 - Datei-ID: Die ID der angefragten Datei.

Falls die Aktion erfolgreich ist, enthält die Antwort den Inhalt der angefragten Datei.

Antwortformat im Fehlerfall:
```  
{
	"status": "<Status>"
}
```

Dabei ist Status einer der folgenden Werte:
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für die Datei oder die Datei existiert nicht.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten.

## Operation PUT /file/\<Datei-ID\>?user=\<Benutzer-ID\>&name=\<Dateiname\>&parentDirectory=\<Verzeichnis-ID\>&writebody
Aktualisiert eine bestehende Datei. Diese Operation kann keine neue Datei erzeugen.
Der Query-Parameter `writebody` ist optional. Wird er angegeben, wird der Inhalt der Datei durch den Inhalt der Anfrage ersetzt. Wird er nicht angegeben, muss die Anfrage leer sein.
Anfragetyp: `application/octet-stream` oder leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Datei-ID: Die ID der zu ändernden Datei.
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.
 - Dateiname: Ein neuer Name für die Datei. Dieser Parameter ist optional. Wird er nicht angegeben, wird die Datei nicht umbenannt.
 - Verzeichnis-ID: Die ID des Verzeichnisses, in das die Datei verschoben werden soll. Dieser Parameter ist optional. Wird er nicht angegeben, wird die Datei nicht verschoben.

Antwortformat:
```  
{
	"status": "<Status>",
	"file": {
		"id": <Datei-ID>,
		"name": <Dateiname>,
		"owner": {
			"id": <Besitzer-ID>,
			"displayName": "<Besitzer-Anzeigename>"
		},
		"parentDirectory": <Verzeichnis-ID>
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für die Datei oder die Datei existiert nicht. Die bestehende Datei wurde nicht verändert, falls sie existiert.
 - `duplicate_name`: Es existiert bereits eine Datei oder ein Verzeichnis mit demselben Namen am Zielort. Die bestehende Datei wurde nicht verändert.
 - `permission_denied`: Es wird versucht, den Dateiinhalt zu verändern, und der Benutzer besitzt lediglich Leseberechtigungen für die Datei oder es wird versucht, die Datei umzubenenen und der Benutzer hat für die Datei oder das Verzeichnis, in dem sie sich befindet, keine Schreibberechtigungen, oder es wird versucht, die Datei zu verschieben und der Benutzer hat für das Quellverzeichnis, das Zielverzeichnis oder die Datei keine Schreibberechtigungen. Die bestehende Datei wurde nicht verändert.
 - `transferral_rejected`: Das Quellverzeichnis und das Zielverzeichnis gehören zu den Dateibäumen verschiedener Benutzer. Die bestehende Datei wurde nicht verändert.
 - `quota_exceeded`: Der Dateiinhalt ist zu groß oder die Veränderung würde zu einer Überschreitung des Speicherkontingents für den Benutzer führen. Die bestehende Datei wurde nicht verändert.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Die bestehende Datei wurde nicht verändert.

Dabei ist Besitzer-ID die ID des Dateibesitzers und Besitzer-Anzeigename der Anzeigename des Besitzers. Der Schlüssel `file` ist nur vorhanden, wenn die Aktion erfolgreich war.

## Operation POST /file/?user=\<Benutzer-ID\>&name=\<Dateiname\>&parentDirectory=\<Verzeichnis-ID\>
Erzeugt eine neue Datei mit dem Inhalt aus der Anfrage im gegebenen Verzeichnis. Der Besitzer des Verzeichnisses wird der Besitzer der neuen Datei.
Anfragetyp: `application/octet-stream`
Antworttyp: `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.
 - Dateiname: Der Name der neu angelegten Datei.
 - Verzeichnis-ID: Die ID des Verzeichnisses, in dem die Datei angelegt werden soll.

Antwortformat:
```  
{
	"status": "<Status>",
	"file": {
		"id": <Datei-ID>,
		"name": <Dateiname>,
		"owner": {
			"id": <Besitzer-ID>,
			"displayName": "<Besitzer-Anzeigename>"
		},
		"parentDirectory": <Verzeichnis-ID>
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für das Verzeichnis oder das Verzeichnis existiert nicht. Es wurde keine Datei angelegt.
 - `duplicate_name`: Es existiert bereits eine Datei oder ein Verzeichnis mit demselben Namen am Zielort. Es wurde keine Datei angelegt.
 - `permission_denied`: Der Benutzer besitzt lediglich Leseberechtigungen für das Verzeichnis. Es wurde keine Datei angelegt.
 - `quota_exceeded`: Der Dateiinhalt ist zu groß oder die Veränderung würde zu einer Überschreitung des Speicherkontingents für den Benutzer führen. Es wurde keine Datei angelegt.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Es wurde keine Datei angelegt.

Dabei ist Datei-ID die ID der neu angelegten Datei, Besitzer-ID die ID des Dateibesitzers und Besitzer-Anzeigename der Anzeigename des Besitzers. Der Schlüssel `file` ist nur vorhanden, wenn die Aktion erfolgreich war.

## Operation DELETE /file/\<Datei-ID\>?user=\<Benutzer-ID\>
Löscht eine bestehende Datei.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Datei-ID: Die ID der zu löschenden Datei.
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.

Antwortformat:
```  
{
	"status": "<Status>"
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für die Datei oder die Datei existiert nicht. Die bestehende Datei wurde nicht gelöscht, falls sie existiert.
 - `permission_denied`: Der Benutzer hat für die Datei oder für das Elternverzeichnis keine Schreibberechtigungen. Die bestehende Datei wurde nicht gelöscht.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Die bestehende Datei wurde nicht gelöscht.

## Operation GET /dir/\<Verzeichnis-ID\>?user=\<Benutzer-ID\>
Gibt Informationen über ein Verzeicnis zurück.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, der das Verzeichnis anfragt.
 - Verzeichnis-ID: Die ID des Angefragen Verzeichnisses.

Antwortformat:
```  
{
	"status": "<Status>",
	"directory": {
		"id": <Verzeichnis-ID>,
		"name": <Verzeichnisname>,
		"owner": {
			"id": <Besitzer-ID>,
			"displayName": "<Besitzer-Anzeigename>"
		},
		"parentDirectory": <Elternverzeichnis-ID>,
		"children": [
			{
				"type": "file",
				"file": {
					"id": <ID einer enthaltenenen Datei>,
					"name": <Name einer enthaltenenen Datei>,
					"owner": {
						"id": <Besitzer-ID>,
						"displayName": "<Besitzer-Anzeigename>"
					},
					"parentDirectory": <Verzeichnis-ID>
				}
			},
			{
				"type": "directory",
				"directory": {
					"id": <ID eines enthaltenenen Verzeichnisses>,
					"name": <Name eines enthaltenenen Verzeichnisses>,
					"owner": {
						"id": <Besitzer-ID>,
						"displayName": "<Besitzer-Anzeigename>"
					},
					"parentDirectory": <Verzeichnis-ID>
				}
			},
			...
		]
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für das Verzeichnis oder das Verzeichnis existiert nicht.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten.

Dabei ist Verzeichnisname der Name des Verzeichnisses und Elternverzeichnis-ID die ID des Elternverzeichnisses. Der Schlüssel `directory` ist nur vorhanden, wenn die Aktion erfolgreich war.
Der Liste `children` enthält einen Eintrag für jede Datei und jedes Verzeichnis, dessen Elternverzeichnis das angefragte Verzeichnis ist. Die Reihenfolge der Einträge ist nicht festgelegt. Jeder dieser Einträge hat für `type` den Wert `file` falls er eine Datei repräsentiert oder `directory` falls er ein Verzeichnis repräsentiert. Im ersten Fall existiert ein weiterer Schlüssel `file` mit Informationen über die Datei, insbesondere die ID, den Namen und den Besitzer der Datei. Im zweiten Fall existiert ein weiterer Schlüssel `directory` mit Informationen über das Verzeichnis, insbesondere die ID, den Namen und den Besitzer des Verzeichnisses. Der Inhalt des Verzeichnisses wird nicht aufgelistet.

## Operation PUT /dir/\<Verzeichnis-ID\>?user=\<Benutzer-ID\>&name=\<Verzeichnisname\>&parentDirectory=\<Elternverzeichnis-ID\>
Aktualisiert ein bestehendes Verzeichnis. Diese Operation kann kein neues Verzeichnis erzeugen.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Verzeichnis-ID: Die ID des zu ändernden Verzeichnisses.
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.
 - Verzeichnisname: Ein neuer Name für das Verzeichnis. Dieser Parameter ist optional. Wird er nicht angegeben, wird das Verzeichnis nicht umbenannt.
 - Elternverzeichnis-ID: Die ID des Verzeichnisses, in das das Verzeichnis verschoben werden soll. Dieser Parameter ist optional. Wird er nicht angegeben, wird das Verzeichnis nicht verschoben.

Antwortformat:
```  
{
	"status": "<Status>",
	"directory": {
		"id": <Verzeichnis-ID>,
		"name": <Verzeichnisname>,
		"owner": {
			"id": <Besitzer-ID>,
			"displayName": "<Besitzer-Anzeigename>"
		},
		"parentDirectory": <Elternverzeichnis-ID>
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für das Verzeichnis oder das Verzeichnis existiert nicht. Das bestehende Verzeichnis wurde nicht verändert, falls es existiert.
 - `duplicate_name`: Es existiert bereits eine Datei oder ein Verzeichnis mit demselben Namen am Zielort. Das bestehende Verzeichnis wurde nicht verändert.
 - `permission_denied`: Es wird versucht, das Verzeichnis umzubenenen und der Benutzer hat für das Verzeichnis oder Elternverzeichnis keine Schreibberechtigungen, oder es wird versucht, das Verzeichnis zu verschieben und der Benutzer hat für das Quellverzeichnis, das Zielverzeichnis oder das Verzeichnis selbst keine Schreibberechtigungen. Das bestehende Verzeichnis wurde nicht verändert.
 - `unmovable_directory`: Es wird versucht, ein Wurzelverzeichnis zu verschieben. Das bestehende Verzeichnis wurde nicht verändert.
 - `cycle_detected`: Es wird versucht, das Verzeichnis in einer Weise zu verschieben, dass es transitiv sein eigenes Elternverzeichnis wird. Das bestehende Verzeichnis wurde nicht verändert.
 - `transferral_rejected`: Das Quellverzeichnis und das Zielverzeichnis gehören zu den Dateibäumen verschiedener Benutzer. Das bestehende Verzeichnis wurde nicht verändert.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Das bestehende Verzeichnis wurde nicht verändert.

Dabei ist Besitzer-ID die ID des Verzeichnisbesitzers und Besitzer-Anzeigename der Anzeigename des Besitzers. Der Schlüssel `directory` ist nur vorhanden, wenn die Aktion erfolgreich war.

## Operation POST /dir/?user=\<Benutzer-ID\>&name=\<Verzeichnisname\>&parentDirectory=\<Elternverzeichnis-ID\>
Erzeugt ein neues Verzeichnis im gegebenen Elternverzeichnis. Der Besitzer des Elternverzeichnis wird der Besitzer der neuen Verzeichnisses.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.
 - Verzeichnisname: Der Name des neu angelegten Verzeichnisses.
 - Elternverzeichnis-ID: Die ID des Verzeichnisses, in dem das Verzeichnis angelegt werden soll.

Antwortformat:
```  
{
	"status": "<Status>",
	"directory": {
		"id": <Verzeichnis-ID>,
		"name": <Verzeichnisname>,
		"owner": {
			"id": <Besitzer-ID>,
			"displayName": "<Besitzer-Anzeigename>"
		},
		"parentDirectory": <Elternverzeichnis-ID>
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für das Elternverzeichnis oder das Elternverzeichnis existiert nicht. Es wurde kein Verzeichnis angelegt.
 - `duplicate_name`: Es existiert bereits eine Datei oder ein Verzeichnis mit demselben Namen am Zielort. Es wurde kein Verzeichnis angelegt.
 - `permission_denied`: Der Benutzer besitzt lediglich Leseberechtigungen für das Elternverzeichnis. Es wurde kein Verzeichnis angelegt.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Es wurde kein Verzeichnis angelegt.

Dabei ist Verzeichnis-ID die ID des neu angelegten Verzeichnisses, Besitzer-ID die ID des Verzeichnisbesitzers und Besitzer-Anzeigename der Anzeigename des Besitzers. Der Schlüssel `directory` ist nur vorhanden, wenn die Aktion erfolgreich war.

## Operation DELETE /dir/\<Verzeichnis-ID\>?user=\<Benutzer-ID\>&cascade
Löscht eine bestehendes Verzeichnis.
Der Query-Parameter `cascade` ist optional. Wird er angegeben, wird auch der Verzeichnisinhalt rekursiv gelöscht. Wird er nicht angegeben, wird das Verzeichnis nur gelöscht, wenn es leer ist.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Verzeichnis-ID: Die ID des zu löschenden Verzeichnisses.
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.

Antwortformat:
```  
{
	"status": "<Status>"
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Leseberechtigungen für das Verzeichnis oder das Verzeichnis existiert nicht. Das bestehende Verzeichnis wurde nicht gelöscht, falls es existiert.
 - `not_empty`: Das Verzeichnis ist nicht leer und die Option `cascade` wurde nicht angegeben. Es wurden keine Dateien oder Verzeichnisse gelöscht.
 - `permission_denied`: Der Benutzer hat für mindestens eine Datei oder mindestens ein Verzeichnis, das gelöscht werden soll, oder für das Elternverzeichnis einer solchen Datei oder eines solchen Verzeichnisses keine Schreibberechtigungen. Es wurden keine Dateien oder Verzeichnisse gelöscht.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Es wurden keine Dateien oder Verzeichnisse gelöscht.

## Operation GET /share/\<Freigabe-ID\>?user=\<Benutzer-ID\>
Gibt den gespeicherten Dateiinhalt zurück.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/octet-stream` oder `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, der die Datei anfragt. Das sollte der Dateibesitzer oder ein Benutzer, demgenüber Leseberechtigungen für die Datei eingeräumt wurden, sein.
 - Datei-ID: Die ID der angefragten Datei.

Falls die Aktion erfolgreich ist, enthält die Antwort den Inhalt der angefragten Datei.

Antwortformat im Fehlerfall:
```  
{
	"status": "<Status>",
	"share": {
		"id": <Freigabe-ID>,
		"issuer": {
			"id": <Ersteller-ID>,
			"displayName": "<Ersteller-Anzeigename>"
		},
		"subject": {
			"id": <Betroffener-ID>,
			"displayName": "<Betroffener-Anzeigename>"
		},
		"target": {
			"type": "<Zieltyp>",
			"id": <Ziel-ID>
		},
		"canWrite": <Schreibberechtigung>
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Berechtigung, die Freigabe einzusehen, oder die Freigabe existiert nicht.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten.

Dabei ist Ersteller-ID die ID des Freigabeerstellers, Ersteller-Anzeigename der Anzeigename des Freigabeerstellers, Betroffener-ID die ID des Betroffenen, Betroffener-Anzeigename der Anzeigename des Betroffenen, Zieltyp der Typ des Freigabeziels und Ziel-ID die ID des Freigabeziels. Der Zieltyp ist entweder `file`, falls es sich um eine Dateifreigabe handelt, oder `directory`, falls es sich um eine Verzeichnisfreigabe handelt. Im ersten Fall ist die Ziel-ID eine Datei-ID. Im zweiten Fall sit die Ziel-ID eine Verzeichnis-ID. Der Schlüssel `share` ist nur vorhanden, wenn die Aktion erfolgreich war.
Schreibberechtigung hat den Wert `true`, falls die Freigabe Leseberechtigungen und Schreibberechtigungen einräumt, oder `false`, falls die Freigabe nur Leseberechtigungen einräumt.

## Operation POST /share/?user=\<Benutzer-ID\>&subject=\<Betroffener-ID\>&targetType=\<Zieltyp\>&targetID=\<Ziel-ID\>&canWrite
Erzeugt eine neue Freigabe für den gegebenen Betroffenen und das gegebene Ziel.
Der Query-Parameter `canWrite` ist optional. Wird er angegeben, werden dem Betroffenen Leseberechtigungen und Schreibberechtigungen eingeräumt. Wird er nicht angegeben, werden dem Betroffenen nur Leseberechtigungen eingeräumt.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.
 - Betroffener-ID: Die ID des Benutzers, für den das Ziel freigegeben werden soll.
 - Zieltyp: `file` falls eine Dateifreigabe erstellt werden soll oder `directory` falls eine Verzeichnisfreigabe erstellt werden soll.
 - Ziel-ID: Die ID der Datei oder des Verzeichnisses, das freigegeben werden soll.

Antwortformat:
```  
{
	"status": "<Status>",
	"share": {
		"id": <Freigabe-ID>,
		"issuer": {
			"id": <Benutzer-ID>,
			"displayName": "<Benutzer-Anzeigename>"
		},
		"subject": {
			"id": <Betroffener-ID>,
			"displayName": "<Betroffener-Anzeigename>"
		},
		"target": {
			"type": "<Zieltyp>",
			"id": <Ziel-ID>
		},
		"canWrite": <Schreibberechtigung>
	}
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `invalid_subject`: Der Betroffene existiert nicht oder ist nicht gültig, zum Beispiel weil es der Freigabeersteller selbst ist. Es wurde keine Freigabe angelegt.
 - `target_not_found`: Der Benutzer hat keine Leseberechtigungen für Freigabeziel oder das Freigabeziel existiert nicht. Es wurde keine Freigabe angelegt.
 - `permission_denied`: Der Benutzer ist nicht der Besitzer des Freigabeziels. Es wurde keine Freigabe angelegt.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Es wurde keine Freigabe angelegt.

Dabei ist Freigabe-ID die ID der neu angelegten Freigabe, Benutzer-Anzeigename der Anzeigename des Freigabeerstellers und Betroffener-Anzeigename der Anzeigename des Betroffenen. Der Schlüssel `share` ist nur vorhanden, wenn die Aktion erfolgreich war.
Schreibberechtigung hat den Wert `true`, falls die Freigabe Leseberechtigungen und Schreibberechtigungen einräumt, oder `false`, falls die Freigabe nur Leseberechtigungen einräumt.

## Operation DELETE /share/\<Freigabe-ID\>?user=\<Benutzer-ID\>
Löscht eine bestehende Freigabe.
Anfragetyp: leerer Anfragekörper
Antworttyp: `application/json`

Parameter:
 - Freigabe-ID: Die ID der zu löschenden Freigabe.
 - Benutzer-ID: Die ID des Benutzers, der die Aktion ausführt.

Antwortformat:
```  
{
	"status": "<Status>"
}
```

Dabei ist Status einer der folgenden Werte:
 - `ok`: Die Aktion wurde erfolgreich beendet.
 - `unauthorized`: Die Sitzung ist nicht berechtigt, im Namen des angegebenen Benutzers zu agieren.
 - `not_found`: Der Benutzer hat keine Berechtigung, die Freigabe einzusehen, oder die Freigabe existiert nicht. Die bestehende Freigabe wurde nicht gelöscht, falls sie existiert.
 - `permission_denied`: Der Benutzer ist nicht der Ersteller der Freigabe. Die bestehende Freigabe wurde nicht gelöscht.
 - `internal_error`: Bei der Verarbeitung ist ein Server- oder Datenbankfehler aufgetreten. Die bestehende Freigabe wurde nicht gelöscht.
