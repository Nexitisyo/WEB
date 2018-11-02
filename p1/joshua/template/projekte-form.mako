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


<form action="save" method="post">
    <label for="projektnummer">Projektnummer:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['projektnummer']}"
        %else:
           value=""
        %endif
           id="projektnummer"
           name="projektnummer"/>
    <label for="bezeichnung">Bezeichnung:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['bezeichnung']}"
        %else:
           value=""
        %endif
           id="bezeichnung" name="bezeichnung"/>
    <label for="beschreibung">Beschreibung:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['beschreibung']}"
        %else:
           value=""
        %endif
           id="beschreibung" name="beschreibung"/>
    <label for="bearbeitungszeitraum">Bearbeitungszeitraum:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['bearbeitungszeitraum']}"
        %else:
           value=""
        %endif
           id="bearbeitungszeitraum" name="bearbeitungszeitraum"/>
    <label for="budget">Budget:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['budget']}"
        %else:
           value=""
        %endif
           id="budget" name="budget"/>
    <label for="kundenverweis">Kundenverweis:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['kundenverweis']}"
        %else:
           value=""
        %endif
           id="kundenverweis" name="kundenverweis"/>
    <label for="mitarbeiterverweis">Mitarbeiterverweis:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['mitarbeiterverweis']}"
        %else:
           value=""
        %endif
           id="mitarbeiterverweis" name="mitarbeiterverweis"/>
    <label for="aufwand">Aufwand:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${projekt['Aufwand']}"
        %else:
           value=""
        %endif
           id="aufwand" name="aufwand"/>
    <input type="submit" value="speichern"/>
    %if action is not UNDEFINED:
        <input type="hidden" value="${projekt['id']}" name="key" />
    %endif

</form>


</body>
</html>