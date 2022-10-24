<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>R1</p>
        </td>
        <td>
            <p>Unbefugte ohne Benutzer in der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer
                Benutzer sehen.</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch </p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Beschreibung</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Unbefugte ohne Benutzer in der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer
                Benutzer sehen.<br/> <br/> Betrifft: A8, A9</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Alle Zugriffe auf die Anwendung m&uuml;ssen authentifiziert erfolgen.<br/> <br/> DSGVO schreibt Schutz
                der Daten gesetzlich vor.<br/> <br/> BSI CON.10.A1<br/> OWASP V1.2.3</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Benutzerverwaltung und Authentifizierung (Anmeldung) erzwingen vor Zugriff.</p>
            <p>&hellip;</p>
        </td>
        <td>
            <p>Manueller Test<br/> Automatisierter Test<br/> Pentest<br/> [Design Review]</p>
            <p>Code Review (Manuell)</p>
            <p>[&hellip;]</p>
        </td>
        <td>
            <p>T1<br/> T2<br/> T3<br/> [T4]<br/> T5</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R2</p>
        </td>
        <td>
            <p>Benutzer der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer
                sehen.</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch<br/></p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Benutzer der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer
                sehen.<br/> <br/> Betrifft: A8, A9</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Vor jedem Zugriff wird die Berechtigung des Benutzers gepr&uuml;ft. <br/> <br/> DSGVO schreibt Schutz der
                Daten gesetzlich vor.<br/> <br/> CON.10.A2</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Authentifizierung (Anmeldung) erzwingen vor Zugriff (siehe R1).<br/> <br/> Autorisierung
                (Berechtigunbgspr&uuml;fung) erzwingen vor Zugriff.</p>
        </td>
        <td>
            <p>Manueller Test<br/> Automatisierter Test<br/> Pentest<br/> [Design Review]</p>
            <p>Code Review (manuell)</p>
            <p>[&hellip;]</p>
        </td>
        <td>
            <p>T6<br/> T7<br/> T8<br/> [T9]<br/> T10</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R3</p>
        </td>
        <td>
            <p>Sicherheit der Daten&uuml;bertragung</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Daten&uuml;bertragung zwischen Webbrowser und Webserver und zwischen Webserver/Webanwendung und DB-Server
                k&ouml;nnte abgeh&ouml;rt werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Alle Kommunikation/Daten&uuml;bertragung muss sicher (vertraulich, integrit&auml;tsgesch&uuml;tzt)
                erfolgen.<br/> <br/> DSGVO schreibt Schutz der Daten gesetzlich vor.<br/> <br/> CON.10.A14<br/> <br/>
                Betrifft: A8, A9, A10, A13, A18</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>&Uuml;berall HTTPS (http &uuml;ber TLS) einsetzen.</p>
        </td>
        <td>
            <p>Manueller Test<br/> Automatisierter Test]<br/> Pentest<br/> Code Review (SAST)</p>
            <p>[&hellip;]</p>
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R4</p>
        </td>
        <td>
            <p>Datenmanipulation</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Unbefugte k&ouml;nnten Daten (A8, A9) in der DB lesen oder ver&auml;ndern.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Ein unbefugter Zugriff lesend oder schreibend muss verhindert werden.</p>
            <p><br/> DSGVO schreibt Schutz der Daten gesetzlich vor.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Daten&uuml;bertragung sch&uuml;tzen (siehe R3).<br/> <br/> Eingabevalidierung (Webanwendung),
                Zugriffskontrolle (Berechtigungspr&uuml;fung) in der Webanwendung + DB-Server.<br/> <br/>
                Kryptografische Verschl&uuml;sselung mit Integrit&auml;tsschutz anbringen. (optional)</p>
        </td>
        <td>
            <p>Manueller Test<br/> [Automatisierter Test]<br/> [Pentest]<br/> [Design Review]</p>
            <p>Code Review (SAST)</p>
            <p>[&hellip;]</p>
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R5</p>
        </td>
        <td>
            <p>Webanwendungs-Schwachstellen</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Es verbleiben Web-typische Schwachstellen in der Anwendung die nicht entdeckt werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>&hellip;.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Sicherheitsrelevante Header setzen (z.B. Content-Security-Policy) und http-Methoden verwenden.</p>
        </td>
        <td>
            <p>[Manueller Test]<br/> [Automatisierter Test]<br/> [Pentest]<br/> [Design Review]<br/> Code Review (SAST)
            <br/>[&hellip;]</p>
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahr-<br>scheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R6</p>
        </td>
        <td>
            <p>Benutzer verwenden unsichere Passwörter</p>
        </td>
        <td>
            <p>Sehr hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Benutzer wählen aus Bequemlichkeit, Unwissenheit oder anderen Gründen unsichere Passwörter für die Authentifizierung.
                <br>Dadurch werden Sicherheitsmechanismen, die auf der Integrität des Benutzerkontos aufbauen, unwirksam.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Das Erraten des Kennworts mittels Bruteforce oder durch Nutzung von Wörterbüchern und Rainbowtables soll unwirtschaftlich sein.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Single-Sign-On über einen externen IDP ermöglichen. (optional)</p>
            <p>Das Passwort muss gewisse Vorgaben erfüllen um verwendet werden zu können.</p>
        </td>
        <td>
            Automatisierter Test<br/> 
            Pentest<br/> 
            Design Review
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

