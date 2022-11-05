# Beziehungen

## 1 Akteur: Patient via Webbrowser
- Eingabe 1:
	- Suchanfragen, Einzeldateien, Änderungen an Einstellungen
	- Synchron via HTTP/TLS, maximal 10 gleichzeitige Benutzer (vgl. NF1), maximale Größe einer Einzeldatei 128 MiB (vgl. R2), verfügbar 24/7/52 zu 99 % (vgl. NF9)
- Ausgabe 1:
	- Webseite, Dateilisten, Dateien
	- Synchron via HTTP/TLS

## 2 Akteur: Arzt via Webbrowser
- Eingabe 2:
	- Suchanfragen, Einzeldateien, Änderungen an Einstellungen
	- Synchron via HTTP/TLS, maximal 10 gleichzeitige Benutzer (vgl. NF1), maximale Größe einer Einzeldatei 128 MiB (vgl. R2), verfügbar 24/7/52 zu 99 % (vgl. NF9)
- Ausgabe 2:
	- Webseite, Dateilisten, Dateien
	- Synchron via HTTP/TLS

## 3 Akteur: Plattformadministrator via Webbrowser
- Eingabe 3:
	- Suchanfragen
	- Synchron via HTTP/TLS, vernachlässigbare Sitzungszahl und Datendurchsatz, keine definierte Anforderung an die Verfügbarkeit
- Ausgabe 3:
	- Webseite, Statistiken über Benutzer und Dateien
	- Synchron via HTTP/TLS

## 4 Akteur: Externer IDP
- Eingabe 4:
	- Bestätigungen und Ablehungen für Anmeldeversuche
	- Synchron via HTTP/TLS
- Ausgabe 4:
	- Benutzerbezeichner von Benutzern, die den IDP für die Anmeldung verwenden
	- Synchron via HTTP/TLS, keine definierte Verfügbarkeitsgarantie (Stand 16.10.2022)

## 5 Akteur: Plattform- / Anwendung- / Datenbankadminstrator via Shell
- Eingabe 5:
	- Beliebige Systembefehle zur Konfiguration und Wartung des Systems
	- Synchron via SSH, vernachlässigbare Sitzungszahl und Datendurchsatz, keine definierte Anforderung an die Verfügbarkeit
- Ausgabe 5:
	- Ausgaben beliebiger Systembefehle
	- Synchron via SSH
