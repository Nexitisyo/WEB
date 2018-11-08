## coding: utf-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Projekte</title>
    %if action is not UNDEFINED:
        <title>Projekt bearbeiten</title>
    %else:
        <title>Projekt hinzufügen</title>
    %endif
    <link rel="stylesheet" type="text/css" href="/../style.css">
</head><body>

<form action="save" method="post">
<table class="collapse">
    <tr>
        <th>Projekt</th>
        <th>Mitarbeiter</th>
        <th>Aufwand</th>
    </tr>

    % for projekte in liste:
        <tr>
            %for orga in liste3:
            
            %if orga['id'] == projekte['id']:
         
            <td>${orga['id']}  </td>
            <td>
            %if type(orga['mitarbeiter']) is list:
                %for mitarbeiter in orga['mitarbeiter']:
                   <p>${mitarbeiter}</p>
                %endfor
            %else:
               ## ${orga['aufwand'][]}
                <p>${orga['mitarbeiter']}</p>
            %endif
            </td>

            <td>
            %if type(orga['mitarbeiter']) is list:
                %for mitarbeiter in orga['mitarbeiter']:
                <p><input type="number"
                     id="aufwand"
                     name="aufwand"
                     min="1" size="40" max="${orga['aufwand']}"></p>
                %endfor

            %else:
                <p><input type="number" 
                    id="aufwand"
                    name="aufwand"
                    min="1" size="40" max="${orga['aufwand']}"></p>                
            %endif 
                 von ${orga['aufwand']}</td>

        </tr>
        % endif
        % endfor
    % endfor
   </table>

        ## <input type="hidden" value="${orga['projektnummer']}" name="projektnummer" />
        ## <input type="hidden" value="${orga['bezeichnung']}" name="bezeichnung" />
        ## <input type="hidden" value="${orga['mitarbeiter']}" name="mitarbeiter" />
        <input type="hidden" value="1337" name="key" />
       

                <ul class="buttons">
                <input type="submit" value="Speichern" />
                <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
                </ul>
</form>
</body>
</html>