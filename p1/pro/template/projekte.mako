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
            <td>${projekte['bearbeitungszeitraum']}</td>
            <td>${projekte['budget']}</td>
            <td>${projekte['kundenverweis']}</td>
            <td>${projekte['mitarbeiterverweis']}</td>
            <td>${projekte['aufwand']}</td>
            <td>
                <a href="edit?key=${projekte['id']}">bearbeiten</a> <a href="delete?key=${projekte['id']}">löschen</a>
            </td>
        </tr>
    % endfor
</table>
<p>Neues Projekt <a href="add">hinzufügen</a></p>
<p>Zurück zur <a href="/../">Startseite</a></p>
</body>
</html>