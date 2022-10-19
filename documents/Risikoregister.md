<table width="945">
    <tbody>
    <tr>
        <td width="75">
            <p><strong>RisikoID</strong></p>
        </td>
        <td width="274">
            <p><strong>Bedrohung</strong></p>
        </td>
        <td width="180">
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td width="123">
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td width="161">
            <p><strong>Risiko</strong></p>
        </td>
        <td width="132">
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td>
            <p>R1</p>
        </td>
        <td width="274">
            <p>Unbefugte ohne Benutzer in der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer
                Benutzer sehen.</p>
        </td>
        <td width="180">
            <p>Hoch</p>
        </td>
        <td width="123">
            <p>Sehr hoch </p>
        </td>
        <td width="161">
            <p>Hoch</p>
        </td>
        <td width="132">
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Beschreibung</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Unbefugte ohne Benutzer in der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer
                Benutzer sehen.<br/> <br/> Betrifft: A8, A9</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Alle Zugriffe auf die Anwendung m&uuml;ssen authentifiziert erfolgen.<br/> <br/> DSGVO schreibt Schutz
                der Daten gesetzlich vor.<br/> <br/> BSI CON.10.A1<br/> OWASP V1.2.3</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td width="161">
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td width="132">
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p>Benutzerverwaltung und Authentifizierung (Anmeldung) erzwingen vor Zugriff.</p>
            <p>&hellip;</p>
        </td>
        <td width="161">
            <p>Manueller Test<br/> Automatisierter Test<br/> Pentest<br/> [Design Review]</p>
            <p>Code Review (Manuell)</p>
            <p>[&hellip;]</p>
        </td>
        <td width="132">
            <p>T1<br/> T2<br/> T3<br/> [T4]<br/> T5</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table width="945">
    <tbody>
    <tr>
        <td width="75">
            <p><strong>RisikoID</strong></p>
        </td>
        <td width="274">
            <p><strong>Bedrohung</strong></p>
        </td>
        <td width="180">
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td width="123">
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td width="161">
            <p><strong>Risiko</strong></p>
        </td>
        <td width="132">
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td width="75">
            <p>&nbsp;R2</p>
        </td>
        <td width="274">
            <p>Benutzer der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer
                sehen.</p>
        </td>
        <td width="180">
            <p>Hoch</p>
        </td>
        <td width="123">
            <p>Sehr hoch<br/></p>
        </td>
        <td width="161">
            <p>Hoch</p>
        </td>
        <td width="132">
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Benutzer der Anwendung k&ouml;nnen Gesundheitsdaten oder pers&ouml;nliche Daten anderer Benutzer
                sehen.<br/> <br/> Betrifft: A8, A9</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Vor jedem Zugriff wird die Berechtigung des Benutzers gepr&uuml;ft. <br/> <br/> DSGVO schreibt Schutz der
                Daten gesetzlich vor.<br/> <br/> CON.10.A2</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td width="161">
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td width="132">
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p>Authentifizierung (Anmeldung) erzwingen vor Zugriff (siehe R1).<br/> <br/> Autorisierung
                (Berechtigunbgspr&uuml;fung) erzwingen vor Zugriff.</p>
        </td>
        <td width="161">
            <p>Manueller Test<br/> Automatisierter Test<br/> Pentest<br/> [Design Review]</p>
            <p>Code Review (manuell)</p>
            <p>[&hellip;]</p>
        </td>
        <td width="132">
            <p>T6<br/> T7<br/> T8<br/> [T9]<br/> T10</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table width="945">
    <tbody>
    <tr>
        <td width="75">
            <p><strong>RisikoID</strong></p>
        </td>
        <td width="274">
            <p><strong>Bedrohung</strong></p>
        </td>
        <td width="180">
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td width="123">
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td width="161">
            <p><strong>Risiko</strong></p>
        </td>
        <td width="132">
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td width="75">
            <p>&nbsp;R3</p>
        </td>
        <td width="274">
            <p>Sicherheit der Daten&uuml;bertragung</p>
        </td>
        <td width="180">
            <p>[Hoch]</p>
        </td>
        <td width="123">
            <p>[Sehr hoch]</p>
        </td>
        <td width="161">
            <p>[Hoch]</p>
        </td>
        <td width="132">
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Daten&uuml;bertragung zwischen Webbrowser und Webserver und zwischen Webserver/Webanwendung und DB-Server
                k&ouml;nnte abgeh&ouml;rt werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Alle Kommunikation/Daten&uuml;bertragung muss sicher (vertraulich, integrit&auml;tsgesch&uuml;tzt)
                erfolgen.<br/> <br/> DSGVO schreibt Schutz der Daten gesetzlich vor.<br/> <br/> CON.10.A14<br/> <br/>
                Betrifft: A8, A9, A10, A13, A18</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td width="161">
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td width="132">
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p>&Uuml;berall HTTPS (http &uuml;ber TLS) einsetzen.</p>
        </td>
        <td width="161">
            <p>Manueller Test<br/> Automatisierter Test]<br/> Pentest<br/> Code Review (SAST)</p>
            <p>[&hellip;]</p>
        </td>
        <td width="132">
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table width="945">
    <tbody>
    <tr>
        <td width="75">
            <p><strong>RisikoID</strong></p>
        </td>
        <td width="274">
            <p><strong>Bedrohung</strong></p>
        </td>
        <td width="180">
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td width="123">
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td width="161">
            <p><strong>Risiko</strong></p>
        </td>
        <td width="132">
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td width="75">
            <p>&nbsp;R4</p>
        </td>
        <td width="274">
            <p>Datenmanipulation</p>
        </td>
        <td width="180">
            <p>Hoch</p>
        </td>
        <td width="123">
            <p>Sehr hoch</p>
        </td>
        <td width="161">
            <p>Hoch</p>
        </td>
        <td width="132">
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Unbefugte k&ouml;nnten Daten (A8, A9) in der DB lesen oder ver&auml;ndern.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Ein unbefugter Zugriff lesend oder schreibend muss verhindert werden.</p>
            <p><br/> DSGVO schreibt Schutz der Daten gesetzlich vor.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td width="161">
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td width="132">
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p>Daten&uuml;bertragung sch&uuml;tzen (siehe R3).<br/> <br/> Eingabevalidierung (Webanwendung),
                Zugriffskontrolle (Berechtigungspr&uuml;fung) in der Webanwendung + DB-Server.<br/> <br/>
                Kryptografische Verschl&uuml;sselung mit Integrit&auml;tsschutz anbringen. (optional)</p>
        </td>
        <td width="161">
            <p>Manueller Test<br/> [Automatisierter Test]<br/> [Pentest]<br/> [Design Review]</p>
            <p>Code Review (SAST)</p>
            <p>[&hellip;]</p>
        </td>
        <td width="132">
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>

