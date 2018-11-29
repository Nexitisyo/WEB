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
        <th>Projekt</th>
        <th>Mitarbeiter</th>
        <th>Aufwand einteilen</th>
    </tr>

    % for projekte in liste:
        <tr>
            %for orga in liste3:
                %if orga['id'] == projekte['id']:
                    <td>ID: ${orga['id']}<br>${orga['bezeichnung']}  </td>
                    <td>
                        %for mitarbeiter in orga['mitarbeiter']:
                            <p>${mitarbeiter}</p>
                        %endfor
                    </td>

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
                            </p>
                        %endfor    
        
                        von ${orga['aufwandMax']}
                    </td>
                % endif
            % endfor
        </tr>
    % endfor
   </table>

    <input type="hidden" value="1337" name="key" />
    <ul class="buttons">
        <input type="submit" value="Speichern" />
        <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
    </ul>
</form>
</body>
</html>