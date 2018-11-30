## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head>
<body>

<table class="collapse">
<tr>
        <th>Projektbezeichnung</th>
        ##Name,Vorname lexikographisch sortiert
        <th>Projektmitarbeiter</th> 
        <th>Aufwand insgesammt</th> 
    </tr>

    % for projekte in liste:
        <tr>
            <td>${projekte['bezeichnung']}</td>
            <td>
                %for mitarbeiterverweis in projekte['mitarbeiterverweis']:
                    <p>${mitarbeiterverweis}</p>
                %endfor
            </td>
            <td>${projekte['aufwandMax']}</td>
        </tr>
    % endfor

</table>
<ul>
    <li><a href="/../">Zurück zur Startseite</a></li>
</ul>
</body>
</html>