<table width="945">
    <tbody>
    <tr>
        <td width="75">
            <p><strong>RisikoID</strong></p>
        </td>
        <td width="274">
            <p><strong>Bedrohung</strong></p>
        </td>
        <td width="180">
            <p><strong>Eintrittswahrscheinlichkeit</strong></p>
        </td>
        <td width="123">
            <p><strong>Auswirkungen</strong></p>
        </td>
        <td width="161">
            <p><strong>Risiko</strong></p>
        </td>
        <td width="132">
            <p><strong>Behandlung</strong></p>
        </td>
    </tr>
    <tr>
        <td width="75">
            <p>&nbsp;R5</p>
        </td>
        <td width="274">
            <p>Webanwendungs-Schwachstellen</p>
        </td>
        <td width="180">
            <p>Hoch</p>
        </td>
        <td width="123">
            <p>Hoch</p>
        </td>
        <td width="161">
            <p>Hoch</p>
        </td>
        <td width="132">
            <p>Reduzieren</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Beschreibung</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>Es verbleiben Web-typische Schwachstellen in der Anwendung die nicht entdeckt werden.</p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p><strong>Anforderungen</strong></p>
        </td>
    </tr>
    <tr>
        <td colspan="6" width="945">
            <p>&hellip;.</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p><strong>Ma&szlig;nahmen</strong></p>
        </td>
        <td width="161">
            <p>&Uuml;berpr&uuml;fung</p>
        </td>
        <td width="132">
            <p>TestID</p>
        </td>
    </tr>
    <tr>
        <td colspan="4" width="652">
            <p>Sicherheitsrelevante Header setzen (z.B. Content-Security-Policy) und http-Methoden verwenden.</p>
        </td>
        <td width="161">
            <p>[Manueller Test]<br/> [Automatisierter Test]<br/> [Pentest]<br/> [Design Review]<br/> Code Review (SAST)
            <br/>[&hellip;]</p>
        </td>
        <td width="132">
            <p>[TId]</p>
        </td>
    </tr>
    </tbody>
</table>
<p>&nbsp;</p>
