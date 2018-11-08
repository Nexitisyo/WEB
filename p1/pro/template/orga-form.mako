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
            <td>${orga['id']}</td>
            <td>
            %if type(orga['mitarbeiter']) is list:
                %for mitarbeiter in orga['mitarbeiter']:
                   <p>${mitarbeiter}</p>
                %endfor
            %else:

                <p>${orga['mitarbeiter']}</p>
            %endif
            </td>

            <td>
            %if type(orga['mitarbeiter']) is list:
                %for mitarbeiter in orga['mitarbeiter']:
                <p><input type="number" name="quantity" min="1" max="${orga['aufwand']}"></p>
                %endfor

            %else:
               <p><input type="number" name="quantity" min="1" size="" max="${orga['aufwand']}"></p>
                
            %endif 
                 von ${orga['aufwand']}</td>

        </tr>
        % endif
        % endfor
    % endfor

##onclick="alert('${mitarbeiter['id']}')"

## <tr>
##             <td><input type="text"
##                 %if action is not UNDEFINED:
##                     value="${projekte['projektnummer']}"
##                 %else:
##                     value=""
##                 %endif
##                     id="projektnummer"
##                     name="projektnummer"/>
##             </td>
## #######################################################################################################################################
##             <td><input type="text"
##                 %if action is not UNDEFINED:
##                     value="${projekte['bezeichnung']}"
##                 %else:
##                     value=""
##                 %endif
##                     id="bezeichnung" name="bezeichnung"/>
##             </td>
## #######################################################################################################################################
##             <td><input type="text"
##                 %if action is not UNDEFINED:
##                     value="${projekte['beschreibung']}"
##                 %else:
##                     value=""
##                 %endif
##                     id="beschreibung" name="beschreibung"/>
##             </td>
            </table>
                            <ul class="buttons">
                <input type="submit" value="Speichern"/>
                <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
                </ul>
</form>
</body>
</html>