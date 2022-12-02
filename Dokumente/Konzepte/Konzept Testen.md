# Testkonzept

## Statische Code Analyse
**Werkzeuge:**
- SonarLint: Codesmell
- CodeQL: Schwachstellen

In unserer Entwicklungsumgebung setzten wir ein SonarLint-Plugin ein, um die Entwicklung von qualitativem Code zu unterstützen. SonarLint macht eine regelbasierte statische Codeanalyse lokal in der Entwicklungsumgebung. Damit sollen viele Probleme in Echtzeit ermittelt und gleichzeitig "Quick Fixes" angeboten werden.

Mithilfe von GitHub Actions wird der Code nach einem Push über eine Pipeline mithilfe von CodeQL auf Schwachstellen überprüft. CodeQL ist wie SonarLint ein statishes regelbasiertes (bei CodeQL heist es "querie") Analysetool.

## Komponenten Tests
**Werkzeuge:**
- Django REST Framework Testing

Die API Schnittstellen werden, wie in der Architekturentscheindung API Testwerkzeuge ermittelt, mithilfe des Django REST Frameworks getestet. Die dynamischen Tests werden mit einer Continuous Integration (CI) pipline in GitHub Actions ausgeführt.

## Integration Tests \**hypothetisch**
