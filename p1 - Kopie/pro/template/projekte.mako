## coding: utf-8
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Projekte</title>
        <link rel="stylesheet" type="text/css" href="/../style.css">
        <script src="/../script.js"></script>
    </head>
    <body>
        <form method="post" action="delete">
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
                    <th>Aufwand insgesammt</th>
                </tr>
                % for projekte in liste:
                <tr class="" id="${projekte['id']}" ondblclick="selectionMarker(${projekte['id']})" style="background-color: #333333">
                    <td>${projekte['id']}</td>
                    <td>${projekte['projektnummer']}</td>
                    <td>${projekte['bezeichnung']}</td>
                    <td>${projekte['beschreibung']}</td>
                    <td>${projekte['bearbeitungszeitraumA']} - <br>${projekte['bearbeitungszeitraumB']}</td>
                    <td>${projekte['budget']}</td>
                    <td>${projekte['kundenverweis']}</td>
                    <td>                
                        %for mitarbeiterverweis in projekte['mitarbeiterverweis']:
                            <p>${mitarbeiterverweis}</p>
                        %endfor
                    </td>
                    <td>${projekte['aufwandMax']}</td>
                </tr>
                % endfor
            </table>
            <input type="hidden" id="inputID" name="key" value=""/>
            <ul class="buttons">
                <li><button type="button" onclick="window.location.href='add'">Projekt hinzufügen</button></li>
                <li><button type="button" onclick="window.location.href='/../'">Zurück zur Startseite</button></li>
            </ul>
            <ul class="editButtons">
                <li><button type="submit" id="delBut" style="display: none" value="delete">Löschen</button></li>
                <li><button type="button" id="edtBut" style="display: none" onclick="editHref()">Bearbeiten</button></li>
                <li><button type="button" id="orgBut" style="display: none" onclick="orgaHref()">Aufwand einteilen</button></li>

            </ul>
        </form>
    </body>
</html>