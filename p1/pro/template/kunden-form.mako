## coding: utf-8
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        %if action is not UNDEFINED:
            <title>Kunden bearbeiten</title>
        %else:
            <title>Kunden hinzufügen</title>
        %endif
        <link rel="stylesheet" type="text/css" href="/../style.css">
    </head>
    <body>

        <form action="save" method="post">
            <table class="collapse">
                <tr>
                    <th><label for="kundennummer">Kundennummer:</label></th>
                    <th><label for="bezeichnung">Bezeichnung:</label></th>
                    <th><label for="ansprechpartner">Ansprechpartner:</label></th>
                    <th><label for="ort">Ort:</label></th> 
                    <th>Aktion:</th>
                </tr>
    ########################################################################################################################                
                <tr>
                    <td>
                        <input type="text"
                                %if action is not UNDEFINED: 
                                    value="${kunden['kundennummer']}"
                                %else:
                                    value=""
                                %endif
                                    id="kundennummer"
                                    name="kundennummer"/>
                    </td>
            ########################################################################################################################                
                    <td>
                        <input type="text"
                                %if action is not UNDEFINED:
                                    value="${kunden['bezeichnung']}"
                                %else:
                                    value=""
                                %endif
                                    id="bezeichnung" name="bezeichnung"/>
                    </td>
            ########################################################################################################################                
                    <td>
                        <input type="text"
                                %if action is not UNDEFINED:
                                    value="${kunden['ansprechpartner']}"
                                %else:
                                    value=""
                                %endif
                                    id="ansprechpartner" name="ansprechpartner"/>
                    </td>
            ########################################################################################################################                
                    <td>
                        <input type="text"
                                %if action is not UNDEFINED:
                                    value="${kunden['ort']}"
                                %else:
                                    value=""
                                %endif
                                    id="ort" name="ort"/>
                    </td>

                    <td>
                        <input type="submit" value="Speichern"/>
                        <input type="button" value="Abbrechen" onclick="location.href='/kunden/';"/>
                    </td>
                </tr>
            </table>
            %if action is not UNDEFINED:
            <input type="hidden" value="${kunden['id']}" name="key"/>
            %endif
        </form>
    </body>
</html>