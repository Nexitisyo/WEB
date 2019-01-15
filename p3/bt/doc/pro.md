## DOKUMENTATION ZUM WEB PRAKTIKUM ##

Fehler:
Kategorien lassen sich nicht bearbeiten
Es lässt sich nur ein Fehler erstellen
Es lässt sich keine Lösung hinzufügen

#### EINLEITUNG ####

Gruppe:				E
Aufbau des Teams:   Mark Borgmann, Viktor Kuznecov
Gueltigkeitsdatum:  14.01.2019


#### BESCHREIBUNG ####

Aufgabe der Anwendung:
Ber der vorliegenden Webanwendung handelt es sich um ein Bug-Tracker.
Der Anwender soll in der Lage sein, Projekte, Komponenten, Mitarbeiter und Kategorien anzulegen, zu bearbeiten und ggf. auch zu loeschen. Ueber diese Values sollen Fehler angelegt und protokolliert werden koennen. Ziel der Uebung ist, fuer auftretende Fehler sofort eine Loesung bereit zu haben.


####### Fehler #######
Fehler haben zwei Zustaende: erkannt und beseitigt.
Bei der Erstellung eines Fehlers befindet sich dieser im Zustand "erkannt". Durch das hinzufuegen einer Loesung erhaelt der Fehler den Status "beseitigt". Somit lassen sich geloeste und noch nicht geloeste Fehler nach Zustand sortieren. 
Fehler lassen sich sortieren, erstellen und bearbeiten.


####### Projekte #######
Projekte ist der Ueberbegriff zur Zuordnung von Fehlern sowie Komponenten und Kategorien. Jede Komponente und jede Kategorie ist einem bestimmten Fehler im Projekt zugeordnet. 
Projekte lassen sich sortieren, erstellen, bearbeiten und loeschen.


####### Kategorien #######
Kategorien bedeuten in diesem Zusammenhang die Zuordnung von Fehlern zu einer bestimmten Gattung, wie zum Beispiel "Hardware", "Beschaedigungen" etc. Somit kann man die Ursache eines Fehlers einem bestimmten Stamm zuordnen. 
Kategorien lassen sich sortieren, erstellen, bearbeiten und loeschen.


####### Komponenten #######
Komponenten sagen aus, an welcher Stelle im Projekt ein Fehler aufgetreten ist und somit das fehlerhafte Glied im Projekt identifiziert werden kann. Beispielsweise könnte man als Komponente "Mainboard" festlegen, um auszusagen, dass an dieser Stelle ein Fehler aufgetreten ist. 
Komponenten lassen sich sortieren, erstellen, bearbeiten und loeschen.


####### Mitarbeiter #######
Mitarbeiter sind eingeteilt in Softwareentwicklung und Qualitaetsservice. Der Qualitaetsservice kann Fehler erstellen, waehrend der Softwareentwickler daran beteilt ist, besagte Probleme zu loesen.
Mitarbeiter lassen sich sortieren, erstellen, bearbeiten und loeschen.


#### REST-Interface ####

Grundlage des REST-Interfaces ist das Method-Dispatching. Die Methoden, die verwendet werden koennen, sind GET, POST, PUT und DELETE. Alle Anfragen werden vom Server in dem JSON-Format an die entsprechende Anfrage zurueckgeschickt.


#### Module

#####database.py
Die Database.py ist das Herzstueck des Projektes, da es wichtige Datenbankfunktionen enthaelt, die im ganzen Bug-Tracker in Bezug auf Datenbanken aufgerufen werden. Die Database.py beinhaltet Funktionen zum erstellen, bearbeiten, loeschen und anzeigen von Daten mit / aus einer JSON-Datei.

#####login.py
Die Login.py ist verantwortlich für den korrekten Ablauf der Anmeldefunktion des Projektes. Es wird ueberprueft ob der eingegebene Username in der entsprechenden Mitarbeiter-JSON existiert, und falls dies der Fall ist, der Login-Vorgang ausgefuehrt.

#####navigation.py
Dieses Modul ist verantwortlich fuer den Navigator auf der linken Seite des Bug-Tracers. Mithilfe der entsprechenden Mitarbeiter-Rolle sendet die Navbar ein anderes Navigationsobjekt.

#####employee.py
Die Employee.py enthaelt verschiedenste Funktionen fuer jeweils Softwareentwickler- und Qualitaetsservicemitarbeiter.

#####role.py
Die Role.py beinhaltet GET-Methoden fuer Rollen, damit Mitarbeiter sich entsprechende Rollen zuweisen lassen koennen.

