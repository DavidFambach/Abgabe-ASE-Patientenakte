# Akteure

## 1 Patient

### 1.1 Kurzbeschreibung
Patienten laden über das Internet Dateien hoch und verwalten diese über die Anwendung. Sie können einzelne Dateien für den Zugriff durch ausgewählte Ärzte und andere Patienten freigeben. Patienten können sich selbstständig registrieren.

### 1.2 Eigenschaften
|                                |                      |
| ------------------------------ | -------------------- |
| Zugriffstyp                    | Webzugriff über HTTP |
| Anzahl gleichzeitiger Benutzer | vgl. NF1             |
| Datendurchsatz                 | vgl. NF1, RL1        |

### 1.3 Beziehungen
- zu Patienten: Geben Dateien frei
- zu Ärzten: Geben Dateien frei


## 2 Arzt

### 2.1 Kurzbeschreibung
Ärzte können über das Internet für Sie freigegebene Dateien einsehen und herunterladen. Ärzte können sich selbstständig registrieren.

### 2.2 Eigenschaften
|                                |                      |
| ------------------------------ | -------------------- |
| Zugriffstyp                    | Webzugriff über HTTP |
| Anzahl gleichzeitiger Benutzer | vgl. NF1             |
| Datendurchsatz                 | vgl. NF1, RL1        |

### 2.3 Beziehungen
- zu Patienten: Erhalten Zugriff auf Dateien


## 3 Anwendungsadministrator

### 3.1 Kurzbeschreibung
Anwendungsadministratoren sind privilegierte Benutzer, die den Dateiverwaltungsdienst und Autorisierungsdienst konfigurieren und warten.

### 3.2 Eigenschaften
|                                |                                                                                 |
| ------------------------------ |---------------------------------------------------------------------------------|
| Zugriffstyp                    | Systemzugriff auf den Dateiverwaltungsdienst und Autorisierungsdienst über SSH |
| Anzahl gleichzeitiger Benutzer | 1                                                                               |
| Datendurchsatz                 | vernachlässigbar                                                                |

### 3.3 Beziehungen
keine


## 4 Datenbankadministrator

### 4.1 Kurzbeschreibung
Datenbankadministratoren sind privilegierte Benutzer, die den Datenbankserver konfigurieren und warten.

### 4.2 Eigenschaften
|                                |                                                |
| ------------------------------ | ---------------------------------------------- |
| Zugriffstyp                    | Systemzugriff auf den Datenbankserver über SSH |
| Anzahl gleichzeitiger Benutzer | 1                                              |
| Datendurchsatz                 | vernachlässigbar                               |

### 4.3 Beziehungen
keine


## 5 Webserveradministrator

### 5.1 Kurzbeschreibung
Webserveradministrator sind privilegierte Benutzer, die den Webserver konfigurieren und warten.

### 5.2 Eigenschaften
|                                |                                          |
| ------------------------------ | ---------------------------------------- |
| Zugriffstyp                    | Systemzugriff auf den Webserver über SSH |
| Anzahl gleichzeitiger Benutzer | 1                                        |
| Datendurchsatz                 | vernachlässigbar                         |

### 5.3 Beziehungen
keine
