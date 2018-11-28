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
                            <ul>
                            
                            <p>
                                <input type="number"
                                    id="aufwandGeteilt"
                                    name="aufwandGeteilt"
                                    min="1" 
                                    size="40" 
                                    value=""
                                    max="${orga['aufwandMax']}">
                            </p>
                        %endfor    
        
                        von ${orga['aufwandMax']}
                    </td>
                % endif
            % endfor
        </tr>
    % endfor
   </table>
   <input type="hidden" value="${orga['projektnummer']}" name="projektnummer" />
   <input type="hidden" value="${orga['bezeichnung']}" name="bezeichnung" />
   <input type="hidden" value="${orga['mitarbeiter']}" name="mitarbeiter" />
   <input type="hidden" value="${projekte['id']}" name="key" />
   
    <ul class="buttons">
        <input type="submit" value="Speichern" />
        <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
    </ul>
</form>
</body>
</html>