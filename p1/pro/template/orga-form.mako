## coding: utf-8
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head>
<body>

<form action="save" method="post">
    <table class="collapse">
        <tr>
            <th>Projektbezeichnung</th>
            <th>Mitarbeiter</th>
            <th>Aufwand einteilen</th>
            <th>Aktion</th>
        </tr>
        <tr>
            <td><p>${projekte['bezeichnung']}</p></td>
            <td>
                %for mitarbeiter in orga['mitarbeiter']:
                    <p>${mitarbeiter}</p>
                    %endfor
            </td>
            <td>
                %for aufwandGeteilt in orga['aufwandGeteilt']:
                    <p><input type="text"
                            value="${aufwandGeteilt}"
                            id="aufwandGeteilt"
                            name="aufwandGeteilt"/>
                    </p>
                %endfor
            </td>
            <td>
                <ul class="buttons">
                    <input type="submit" value="Speichern" />
                    <input type="button" value="Abbrechen" onclick="location.href='/projekte/'"/>
                </ul>
            </td>   
        </tr>
    </table>


    <input type="hidden" value="${orga['bezeichnung']}" name="bezeichnung" id="bezeichnung" />
    <input type="hidden" value="${orga['mitarbeiter']}" name="mitarbeiter" id="mitarbeiter" />
    <input type="hidden" value="${orga['id']}" name="key" id="key" />

</form>
</body>
</html>