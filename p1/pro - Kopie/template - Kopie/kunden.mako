## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script type="text/javascript" src="/../script.js"></script>
    <link rel="stylesheet" type="text/css" href="/../style.css">
    <title>Kunden</title>
</head><body>
<table class="collapse">
        <tr>
        <th>ID</th>
        <th>Kundennummer</th>
        <th>Bezeichnung</th>
        <th>Ansprechpartner</th>
        <th>Ort</th>
        <th>Aktion</th>
    </tr>
    % for kunden in liste:
   <tr class="selected" id="${kunden['id']}" onclick="editPy(id)" onmouseenter="selectionMarker(${kunden['id']})"" onmouseleave="deselectionMarker(${kunden['id']})">
            <td>${kunden['id']}</td>
            <td>${kunden['kundennummer']}</td>
            <td>${kunden['bezeichnung']}</td>
            <td>${kunden['ansprechpartner']}</td>
            <td>${kunden['ort']}</td>
            <td>
                <ul class="buttons">
                    <li><a href="delete?key=${kunden['id']}">löschen</a></li>
                </ul>
            </td>
        </tr>
    % endfor
</table>
    <ul>
        <li><a href="add">Kunden hinzufügen</a></li>
        <li><a href="/../">Zurück zur Startseite</a></li>
    </ul>
</body>
</html>