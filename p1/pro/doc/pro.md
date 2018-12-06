## DOKUMENTATION ZUM WEB PRAKTIKUM ##


#### EINLEITUNG ####

Gruppe:				E
Aufbau des Teams:   Mark Borgmann, Viktor Kuznecov
Gueltigkeitsdatum:  30.11.2018



#### BESCHREIBUNG ####

Aufgabe der Anwendung:
Ber der vorliegenden Webanwendung handelt es sich um ein Projektinformationssystem.
Der Anwender soll in der Lage sein,  Kunden, Mitarbeiter und Projekte anzuzeigen, anzulegen und bei Bedarf zu bearbeiten sowie zu loeschen.



Kunden haben folgende Schluessel:
Kunden-ID, Kundennummer, Bezeichnung, Ansprechpartner, Ort

Das Kundendatenblatt enthaelt folgende Funktionen:
- (jew.) Bearbeiten 
- (jew.) Loeschen
- Kunden hinzufuegen
- Zurueck zur Startseite



Mitarbeiter haben folgende Schluessel:
Mitarbeiter-ID, Name, Vorname, Funktion

Das Mitarbeiterdatenblatt enthaelt folgende Funktionen:
- (jew.) Bearbeiten
- (jew.) Loeschen
- Mitarbeiter hinzufuegen
- Zurueck zur Startseite



Projekte haben folgende Schluessel:
Projekt-ID, Projektnummer, Bezeichnung, Beschreibung, Zeitraum, Budget, Kundenverweis, Mitarbeiterverweis, Aufwand

Das Projektdatenblatt enthaelt folgende Funktionen:
- (jew.) Bearbeiten
- (jew.) Loeschen
- (jew.) Organisieren
- Projekt hinzufuegen
- Zurueck zur Startseite



#### SERVERSEITIGE FUNKTIONEN ####

Auf der Serverseite wurde eine weitgehende Distribution-of-Concerns-Idee verfolgt.
Es stehen folgende Dateien zur Verfuegung:

 -  server.py    (Startet den Server)

