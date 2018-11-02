## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="/../style.css">
    <title>Kunden</title>
</head><body>
<table>
    <tr>
        <th>ID</th>
        <th>Kundennummer</th>
        <th>Bezeichnung</th>
        <th>Ansprechpartner</th>
        <th>Ort</th>
        <th>Aktion</th>
    </tr>
    % for kunden in liste:
        <tr>
            <td>${kunden['id']}</td>
            <td>${kunden['kundennummer']}</td>
            <td>${kunden['bezeichnung']}</td>
            <td>${kunden['ansprechpartner']}</td>
            <td>${kunden['ort']}</td>
            <td>
                <a href="edit?key=${kunden['id']}">bearbeiten</a> <a href="delete?key=${kunden['id']}">löschen</a>
            </td>
        </tr>
    % endfor
</table>
<p>Neuen Kunden <a href="add">hinzufügen</a></p>
<p>Zurück zur <a href="/../">Startseite</a></p>
</body>
</html>