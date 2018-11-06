<!DOCTYPE html>
<html lang="en">
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="/../style.css" />
    <title>Mitarbeiterdaten</title>
</head>
<body>
    <h2 text-align="center">Mitarbeiterdaten</h2>
    
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
                <a href="#">bearbeiten</a> <a href="#">l&ouml;schen</a>
            </td>
        </tr>
         % endfor
            <td>
            <a href="edit">bearbeiten</a>
            <a href="delete">l&ouml;schen</a>
        </td>
    </tr>

    </table>
    <br>
    <br>
    <a href="create">Eintrag hinzuf&uuml;gen</a>
    <br>
    <a href="/index">Zur&uuml;ck</a>
</body>