#####project.py
Die Project.py stellt die Schnittstelle fuer Projekte, Projektkomponenten und Komponenten bereit. Die Project.py arbeitet vorwiegend mit der Database.py zusammen und ermoeglicht die Uebergabe und Ausfuehrung von verschiedenen Funktionen.

#####error.py
Die Error.py beinhaltet alle Funktionen, die sich ueber Fehler/, Loesung/, Katursache/ und Katfehler/ aufrufen lassen. Diese Funktionen uebergeben Daten an die database.py, welche diese dann weiter verwerten kann.

#####template.py
Die Template.py ist verantwortlich fuer die Uebergabe der Mako-Templates vom Server zum Client.


--

#### Datenablage
Jegliche Form der Datenhaltung findet im JSON-Format statt. So speichert beispielsweise die employee.json alle relevanten Mitarbeiterdaten, die project.json jegliche Informationen ueber die Projekte, die error.json hingegen alle eingetragenen Fehler sowie deren entsprechenden Loesungen mitsamt Kategorie. Gegebenenfalls auftredende andere Verweise werden anhand der ID realisiert. Das gilt auch fuer Daten, zwischen denen eine Korrelation besteht.

#### UEBERSICHT FUNKTIONEN ####

    
##### JSON FILE
	def initJSON(self):
        Initialisiert error-, employee- und project.json

    def writeJSONFile(self, filename, data):
         Updated übergebenes JSON-File mit neuem Datensatz.

    def readJSONFile(self, filename):
        Gibt den Inhalt des JSON-Files wieder.
        
##### HELP FUNCTIONS
    def isNumber(self, string):
        Prüft ob übergebener Wert eine Zahl ist.

    def getNextID(self, filename):
        Gibt die nächsthöchste ID, inkrementiert wieder.

    def getById(self, filename, id):
       Gibt einen gesuchten Eintrag anhand der ID wieder.
	   
##### LOGIN FUNCTIONS
    def getRoleIdByUsername(self, username):
		Gibt den Benutzer anhand von "username" wieder.
		
##### PROJECT FUNCTIONS
    def getAllProjects(self):
        Gibt alle Projekte und ihre Komponenten wieder.

    def getProjectById(self, id):
        Gibt ein Projekt und dessen Komponenten wieder.

    def createProject(self, name, desc):
       Erstellt neuen Eintrag und returned dessen neue ID

    def updateProject(self, id, name, desc):
       Updated ein Projekt. True falls erfolgreich, sonst False.

    def deleteProject(self, id):
        Löscht ein Projekt anhand einer ID.

##### COMPONENT FUNCTIONS
    def getAllComponents(self):
        Gibt alle Komponenten wieder.

    def getComponentById(self, id):
        Gibt Komponente anhand einer ID wieder.

    def createComponent(self, name, desc, projectid):
        Legt neue Komponente anhand einer Project-ID und weist inkrementierte ID zu.

    def addErrorToCoponent(self, componentid, errorid):
        Legt einen Fehler(anhand einer Fehler-ID) zu einer bestimmten Komponente(anhand einer Error-ID) an.

    def updateComponent(self, id, name, desc, projectid):
        Updated Komponente anhand einer ID.
		
    def deleteComponent(self, id, skip=False):
        Löscht Komponente anhand einer ID.

    # Role Function # 
    def getAllRoles(self):
        Gibt alle Benutzerrollen wieder.
##### EMPLOYEE FUNCTIONS 
    def getAllEmployees(self):
        Gibt alle Benutzer wieder.

    def getEmployeeById(self, id):
        Gibt Benutzer anhand der ID wieder.

    def createEmployee(self, roleid, username, firstname, lastname, email, phone, address):
        Legt neuen Benutzer an und weist inkrementierte ID zu.

    def updateEmployee(self, id, roleid, username, firstname, lastname, email, phone, address):
        Updated Benutzerinformationen.

    def deleteEmployee(self, id):
        Löscht Benutzer anhand der ID.

##### SOFTWARE-DEVELOPER FUNCTIONS

    def getAllSoftwareDeveloper(self):
        Gibt alle SW-Benutzer wieder.

    def getSoftwareDeveloperById(self, id):
		Gibt SW-Benutzer anhand der ID wieder.

    def createSoftwareDeveloper(self, username, fistname, lastname, email, phone, address):
		Legt neuen SW-Benutzer an.

