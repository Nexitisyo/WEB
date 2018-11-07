## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head><body>

<form action="save" method="post">
<table class="collapse">
    <tr>
        <th>Projekt</th>
        <th>Mitarbeiter</th>
        <th>Aktion</th>
    </tr>

    % for projekte in liste:
        <tr>
            
            <td>${projekte['id']}</td>
            <td>${projekte['mitarbeiterverweis']}</td>
            <td>
                <ul class="buttons">
                <input type="submit" value="Speichern"/>
                <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
                </ul>
            </td>
        </tr>
    % endfor
</table>
</form>
</body>
</html>