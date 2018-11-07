## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head><body>
<table class="collapse">
    <tr>
        <th>ID</th>
        <th>Projektnummer</th>
        <th>Bezeichnung</th>
        <th>Beschreibung</th>
        <th>Bearbeitungszeitraum</th>
        <th>Budget</th>
        <th>Kundenverweis</th>
        <th>Mitarbeiterverweis</th>
        <th>Aufwand</th>
        <th>Aktion</th>
    </tr>

    % for projekte in liste:
        <tr>
            <td>${projekte['id']}</td>
            <td>${projekte['projektnummer']}</td>
            <td>${projekte['bezeichnung']}</td>
            <td>${projekte['beschreibung']}</td>
            <td>${projekte['bearbeitungszeitraumA']} bis ${projekte['bearbeitungszeitraumB']}</td>
            <td>${projekte['budget']}</td>
            <td>${projekte['kundenverweis']}</td>
            <td>${projekte['mitarbeiterverweis']}</td>
            <td>${projekte['aufwand']}</td>
            <td>
                <ul class="buttons">
                    <li><a href="edit?key=${projekte['id']}">Bearbeiten</a></li>
                    <li><a href="delete?key=${projekte['id']}">Löschen</a></li>
                    % for orga in liste3:
                        <li><a href="/orga/edit?key=${orga['id']}">${orga['bezeichnung']}</a></li>
                    % endfor
                </ul>
            </td>
        </tr>
    % endfor
</table>
    <ul class="buttons">
        <li><a href="add">Projekt hinzufügen</a></li>
        <li><a href="/../">Zurück zur Startseite</a></p></li>
    </ul>
</body>
</html>