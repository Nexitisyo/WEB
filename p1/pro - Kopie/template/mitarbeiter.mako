## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mitarbeiter</title>
    <script src="/../script.js"></script>
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head>
<body>
<table class="collapse">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Vorname</th>
        <th>Funktion</th>
        <th>Aktion</th>
    </tr>
    % for mitarbeiter in liste:
        <tr class="selected" id="${mitarbeiter['id']}" onclick="editPy(id)" onmouseenter="selectionMarker(${mitarbeiter['id']})" onmouseleave="deselectionMarker(${mitarbeiter['id']})">

            <td>${mitarbeiter['id']}</td>
            <td>${mitarbeiter['name']}</td>
            <td>${mitarbeiter['vorname']}</td>
            <td>${mitarbeiter['funktion']}</td>
            <td>
                <ul class="buttons">
                <li><a href="delete?key=${mitarbeiter['id']}">löschen</a><li>
                </ul>
            </td>
        </tr>
    % endfor
</table>
    <ul>
        <li><a href="add">Neuen Mitarbeiter hinzufügen</a></li>
        <li><a href="/../">Zurück zur Startseite</a></li>
    </ul>
</body>
</html>