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
    <table class="collapse">
       <tr>
            <th><label for="name">Name:</label></th>
            <th><label for="vorname">Vorname:</label></th>
            <th><label for="funktion">Funktion:</label></th>
            <th>Aktion:</th>
        </tr>
##################################################################################################################
            <tr>
            <td><input type="text"
                %if action is not UNDEFINED:
                    value="${mitarbeiter['name']}"
                %else:
                    value=""
                %endif
                    id="name"
                    name="name"/>
                    ##eafaefaef
            </td>
##################################################################################################################
            <td>
                <input type="text"
                    %if action is not UNDEFINED:
                        value="${mitarbeiter['vorname']}"
                    %else:
                        value=""
                    %endif
                        id="vorname" name="vorname"/>
            </td>
##################################################################################################################
            <td>
                <input type="text"
                    %if action is not UNDEFINED:
                        value="${mitarbeiter['funktion']}"
                    %else:
                        value=""
                    %endif
                        id="funktion" name="funktion"/>
            </td>
            <td>
                <input type="submit" value="Speichern"/>
                <input type="button" value="Abbrechen" onclick="location.href='/mitarbeiter/';"/>
           </td>
           </tr>
        %if action is not UNDEFINED:
            <input type="hidden" value="${mitarbeiter['id']}" name="key" />
        %endif
</table>
</form>
</body>
</html>