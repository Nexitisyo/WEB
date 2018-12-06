## DOKUMENTATION ZUM WEB PRAKTIKUM ##


#### EINLEITUNG ####

Gruppe:             E
Aufbau des Teams:   Mark Borgmann
                    Viktor Kuznecov
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

Auf der Serverseite wurde eine weitgehende "Distribution-of-concern"-Idee verfolgt. 
Es stehen folgende Dateien zur Verfuegung:

 - server.py    (Startet den Server)

/app:
 - orga.py:
        - Zweck: 
        - Aufbau:
        - Zusammenwirken:
        - API:

 - view.py:
        - Zweck: Laedt Templates, zeigt Templates an,speichert Paths
        - Aufbau:
        - Zusammenwirken:
        - API:

 - index.py:
        - Zweck: Laedt das index.mako Template
        - Aufbau:
        - Zusammenwirken:
        - API: 

 - kunden.py: 
        - Zweck: ruft alle Funktionen der Kunden (add, delete, save, edit, default und index) auf
        - Aufbau:
        - Zusammenwirken: database.py
        - API:

 - projekte.py
        - Zweck: ruft alle Funktionen der Projekte (add, delete, save, edit, default und index) auf
        - Aufbau:
        - Zusammenwirken: database.py
        - API:

 - database.py:
        - Zweck: Beinhaltet alle Datenbank-Funktionen, welche sich von anderen .py-Dateien aufrufen lassen 
        - Aufbau:
        - Zusammenwirken: mitarbeiter.py, projekte.py, kunden.py
        - API:
         
 - auswertung.py:
        - Zweck: Stellt eine Uebersicht aller Projekte anhand von Projektbezeichnung, Mitarbeiter und Aufwand zusammen
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - mitarbeiter.py:
        - Zweck: ruft alle Funktionen der Mitarbeiter (add, delete, save, edit, default und index) auf
        - Aufbau:
        - Zusammenwirken: database.py
        - API:

 /content:
 - script.js:
        - Zweck: Enthaelt Funktionen fuer den MouseOver-Effekt (Zeile markieren)
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - style.css:
        - Zweck: Legt massgebliche Regeln zum Erscheinungsbild der Webseite fest
        - Aufbau: gekapselte Informationen zu html-Befehlen (wie z.B.)
        - Zusammenwirken: wird von allen Seiten verwendet
        - API:
         
 - LOVES.ttf        (Schriftart)
 - Capsuula.tff     (Schriftart)

 /data:
 - data.json
 - orga.json
 - kunden.json
 - projekte.json
 - mitarbeiter.json

 /doc:
 - pro.md (Diese Dokumentation)

 /template:
 - index.mako:
        - Zweck: Template fuer die Startseite      
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - liste.mako:
        - Zweck: 
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - kunden.mako:
        - Zweck: Template fuer das Kundendatenblatt
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - projekte.mako:
        - Zweck: Template fuer das Projektdatenblatt
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - orga-form.mako:
        - Zweck: 
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - auswertung.mako:
        - Zweck: 
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - kunden-form.mako:
        - Zweck: Template fuer die Bearbeitungsflaeche der Kunden
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - mitarbeiter.mako:
        - Zweck:  Template fuer das Mitarbeiterdatenblatt
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - projekte-form.mako:
        - Zweck: Template fuer die Bearbeitungsflaeche der Projekte
        - Aufbau:
        - Zusammenwirken:
        - API:
         
 - mitarbeiter-form.mako:
        - Zweck: Template fuer die Bearbeitungsflaeche der Mitarbeiter
        - Aufbau:
        - Zusammenwirken:
        - API:
         

#### DATENABLAGE ####

Zur Ablage saemtlicher Datenbestaende wurde das .JSON (JavaScript Object Notation)-Format genutzt.

#### PRUEFUNGSPROTOKOLL W3C-VALIDATOR ####


