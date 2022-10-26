# Akteure

## 1 Patient

### 1.1 Kurzbeschreibung
Patienten laden über das Internet Dateien hoch und verwalten diese über die Anwendung. Sie können einzelne Dateien für den Zugriff durch ausgewählte Ärzte und andere Patienten freigeben. Patienten können sich selbstständig registrieren.

### 1.2 Eigenschaften
|                                |                      |
| ------------------------------ | -------------------- |
| Zugriffstyp                    | Webzugriff über HTTP |
| Anzahl gleichzeitiger Benutzer | vgl. NF1             |
| Datendurchsatz                 | vgl. NF1, R1         |

### 1.3 Beziehungen
- zu Patienten: Geben Dateien frei
- zu Ärzten: Geben Dateien frei


## 2 Arzt

### 1.1 Kurzbeschreibung
Ärzte können über das Internet für Sie freigegebene Dateien einsehen und herunterladen. Ärzte können sich selbstständig registrieren.

### 1.2 Eigenschaften
|                                |                      |
| ------------------------------ | -------------------- |
| Zugriffstyp                    | Webzugriff über HTTP |
| Anzahl gleichzeitiger Benutzer | vgl. NF1             |
| Datendurchsatz                 | vgl. NF1, R1         |

### 1.3 Beziehungen
- zu Patienten: Erhalten Zugriff auf Dateien


## 3 Plattformadministrator

### 1.1 Kurzbeschreibung
Plattformadministratoren sind privilegierte Benutzer, die die Gesamtanwendung verwalten, indem sie Statistiken über die Anwendung, insbesondere Benutzerzahl und Speicherverbrauch einsehen. Sie sind in der Lage, beliebige Benutzer und Dateien zu löschen. Sie sind allerdings nicht in der Lage, die über die Anwendung geteilten Dateien einzusehen oder herunterzuladen.

### 1.2 Eigenschaften
|                                |                      |
| ------------------------------ | -------------------- |
| Zugriffstyp                    | Webzugriff über HTTP |
| Anzahl gleichzeitiger Benutzer | 1                    |
| Datendurchsatz                 | vernachlässigbar     |

### 1.3 Beziehungen
keine


## 4 Anwendungsadministrator

### 1.1 Kurzbeschreibung
Anwendungsadministratoren sind privilegierte Benutzer, die den Dateiablagedienst konfigurieren und warten.

### 1.2 Eigenschaften
|                                |                                                  |
| ------------------------------ | ------------------------------------------------ |
| Zugriffstyp                    | Systemzugriff auf den Dateiablagedienst über SSH |
| Anzahl gleichzeitiger Benutzer | 1                                                |
| Datendurchsatz                 | vernachlässigbar                                 |

### 1.3 Beziehungen
keine


## 5 Datenbankadministrator

### 1.1 Kurzbeschreibung
Datenbankadministratoren sind privilegierte Benutzer, die den Datenbankserver konfigurieren und warten.

### 1.2 Eigenschaften
|                                |                                                |
| ------------------------------ | ---------------------------------------------- |
| Zugriffstyp                    | Systemzugriff auf den Datenbankserver über SSH |
| Anzahl gleichzeitiger Benutzer | 1                                              |
| Datendurchsatz                 | vernachlässigbar                               |

### 1.3 Beziehungen
keine


## 6 Webserveradministrator

### 1.1 Kurzbeschreibung
Webserveradministrator sind privilegierte Benutzer, die den Webserver konfigurieren und warten.

### 1.2 Eigenschaften
|                                |                                          |
| ------------------------------ | ---------------------------------------- |
| Zugriffstyp                    | Systemzugriff auf den Webserver über SSH |
| Anzahl gleichzeitiger Benutzer | 1                                        |
| Datendurchsatz                 | vernachlässigbar                         |

### 1.3 Beziehungen
keine
