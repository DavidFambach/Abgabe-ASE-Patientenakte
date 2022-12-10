# Umsetzungskonzept gegen DDoS-Angriffe

|                                                                       |
|-----------------------------------------------------------------------|
| Das System soll hinreichend gegen DDoS / DoS Anfriffe geschützt sein. |

### Risiko
#### Eintrittswahrscheinlichkeit
Unsere Anwendung ist im medizinischen Kontext angesiedelt. Aus diesem Grund muss damit gerechnet werden, dass sie von Aktivisten mutwillig sabotiert wird und von Whitehats zum Gemeinwohl getestet wird. Eine der üblichsten Methoden, dies zu tun, ist, die Anwendung durch viele automatische Anfragen für echte unzugänglich zu machen.
Durch die erhöhte Eintrittswahrscheinlichkeit muss dieses Risiko, wenn die Anwendung produktiv betrieben werden, unbedingt behandelt werden.

#### Auswirkung
DDoS-Angriffe sind trotz ihrer einfachen Struktur sehr gefährliche Angriffe. Durch gigantische Botnetze mit über 500.000 Netzwerkgeräten können Angreifer enormen Traffic verursachen. Damit sind die Angriffe für Unternehmen, die von der Erreichbarkeit ihrer Webanwendungen abhängig sind, extrem gefährlich. Zudem gibt es für DDoS-Angriffe keine gute Absicherung. 

### Maßnahmen
#### Organisatorische Maßnahmen:
Es sollte eine Risikobewertung für den Fall eines DDoS-Angriffes erstellt werden.
Ein Ablaufplan mit Richtlinien für die Vorgehensweise in einem akuten Angriffsfall muss aufgestellt werden. Spezielle Handlungsrollen für das IT-Personal, andere Geschäftsabteilungen und eingebundene Dienstleister müssen darin festgelegt sein. Im Anschluss an die Konzeptionierung sollte die Wirkung der Strategie mithilfe simulierter Angriffsszenarien getestet werden. Regelmäßiges Überprüfen und Testen der Abwehrstrategie ist ebenso wichtig.

#### Sofortmaßnahmen bei einem Angriff
Whitelisting für besonders wichtige, zugriffsberechtigte Nutzer oder Kunden infrage. Bei umsatzkritischen Webdiensten hingegen, auf die viele Nutzer Zugriff haben, können eine Log-in-Wall, Captchas oder eine Überprüfung der Browser-Echtheit den Dienst auf Anwendungsebene schützen.

#### Anti-DDoS Appliance
Mithilfe einer Anti-DDoS Appliance kann in das Netzwerk eingehender Datenverkehr gefiltert werden. Mit einer Anti-DDoS-Appliance kann einigen Angriffsmustern im Rahmen der verfügbaren Anbindungsbandbreite entgegengewirkt werden. Solche Anti-DDoS-Appliances bieten, je nach Ausführung, neben Filterung von altbekannten DoS-Mustern inzwischen auch selbstlernende Filter gegen unbekannte Angriffe auf Applikations-Ebene, „Low and Slow“-Angriffe und Multivektor-Angriffe.

#### Externe Dienstleistungsmodelle
Einige Netzbetrieber bieten im Fall eines DDoS Angriffs spezielle Anti-DDoS Maßnahmen an.

Sollte der lokale Netzbetreiber keine solchen Maßnahmen Anbieten, gibt es spezialisierte Dienstleister die verscheidene Modelle des DDoS-Schutzes anbieten.
- Traffic-Scrubbing-Netze (Verkehrssäuberungs-Netze), die bei erkannterm DDoS-Angriff den Verkehr über ein detiziertes Netzwerk mit DDoS-Filter routen
- Content-Delivery-Network (CDN), die statische Inhalte redundant via Caching oder Replikation auf Servern verteilen, die an vielen verschiedenen Standorten in verschiedene autonome Systeme eingebunden sind.
- Mega Cloud, die viele redundante Ressourcen in einer weltweit verteilten Umgebung bietet. Durch hohe Anbindungs-Bandbreiten kombiniert mit Skalierbarkeit und Replikation können hier Webservices mit umfangreichen Cyber-Sicherheitsfeatures geschützt zur Verfügung gestellt werden.
- Cloud-Filter, die als Reverse-Proxy über einem weltweiten Content Delivery Network (CDN) mit DNS-Servern, Caching, Blocklisten, BGP Origin Protection, Web-Application-Firewall (WAF), Malware-Scanner, Spam-Schutz und in Bezug auf Schutz vor DDoS-Angriffen verschiedenen modernen Cyber-Schutzmechanismen agieren. Durch die Redundanz in verschiedenen Autonomen Systemen, stetige Weiterentwicklung der Cyber-Schutztechnologien und rundum großzügig dimensionierte Kapazitäten erreichen diese Cloud-Filternetze einen starken Schutz mit vielen einfach nutzbaren Zusatzleistungen zum Schutz von Webanwendungen

### Fazit
In der Anwendung selbst kann nur geringfügig für Schutz gegen DDoS-Attacken gesorgt werden. Eine Möglichkeit ist die Überprüfung der Benutzer mit Captchas oder der Überprüfung der Browserechtheit.

Weiere Maßnahmen sind von der Anwendung unabhängig und werden daher in die Verantwortung des Betreibers gelegt. Um dem Betreiber maximale flexibilität bei der Wahl seines DDoS-Schutzkonzeptes zu ermöglichen, muss die Anwendung auch auf verteilten Systemen lauffähig sein.
