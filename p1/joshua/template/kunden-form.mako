## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    %if action is not UNDEFINED:
        <title>Kunden bearbeiten</title>
    %else:
        <title>Kunden hinzufügen</title>
    %endif
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head>
<body>

<form action="save" method="post">

    <label for="kundennummer">Kundennummer:</label>
    ## if action is not UNDEFINED = Wenn action in form action definiert ist z.B durch einen Aufruf in kunden.py dann setze value auf einen bestimmten Eintrag
    <input type="text"
        %if action is not UNDEFINED: 
           value="${kunden['kundennummer']}"
        %else:
           value=""
        %endif

           id="kundennummer"
           name="kundennummer"/>

    <label for="bezeichnung">Bezeichnung:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${kunden['bezeichnung']}"
        %else:
           value=""
        %endif
           id="bezeichnung" name="bezeichnung"/>

    <label for="ansprechpartner">Ansprechpartner:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${kunden['ansprechpartner']}"
        %else:
           value=""
        %endif
           id="ansprechpartner" name="ansprechpartner"/>

    <label for="ort">Ort:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${kunden['ort']}"
        %else:
           value=""
        %endif
           id="ort" name="ort"/>

    <input type="submit" value="speichern"/>
    %if action is not UNDEFINED:
        <input type="hidden" value="${kunden['id']}" name="key"/>
    %endif

</form>


</body>
</html>