Sie können sich bei Ihrer Implementierung an folgenden Überlegungen orientieren:
• jeder Instanz jeder im Datenmodell genannten Klasse wird durch einen Objekt-ID eindeutig identifiziert
• als Objekt-ID kann eine Ganzzahl verwendet werden, die zentral verwaltet wird
	? der aktuelle Wert wird z.B. in einer Datei abgelegt, damit er bei jedem Start des Webservers weiter verwendet werden kann
	? Werte werden nicht neu verwendet, es wird bei Anlegen neuer Instanzen einfach durch Inkrementieren eine neue Objekt-ID
	erzeugt
	
• für jede Klasse wird eine eigene JSON-Datei verwendet, die alle Instanzen der Klasse enthält
• für Beziehungen müssen ggf. ebenfalls eigene JSON-Datein verwendet werden
	? Beziehungen werden anhand der Objekt-IDs identiziert
	
• das von Ihnen zu implementierende Modul database.py kapselt die skizzierte Verwaltung der persistenten Daten und stellt
den anderen Modulen eine geeignete Schnittstelle zur Bearbeitung zur Verfügung
	? direkte Zugriffe auf die (interne) Form der persistenten Daten durch andere Module sind unbedingt zu vermeiden	