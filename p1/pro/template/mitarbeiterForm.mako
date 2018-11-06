<html>
<head>
    <link rel="stylesheet" type="text/css" href="/../style.css" />
    <title>Mitarbeiterdaten</title>
    <meta charset="UTF-8">
</head>
<body>
    <h2>Mitarbeiter hinzuf&uuml;gen</h2>

    <form class="entry" action="addEntry" method="post">
    <ul style="list-style-type:none">
    <table>
        <tr>
        <th><label for="name">Name:</label></th>
        <th><label for="vorname">Vorname:</label></th>
        <th><label for="funktion">Funktion:</label></th>
        <th></th>
        </tr>

        <tr>
        <td><input value="" id="name", name="name"></input></td>
        <td><input value="" id="vorname", name="vorname"></input></td>
        <td><input value="" id="funktion", name="funktion"></input></td>
        <td><input type="submit" value="Speichern"/></td>
        </tr>
    </table>
    </ul>
    </form>
    <a href="/mitarbeiter">Zur&uuml;ck</a>
</body>