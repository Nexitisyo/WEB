## coding: utf-8
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <script src="/../script.js"></script>
        <link rel="stylesheet" type="text/css" href="/../style.css">
        <title>Kunden</title>
    </head>
    <body>
        <form action="delete" method="post">
            <table class="collapse">
                <tr>
                    <th>ID</th>
                    <th>Kundennummer</th>
                    <th>Bezeichnung</th>
                    <th>Ansprechpartner</th>
                    <th>Ort</th>
                </tr>
                % for kunden in liste:
                <tr class="" id="${kunden['id']}" ondblclick="selectionMarker(${kunden['id']})" style="background-color: #333333">
                        <td>${kunden['id']}</td>
                        <td>${kunden['kundennummer']}</td>
                        <td>${kunden['bezeichnung']}</td>
                        <td>${kunden['ansprechpartner']}</td>
                        <td>${kunden['ort']}</td>
                </tr>
                % endfor
            </table>
            <input type="hidden" id="inputID" name="key" value=""/>
            <ul class="buttons">
                <li><button type="button" onclick="window.location.href='add'">Kunden hinzufügen</button></li>
                <li><button type="button" onclick="window.location.href='/../'">Zurück zur Startseite</button></li>
            </ul>
            <ul class="editButtons">
                <li><button type="submit" id="delBut" style="display: none" value="delete">Löschen</button></li>
                <li><button type="button" id="edtBut" style="display: none" onclick="editHref()">Bearbeiten</button></li>
            </ul>
        </form>
    </body>
</html>