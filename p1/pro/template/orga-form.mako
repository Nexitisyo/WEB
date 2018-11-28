## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    ##<meta http-equiv="refresh" content="1">
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head><body>

<form action="save" method="post">
<table class="collapse">
    <tr>
        <th>Projektbezeichnung</th>
        <th>Mitarbeiter</th>
        <th>Aufwand einteilen</th>
        <th>Aktion</th>
    </tr>
    
    <tr>
            <td><p>${projekte['bezeichnung']}</p>
            </td>

            <td>
                %for mitarbeiter in orga['mitarbeiter']:
                    <p>${mitarbeiter}</p>
                 %endfor
            </td>

<<<<<<< HEAD
                    <td>
                        %for mitarbeiter in orga['mitarbeiter']:
                            <p>
                            <ul>
                                <input type="number"
                                    id="aufwandGeteilt"
                                    name="aufwandGeteilt"
                                    min="1" 
                                    size="40" 
                                    value="${projekte['aufwandMax'][0]}"
                                    max="${orga['aufwandMax'][0]}">
=======
             <td>
                %for aufwandGeteilt in orga['aufwandGeteilt']:
                    <p><input type="text"
                        %if action is not UNDEFINED:
                            value="${aufwandGeteilt}"
                        %else:
                            value=""
                        %endif
                            id="bezeichnung"
                            name="bezeichnung"/>
>>>>>>> 367b5187891e4af449608c7fc9bd2ce128f40b15
                            </p>
                %endfor
            </td>


<<<<<<< HEAD
    <input type="hidden" value="1337" name="key" />
=======
    <td>
>>>>>>> 367b5187891e4af449608c7fc9bd2ce128f40b15
    <ul class="buttons">
        <input type="submit" value="Speichern" />
        <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
    </ul>
    </td>   
    </tr>

       </table>


##        <input type="hidden" value="${orga['projektnummer']}" name="projektnummer" />
##    <input type="hidden" value="${orga['bezeichnung']}" name="bezeichnung" />
##    <input type="hidden" value="${orga['mitarbeiter']}" name="mitarbeiter" />
##    <input type="hidden" value="${orga['id']}" name="key" />
</form>
</body>
</html>