[comment]: <> (TODO: Einfügung der Passwortrichtlinien?)


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahr-<br>scheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R7</p>
        </td>
        <td>
            <p>Benutzer vergessen Passwörter</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Die aus hohen Anforderungen (siehe R6) an das Passwort ist dieses nicht sehr einprägsam. Hinzu kommt, dass die Gesundheitsakte von den meisten Benutzern nicht regelmäßig sondern in größeren Zeitabständen verwendet wirt.</p>
            <p>Infolgedessen werden viele Benutzer ihr Zugangsdaten vergessen und somit ihre verschlüsselten Daten verlieren (vgl. Konzept "Schützen von Data-at-rest").</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Die Benutzer auf dieses Risiko aufmerksam machen und Möglichkeiten die Vermeidung nahelegen.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Bei der Erstellung des Kontos darauf hinweisen, dass es sich bei der Anwendung nicht um einen Onlinespeicher, sondern um eine Datenaustauschplattform handelt. Das hat zur Folge, dass die Verfügbarkeit der Daten der Vertraulichkeit und der Integrität der Daten untergeordnet ist.</p>
            <p>Bei der Erstellung des Kontos darauf hinweisen, dass in der Anwendung zum Schutz der Vertraulichkeit die Daten Ende-zu-Ende verschlüsselt werden. Das hat zur Folge, dass beim Zurücksetzen des Anmeldekennworts sämtliche gespeicherte Daten gelöscht werden.</p>
            <p>Bei der Erstellung des Kontos darauf hinweisen, dass zum Verwalten von komplexen Passwörtern ein Passwortmanager eine große Hilfe ist.</p>
        </td>
        <td>
            Manueller Test<br/> 
            Code Review
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahr-<br>scheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R8</p>
        </td>
        <td>
            <p>Überlastung der Speicherressourcen durch zu viele (Fake-)Dokumente.</p>
        </td>
        <td>
            <p>Hoch</p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>?</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p></p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p></p>
        </td>
        <td>
            <p></p>
        </td>
        <td>
            <p></p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R9</p>
        </td>
        <td>
            <p>Benutzer der Anwendung laden b&ouml;sartige Dateien hoch.</p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Benutzer der Anwendung laden b&ouml;sartige Dateien hoch.<br>
            Diese k&ouml;nnten dann von anderen Benutzern heruntergeladen und ge&ouml;ffnet werden und dadurch ihr System infizieren.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Das Hochladen einer solchen Datei soll erschwert und wenn m&ouml;glich verhindert werden. <br>
            Benutzer sollten vor dem Ausführen / beim Herunterladen einer Datei vor Risiken gewarnt werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>Nur Dateien mit freigegebenen Dateiendungen d&uuml;rfen hochgeladen werden.<br>
                Benutzer werden beim Herunterladen vor m&ouml;gliche Risiken gewarnt
            </p>
        </td>
        <td>
            <p>Manueller Test<br/> Automatisierter Test</p>
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R10</p>
        </td>
        <td>
            <p>Unbefugte sehen geheime Konfigurationsparameter ein</p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Niedrig</p>
        </td>
        <td>
            <p>Reduzieren/Akzeptieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Unbefugte Prozesse oder Benutzer können geheime Konfigurationsparameter ein, insbesondere kryptografische Schlüssel, die von einer Anwendungskomponente benötigt, zum Beispiel zum Erbringen eines Identitätsnachweises.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Geheime Konfigurationsparameter werden vertraulich gespeichert<br>
				- OWASP ASVS V1.6.2 wird explizit nicht eingesetzt (vgl. Konzept "Schützen von konfigurierten Geheimnissen produktiver Systeme")<br>
				Betrifft: A4, A6
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>- Ausgeben einer Warnung an den Administrator, falls für geheime Konfigurationsparameter im Dateisystem ungünstige Zugriffsrechte gesetzt sind. Diese Maßnahme ist sehr einfach umsetzbar, ermöglicht aber nur die Erkennung eines einzelnen, speziellen Szenarios und reduziert damit formell das bezeichnete Risiko. Weil dies aber die einzige Maßnahme ist, wäre es irreführend, die Risikobehandlung als kommentarlos als Reduzieren zu bezeichnen, weil das nur unerheblich unter dem Ursprungsrisiko liegende Restrisiko de facto akzeptiert wird.</p>
        </td>
        <td>
            <p>- Manueller Test</p>
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R11</p>
        </td>
        <td>
            <p>Privilegierte Benutzer sehen Gesundheitsdaten anderer Benutzer ein</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>Privilegierte Benutzer können Gesundheitsdaten anderer Benutzer einsehen. Dieses Risiko unterscheidet sich von R1 dahingehend, dass der Benutzer, der unbefugt Daten einsehen kann, berechtigterweise erweiterte Rechte auf Systemen der Anwendung hat.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- Maßnahmen, die die Möglichkeiten priveligierter Benutzer beschränken, Vertraulichkeit und Integrität gespeicherter Gesundheitsdaten zu verletzen, und deren Aufwand ihren Nutzen nicht unangemessen übersteigt, werden implementiert.<br>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br>
				Betrifft: A8<br>
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>
				- Einsatz von Ende-zu-Ende-Verschlüsselung für Benutzerdaten mittels asymmetrischer Kryptografie (vgl. Konzept "Schützen von Data-at-rest")<br>
				- Maßnahmen gemäß R1
            </p>
        </td>
        <td>
            <p>
				- Manueller Test<br>
				- Design Review<br>
				- Code Review
			</p>
        </td>
        <td>
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>


