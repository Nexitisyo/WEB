## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mitarbeiter</title>
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
        <tr>
            <td>${mitarbeiter['id']}</td>
            <td>${mitarbeiter['name']}</td>
            <td>${mitarbeiter['vorname']}</td>
            <td>${mitarbeiter['funktion']}</td>
            <td>
                <a href="edit?key=${mitarbeiter['id']}">bearbeiten</a> <a href="delete?key=${mitarbeiter['id']}">löschen</a>
            </td>
        </tr>
    % endfor
</table>
<p>Neuen Mitarbeiter <a href="add">hinzufügen</a></p>
<p>Zurück zur <a href="/../">Startseite</a></p>
</body>
</html>