## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    %if action is not UNDEFINED:
        <title>Mitarbeiter bearbeiten</title>
    %else:
        <title>Mitarbeiter hinzufügen</title>
    %endif
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head>
<body>


<form action="save" method="post">
    <label for="name">Name:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${mitarbeiter['name']}"
        %else:
           value=""
        %endif
           id="name"
           name="name"/>
    <label for="vorname">Vorname:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${mitarbeiter['vorname']}"
        %else:
           value=""
        %endif
           id="vorname" name="vorname"/>
    <label for="funktion">Funktion:</label>
    <input type="text"
        %if action is not UNDEFINED:
           value="${mitarbeiter['funktion']}"
        %else:
           value=""
        %endif
           id="funktion" name="funktion"/>

    <input type="submit" value="speichern"/>
    %if action is not UNDEFINED:
        <input type="hidden" value="${mitarbeiter['id']}" name="key" />
    %endif

</form>


</body>
</html>