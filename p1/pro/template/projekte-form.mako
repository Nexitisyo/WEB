## coding: utf-8
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    %if action is not UNDEFINED:
        <title>Projekt bearbeiten</title>
    %else:
        <title>Projekt hinzufügen</title>
    %endif
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head>
<body>

<form class="collapse" action="save" method="post">
    <label for="projektnummer">Projektnummer:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekte['projektnummer']}"
        %else:
           value=""
        %endif
           id="projektnummer"
           name="projektnummer"/>
#######################################################################################################################################
    <label for="bezeichnung">Bezeichnung:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekte['bezeichnung']}"
        %else:
           value=""
        %endif
           id="bezeichnung" name="bezeichnung"/>
#######################################################################################################################################
    <label for="beschreibung">Beschreibung:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekte['beschreibung']}"
        %else:
           value=""
        %endif
           id="beschreibung" name="beschreibung"/>
#######################################################################################################################################
    <label for="bearbeitungszeitraum">Bearbeitungszeitraum:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekte['bearbeitungszeitraum']}"
        %else:
           value=""
        %endif
           id="bearbeitungszeitraum" name="bearbeitungszeitraum"/>
#######################################################################################################################################
    <label for="budget">Budget:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekte['budget']}"
        %else:
           value=""
        %endif
           id="budget" name="budget"/>
#######################################################################################################################################
    <label for="kundenverweis">Kundenverweis:</label>
    <input list="kunden" 
        %if action is not UNDEFINED:
            value="${projekte['kundenverweis']}"
        %else:
            value=""
        %endif
            id="kundenverweis" name="kundenverweis">
            
    <datalist id="kunden">
        % for kunden in liste:
            <option value="${kunden['id']}">${kunden['bezeichnung']}</option>
        % endfor
    </datalist> 
#######################################################################################################################################
    <label for="mitarbeiterverweis">Mitarbeiterverweis:</label>
    <input list="mitarbeiter" 
        %if action is not UNDEFINED:
            value="${projekte['mitarbeiterverweis']}"
        %else:
            value=""
        %endif
            id="mitarbeiterverweis" name="mitarbeiterverweis">
            
    <datalist id="mitarbeiter">
        % for mitarbeiter in liste2:
            <option value="${mitarbeiter['id']}">${mitarbeiter['name']}</option>
        % endfor
    </datalist> 
#######################################################################################################################################          
    <label for="aufwand">Aufwand:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekte['aufwand']}"
        %else:
           value=""
        %endif
           id="aufwand" name="aufwand"/>
    <input type="submit" value="speichern"/>
    %if action is not UNDEFINED:
        <input type="hidden" value="${projekte['id']}" name="key" />
    %endif
</form>
</body>
</html>