<table>
    <tbody>
    <tr>
        <td>
            <p><strong>RisikoID</strong></p>
        </td>
        <td>
            <p><strong>Bedrohung</strong></p>
        </td>
        <td>
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td>
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td>
            <p><strong>Risiko</strong></p>
        </td>
        <td>
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>&nbsp;R12</p>
        </td>
        <td>
            <p>Privilegierte Benutzer sehen Gesundheitsdaten anderer Benutzer ein</p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Hoch<br/></p>
        </td>
        <td>
            <p>Mittel</p>
        </td>
        <td>
            <p>Akzeptieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				Privilegierte Benutzer können personenbezogenen Daten anderer Benutzer einsehen. Dieses Risiko unterscheidet sich von R1 dahingehend, dass der Benutzer, der unbefugt Daten einsehen kann, berechtigterweise erweiterte Rechte auf Systemen der Anwendung hat.<br>
				Für priveligierte Benutzer, die aus geschäftlichen Gründen auf die oder eine Telmenge der gespeicherten personenbezogenen Daten zugreifen müssen, besteht die Möglichkeit, dass dieser Zugang missbraucht wird. Aufgrund der Datenminimierung nach DSGVO ist die Menge der vorhandenen und damit zugreifbaren Daten bereits minimal. Das Ergreifen weiterer technischer Maßnahmen gegen einen Missbrauch des Zugangs wäre risikobasiert nicht angemessen. Stattdessen sollten für den Betrieb der Anwendung gegebenenfalls geeignete organisatorische Maßnahmen implementiert werden, die dieses Risiko auf ein akzeptables Maß reduzieren (NDO).
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6">
            <p>
				- DSGVO schreibt Schutz der Daten gesetzlich vor.<br>
				Betrifft: A9
			</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td>
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td>
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4">
            <p>n/a</p>
        </td>
        <td>
            <p>n/a</p>
        </td>
        <td>
            <p>n/a</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>
