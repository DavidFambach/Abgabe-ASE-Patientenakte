# Testkonzept

## Statische Codeanalyse
**Werkzeuge:**
- SonarLint: Codesmell
- CodeQL: Schwachstellen

In unserer Entwicklungsumgebung setzten wir ein SonarLint-Plugin ein, um die Entwicklung von qualitativem Code zu unterstützen. SonarLint macht eine regelbasierte statische Codeanalyse lokal in der Entwicklungsumgebung. Damit sollen viele Probleme in Echtzeit ermittelt und gleichzeitig "Quick Fixes" angeboten werden.

Mithilfe von GitHub Actions wird der Code nach einem Push über eine Pipeline mithilfe von CodeQL auf Schwachstellen überprüft. Dadurch werden potenzielle Sicherheits- und Zuverlässigkeitsprobleme innerhalb der Codebasis identifiziert. CodeQL ist wie SonarLint ein statisches, regelbasiertes (bei CodeQL heißt es "querie") Analysetool.

## Codereview
Sobald die statische Codeanalyse abgeschlossen ist, überprüft der Code-Reviewer die Ergebnisse und bestimmt, ob eines der identifizierten Probleme behoben werden muss. Der Codeprüfer kann auch zusätzliche Vorschläge zur Verbesserung der Codebasis machen.

Der Code-Reviewer bespricht dann die Ergebnisse mit dem Entwicklungsteam und gibt Empfehlungen für erforderliche Änderungen. Dies kann Refactoring, Umschreiben von Code oder Ändern der Architektur der Codebasis umfassen. Das Entwicklungsteam wird dann die empfohlenen Änderungen implementieren.

Sobald die Änderungen implementiert wurden, wird die Codebasis erneut gescannt und alle verbleibenden Probleme müssen behoben werden. Der Codeprüfer überprüft dann die Ergebnisse und bestimmt, ob weitere Änderungen vorgenommen werden müssen. Der Vorgang wird wiederholt, bis alle potenziellen Probleme behoben wurden.

## Komponententests
**Werkzeuge:**
- Django REST Framework Testing

Die API-Schnittstellen werden, wie in der Architekturentscheidung API-Testwerkzeuge ermittelt, mithilfe des Django REST Frameworks getestet. Die dynamischen Tests werden mit einer Continuous Integration (CI) Pipeline in GitHub Actions ausgeführt. Dadurch ist zu jedem Stand ersichtlich, ob die REST-Schnittstellen das in der Dokumentation festgehaltene verhalten aufweisen. Sollte dies nicht der Fall sein, können die Codeänderungen, die zum fehlerhaften Verhalten geführt haben, sofort in einem Codereview untersucht und ggf. der Code korrigiert oder die Dokumentation angepasst werden.

## Integrationstests (hypothetisch)
**Werkzeuge:**
- Django REST Framework Testing
- Manuell

Automatisierte Integrationstests werden, wie die Komponententests, über das Django REST Framework verwirklicht. Der einzige fall in dem dies jedoch sinnvoll ist, ist beim Löschen eines Benutzers. Dies ist der einzige fall bei dem mehrere dienste miteinander (wenn auch nicht direkt) Kommunizieren.

Bei den übrigen Integrationstests sollte vor allem aufgrund des Zusammenspiels mit dem Frontend ein manueller Test durchgeführt werden. Von dort aus kann im Fehlerfall, über direkte HTTP-Requests, auch das Frontend übergangen und direkt mit den Endpunkten kommuniziert werden.
