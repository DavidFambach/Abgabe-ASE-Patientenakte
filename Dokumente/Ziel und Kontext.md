# Ziel und Kontext
Ziel ist die Bereitstellung einer Webanwendung, die es Patienten ermöglicht, Gesundheitsdaten zu verwalten und mit Ärzten und anderen Personen zu teilen, also lesenden Zugriff einzuräumen. Dadurch wird sichergestellt, dass Patienten und Ärzten stets aktuelle und vollständige Unterlagen zur Verfügung stehen. Ein besonderer Fokus liegt auf dem Schutz der Vertraulichkeit und Integrität dieser Daten.

# Regulatorische Vorschriften
Für die Entwicklung und den Betrieb einer solchen Anwendung sind verschiedene deutsche und europäische Vorschriften von Bedeutung. Im folgenden werden einige Implikationen ausgewählter bestehender und zukünftiger Vorschriften für den Entwicklungsprozess einer solchen Anwendung, die Anwendung selbst und den Betrieb derselben untersucht.
Die europäische Datenschutz-Grundverordnung (Verordnung EU 2016/679) enthält Bestimmungen zur Verarbeitung personenbezogener Daten mit dem Ziel die Rechte natürlicher Personen im Bezug auf diese Daten zu stärken. Weil sich die DSGVO nur auf die Verarbeitung personenbezogener Daten bezieht, betrifft sie nur den Betrieb der Anwendung direkt. Allerdings erfordert der DSGVO-konforme Betrieb einer Anwendung zur Verwaltung von Gesundheitsdaten notwendigerweise auch bestimmte Eigenschaften der Anwendung selbst, sodass die meisten Vorschriften der DSGVO sowohl als Anforderung an die Anwendung als auch an deren Betrieb verstanden werden müssen. Die DSGVO fordert insbesondere, dass
- weil es sich bei den verarbeiteten personenbezogenen Daten um Gesundheitsdaten handelt, eine ausdrückliche Einwilligung der betroffenen Person vor der Verarbeitung eingeholt wird (Art. 9 Abs. 1, 2 DSGVO).
- Rahmenbedingungen für die Einwilligung eingehalten werden (Art. 7, 8 DSGVO).
- Informationspflichten eingehalten werden können (Art. 13, 15 DSGVO).
- betroffenen Personen ermöglicht wird, bestimmte Betroffenenrechte auszuüben (Art. 16-20 DSGVO).
- risikobasiert technische und organisatorische Maßnahmen zum Schutz der Verarbeitung personenbezogener Daten sowie deren Integrität und Vertraulichkeit (Art. 5 Abs. 1 lit. f DSGVO, Art. 24 Abs. 1 DSGVO, Art. 32 DSGVO).
- Voreinstellungen der Anwendung datenschutzfreundlich sind (Art. 25 Abs. 1, 2 DSGVO).
- keine personenbezogenen Daten erfasst werden, die keinem eindeutigen Zweck dienen oder nicht länger erforderlich sind oder deren Zweck über das für die Anwendung notwendige Maß hinausgeht (Art. 5 Abs. 1 lit. b, c, e).
Die vorgenannten Forderungen konzentrieren sich auf Aspekte, die bereits bei der Entwicklung der Anwendung zu berücksichtigen sind. Für den Betrieb der Anwendung sind weitere Aspekte relevant, unter Anderem die Benennung von Kontaktpersonen und einem Datenschutzbeauftragten oder die Information von Aufsichtsbehörden bei Datenschutzvorfällen.
Weil für die Verarbeitung von Gesundheitsdaten bereits eine Einwilligung des Betroffenen eingeholt werden muss, wird auch für personenbezogene Daten, die nicht unter Art. 9 DSGVO fallen, eine Einwilligung als Rechtsgrund der Verarbeitung eingesetzt.
Darüber hinaus ist ein angemessener Schutz von Vertraulichkeit, Integrität und Verfügbarkeit sensibler Daten für Entwickler und Betreiber einer Anwendung, deren Zweck der Umgang mit diesen Daten ist, von erheblicher Bedeutung, weil Datenpannen insbesondere in diesem Bereich erhebliche Rufschädigungen herbeiführen können, die unter Umständen auch geschäftsgefährdend sein können. Je nach Rechtsform eines Unternehmens existieren verschiedene Vorschriften, die die Geschäftsführung verpflichten, auf die Erkennung oder Behebung dieser Probleme hinzuwirken (vgl. bspw. § 91 Abs. 2 AktG).
In der Zukunft können zusätzliche Vorschriften relevant werden, beispielsweise durch den vorgeschlagenen EU Cyber Resillience Act, der Sicherheitsvorgaben für Produkte mit digitalen Komponenten macht. Für EHR-Systeme nach der vorgeschlagenen European Health Data Space Regulation, was unter anderem Lösungen zur Verwaltung von Gesundheitsdaten umfasst, wird Konformität zu einem Anforderungskatalog gefordert (vgl. Art. 24 Abs. 4 Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022). Dieser Anforderungskatalog betrifft sowohl den Entwicklungsprozess der Anwendung als auch die Anwendung selbst als auch den Betrieb der Anwendung. Er fordert insbesondere, dass
- der Entwicklungsprozess eine Bedrohungsanalyse umfasst (Art. 10 Abs. 3 Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
- der Entwicklungsprozess in Anbetracht bestehender Risiken angemessen ist (Anhang 1 Abs. 1 Nr. 1 Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
- der Entwicklungsprozess zur Behandlung von Schwachstellen fähig ist (Anhang 1 Abs. 2 Nr. 2 Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
- der Entwicklungsprozess angemessene Sicherheitstests vorsieht (Anhang 1 Abs. 2 Nr. 3 Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
- für den Entwicklungsprozess und den Betrieb der Anwendung eine Minimierung der Angriffsoberfläche und eine Minimierung der Auswirkungen von Sicherheitsvorfällen (Anhang 1 Abs. 1 Nr. 3 lit. h, i Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
- für die Anwendung eine Freiheit von Schwachstellen zur Auslieferung (Anhang 1 Abs. 1 Nr. 2 Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
- für die Anwendung
	- sichere Standardeinstellungen,
	- einen Schutz gegen nicht autorisierten Zugriff,
	- einen Schutz der Vertraulichkeit von verarbeiteten Daten, unabhängig davon, ob sie personenbezogen sind, während der Speicherung und Übertragung,
	- einen Schutz der Integrität dieser Daten,
	- eine Datenminimierung für personenbezogene und nicht personenbezogene Daten,
	- einen Schutz der Verfügbarkeit der Kernfunktionen sowie einen Schutz gegen DoS-Angriffe,
	- eine Minimierung der von dem Produkt für andere Dienste ausgehenden Gefahren,
	- ein Logging von sicherheitsrelevanten Ereignissen und
	- die Fähigkeit zu Sicherheitsaktualisierungen (Anhang 1 Abs. 1 Nr. 3 lit. a-g, j, k Proposed EU Cyber Resilience Act i. d. F. v. 15. September 2022).
Diese Aspekte sind derzeit noch nicht verbindlich, aber werden in der Zukunft wahrscheinlich mindestens in ähnlicher Form vom Gesetzgeber eingefordert werden. Neben den genannten rechtlichen Vorgaben gibt es weitere Gründe, Sicherheitsaspekte bei der Entwicklung verstärkt zu berücksitigen, unter Anderem die oben genannte Gefahr der Rufschädigung bei Pannen, aber auch eine Verringerung der notwendig werdenden Korrekturmaßnahmen können sowohl für Softwarehersteller als auch -betreiber eine Aufwands- und damit eine Kostenreduktion darstellen.
