## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head><body>
<table>
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
    % for projekt in liste:
        <tr>
            <td>${projekt['id']}</td>
            <td>${projekt['projektnummer']}</td>
            <td>${projekt['bezeichnung']}</td>
            <td>${projekt['beschreibung']}</td>
            <td>${projekt['bearbeitungszeitraum']}</td>
            <td>${projekt['budget']}</td>
            <td>${projekt['kundenverweis']}</td>
            <td>${projekt['mitarbeiterverweis']}</td>
            <td>${projekt['aufwand']}</td>
            <td>
                <a href="edit?key=${projekt['id']}">bearbeiten</a> <a href="delete?key=${projekt['id']}">löschen</a>
            </td>
        </tr>
    % endfor
</table>
<p>Neues Projekt <a href="add">hinzufügen</a></p>
<p>Zurück zur <a href="/../">Startseite</a></p>
</body>
</html>