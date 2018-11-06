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
<tr>    ##Nach projektbezeichnung sortiert
        <th>Projektbezeichnung</th>
        ##Name,Vorname lexikographisch sortiert
        <th>Projektmitarbeiter</th> 
        <th>Aufwand pro Woche</th> 
    </tr>

    % for projekte in liste:
        <tr>
            <td>${projekte['bezeichnung']}</td>
            <td>${projekte['mitarbeiterverweis']}</td>
            <td>${projekte['aufwand']}</td>
        </tr>
    % endfor

</table>
<p>Zurück zur <a href="/../">Startseite</a></p>
</body>
</html>