##### QUALITY-MANAGEMENT FUNCTIONS

    def getAllQualityManagement(self):
        Gibt alle QS-Benutzer wieder.

    def getQualityManagementById(self, id):
		Gibt QS-Benutzer anhand der ID wieder.
		
    def createQualityManagement(self, username, firstname, lastname, email, phone, address):
        Legt neuen QS-Benutzer an.

##### ERROR CATEGORY

    def getAllErrorCategories(self):
        Gibt alle Fehlerkategorien wieder.

    def getErrorCategoryById(self, id):
		Gibt Fehlerkategorie anhand der ID wieder.
    def createErrorCategory(self, name):
		Legt neue Fehlerkategorie an und weist inkrementierte ID zu.

    def updateErrorCategory(self, id, name):
		Updated Fehlerkategorie anhand der ID.

    def deleteErrorCategory(self, id):
		Löscht Fehlerkategorie anhand der ID.
    def getAllResultCategories(self):
        Gibt alle Lösungskategorien wieder.

##### RESULT CATEGORY
    def getResultCategoryById(self, id):
		Gibt Lösungskategorie anhand der ID wieder.

    def createResultCateogry(self, name):
        Legt neue Kategorie an und weist inkrementierte ID zu.

    def updateResultCategory(self, id, name):
		Updated eine Lösungskategorie anhand der ID.

    def deleteResultCategory(self, id):
		Löscht eine Lösungskategorie anhand der ID.

##### ERROR FUNCTIONS
    def getAllErrors(self):
        Gibt alle Fehlereinträge wieder.

    def getErrorById(self, id):
		Gibt Fehlereintrag anhand der ID wieder.

    def getAllErrorsByType(self, type):
        Gibt alle Fehlereinträge anhand des Typs wieder.

    def createNewError(self, desc, employee, component, categories):
        Legt neuen Fehlereintrag an und weist inkrementierte ID zu.

    def updateError(self, id, desc, employee, component, categories):
        Updated einen Fehlereintrag.

    def deleteError(self, id):
		Löscht einen Fehlereintrag anhand der ID

##### FEHLEREINTRAG

    def GET(self, id=None, type=None):
        Gibt Fehlereintrag anhand des Typs und ID wieder.

    
    def POST(self, desc, employee, component, category):
        Erstellt neuen Fehlereintrag.

    
    def PUT(self, id, desc, employee, component, category):
        Updated Fehlereintrag anhand der ID.
		
#####  FEHLERKATEGORIE

    def GET(self, id=None):
        Gibt Fehlerkategorie anhand der ID wieder.

	def POST(self, name):
        Erstellt neue Fehlerkategorie.
		
    def PUT(self, id, name):
        Updated Fehlerkategorie anhand der ID.

    def DELETE(self, ids):
        Löscht Fehlerkategorie anhand der ID.
		
#####LOESUNGSEINTRAG
    def GET(self, id):
        Gibt Lösungseintrag wieder anhand der ID.

    
    def POST(self, desc, employee, error, categories):
		Erstellt neuen Lösungseintrag.

    
    def PUT(self, id):
        Updated Lösungseintrag anhand der ID.
##### LOESUNGSKATEGORIE

    def GET(self, id=None):
        Gibt Lösungskategorie anhand ID wieder.

    
    def PUT(self, id, name):
        Updated Lösungskategorie anhand der ID.

    
    def POST(self, name):
        Erstellt neue Lösungskategorie.

    
    def DELETE(self, ids):
        Löscht Lösungskategorie anhand der ID.

##### RESULT FUNCTIONS
    def getAllResult(self):
        Gibt alle Lösungseinträge wieder.

    def getResultById(self, id):
        Gibt einen Lösungseintrag anhand der ID wieder.

    def createNewResult(self, desc, employee, error, categories):
        Legt neuen Lösungeintrag an und weist inkrementierte ID zu.

    def updateResult(self, id):
        Updated einen Lösungeintrag anhand der ID.

    def deleteResult(self, id):
        Löscht einen Lösungeintrag anhand der ID.

#### ORDNERSTRUKTUR ####

- server.py (Startet den Server)


##### /app:
	
    Beinhaltet alle Python-Dateien

##### /content:

	css-Folder
    js-Folder
	
##### /data:

	Beinhaltet alle Datenbanken mit Eintraegen


 #####/doc:

	pro.md (Diese Dokumentation)

 ##### /template:

	Beinhaltet alle Mako-Templates



#### PRUEFUNGSPROTOKOLL W3C-VALIDATOR ####

Alle Pruefungen unter Zuhilfenahme des W3C-Validators waren erfolgreich und fehlerfrei.