/app:
 - orga.py:
      Dient zur Einteilung des Aufwands fuer Mitarbeiter

       index(self)
              returned orga-form.mako, initialisiert JSON-Dateien

       save(self, aufwandGeteilt, bezeichnung, mitarbeiter, key=None)
              aktualisiert einen Eintrag
              ruft Uebersicht auf

       edit(self, key)
              initialisiert JSON-Dateien
              returned orga-form.mako

       default(self, *arglist, **kwargs)
              Fehlerbehandlung bei ungueltigem Seitenaufruf

       Zusammenwirken: database.py


 - view.py:
      Erstellt Dictionaries, zeigt Template an
        
        create(self, template_spl, data_opl=None, data2=None, data2=None, data3=None, data4=None)
              Erstellt oder uebergibt Dictionaries
              Zeigt Template an

       Zusammenwirken: Mit jeder Seite
        

 - index.py:
      Startseite

        index(self)
              zeigt index.mako an

        default(self, *arglist, **kwargs)
              Fehlerbehandlung bei ungueltigem Seitenaufruf

       Zusammenwirken: /

 - kunden.py: 
      ruft alle Funktionen der Kunden (add, delete, save, edit, default und index) auf
       
        index(self)
              zeigt kunden.mako an
        save(self, kundennummer, bezeichnung, ansprechpartner, ort, key=None)
              erstellt oder aktualisiert neuen Eintrag
        add(self)
              zeigt kunden-form.mako an
        delete(self, key)
              entfernt einen Eintrag mithilfe des Keys
        edit(self, key)
              ruft kunden-form.mako mit bestimmten Eintrag auf

        default(self, *arglist, **kwargs)
              Fehlerbehandlung bei ungueltigem Seitenaufruf

       Zusammenwirken: database.py

 - projekte.py
      ruft alle Funktionen der Projekte (add, delete, save, edit, default und index) auf

        index(self)
              zeigt projekte.mako an
        save(self, projektnummer, bezeichnung, bearbeitungszeitraumA, bearbeitungszeitraumB, budget, kundenverweis, mitarbeiterverweis, key=None)
              erstellt oder aktualisiert neuen Eintrag, und kopiert diesen in orga.json
        add(self)
              zeigt projekte-form.mako an
        delete(self, key)
              entfernt einen Eintrag aus Projekte.json und orga.json mithilfe des Keys
        edit(self, key)
              ruft projekte-form.mako mit bestimmten Eintrag auf
        default(self, *arglist, **kwargs)
              Fehlerbehandlung bei ungueltigem Seitenaufruf

        - Zusammenwirken: database.py
       

 - database.py:
      Beinhaltet alle Datenbank-Funktionen, welche sich von anderen .py-Dateien aufrufen lassen 

        read(dbfile)
              laedt .json-File in eine Variable
              returned den Pfad der .json
        calc(start, end)
              kalkuliert Differenz zwischen zwei Bearbeitungszeitraeumen in Tagen
        readValueById(dbfile, key)
              sucht nach Eintrag mit entsprechendem Key
              returned diesen Eintrag
        write(dbfile, newData)
              schreibt in .json-File
        writeValueById(dbfile, key, newData)
              sucht nach Eintrag mit entsprechendem Key
              falls gefunden, Eintrag updaten
              falls nicht, Eintrag neu schreiben
              updated .json-File
        deleteValueById(dbfile, key)
              sucht nach Eintrag mit entsprechendem Key
              loescht diesen Eintrag
              updated .json-File
        append(dbfile, values)
              erhoeht Counter fuer ID
       
        - Zusammenwirken: /
         
 - auswertung.py:
      Stellt eine Uebersicht aller Projekte anhand von Projektbezeichnung, Mitarbeiter und Aufwand zusammen
        
        index(self)
              zeigt Auswertung.mako an
        default(self, *arglist, **kwargs)
              Fehlerbehandlung bei ungueltigem Seitenaufruf
       
         
 - mitarbeiter.py:
      ruft alle Funktionen der Mitarbeiter (add, delete, save, edit, default und index) auf

        index(self)
              zeigt mitarbeiter.mako an
        save(self, funktion, name, vorname, key=None)
              erstellt oder aktualisiert neuen Eintrag
        add(self)
              zeigt mitarbeiter-form.mako an
        delete(self, key)
              entfernt einen Eintrag aus mitarbeiter.json mithilfe des Keys
        edit(self, key)
              ruft mitarbeiter-form.mako mit bestimmten Eintrag auf
        default(self, *arglist, **kwargs)
              Fehlerbehandlung bei ungueltigem Seitenaufruf
       
       - Zusammenwirken: database.py


 /content:
 - script.js:
      Enthaelt Funktionen fuer Mouse-Events

        selectionMarker(id)
            markiert ein Element und fuegt deren ID zu einer Liste hinzu
            
       falls nicht markiert -> 
            selektiere das Element und fuege ID zur Liste hinzu
            zeige Button zum Bearbeiten an, falls nur 1 Element markiert
            zeige Button zum loeschen an.
            
       falls markiert -> 
            deselektiert das Element und loescht deren ID aus der Liste
            Falls 1 oder mehr noch markiert, zeige Button zum Loeschen an
            Ansonsten verstecke Button zum bearbeiten

       colorToHex(color)
     	   konvertiert RGB(A) zu Hex-Farbschema

       editHref()
       	 Weiterleitung zur Bearbeitungsform



 - style.css:
       Legt massgebliche Regeln zum Erscheinungsbild der Webseite fest
       Beinhaltet gekapselte Informationen zu html-Befehlen (wie z.B.)
       Wird von allen Seiten verwendet

 - LOVES.ttf        (Schriftart)
 - Capsuula.tff     (Schriftart)

 /data:

 	Beinhaltet alle Datenbanken mit Eintraegen
 	  data.json
 	  orga.json
 	  kunden.json
 	  projekte.json
 	  mitarbeiter.json

 /doc:
 	  pro.md (Diese Dokumentation)

 /template:
 	  index.mako
 	  liste.mako
 	  kunden.mako
 	  projekte.mako
 	  orga-form.mako
 	  auswertung.mako
       mitarbeiter.mako
 	  kunden-form.mako
 	  projekte-form.mako
 	  mitarbeiter-form.mako

#### DATENABLAGE ####

Zur Ablage saemtlicher Datenbestaende wurde das .JSON (JavaScript Object Notation)-Format genutzt.
Datenbankfunktionen selbst werden durch die database.py realisiert, welche verschiedene Schnittstellen zum
erstellen, speichern, bearbeiten und loeschen bereitstellt.

#### PRUEFUNGSPROTOKOLL W3C-VALIDATOR ####


