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
        <form method="post" action="delete">
            <table class="collapse">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Vorname</th>
                    <th>Funktion</th>
                </tr>
                % for mitarbeiter in liste:
                <tr class="" id="${mitarbeiter['id']}" ondblclick="selectionMarker(${mitarbeiter['id']})" style="background-color: #333333">
                        <td>${mitarbeiter['id']}</td>
                        <td>${mitarbeiter['name']}</td>
                        <td>${mitarbeiter['vorname']}</td>
                        <td>${mitarbeiter['funktion']}</td>
                </tr>
                % endfor
            </table>
            <input type="hidden" id="inputID" name="key" value=""/>
            <ul class="buttons">
                <li><button type="button" onclick="window.location.href='add'">Mitarbeiter hinzufügen</button></li>
                <li><button type="button" onclick="window.location.href='/../'">Zurück zur Startseite</button></li>
            </ul>
            <ul class="editButtons">
                <li><button type="submit" id="delBut" style="display: none" value="delete">Löschen</button></li>
                <li><button type="button" id="edtBut" style="display: none" onclick="editHref()">Bearbeiten</button></li>
            </ul>
        </form>
    </body>
</html>