## coding: utf-8
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        %if action is not UNDEFINED:
            <title>Projekt bearbeiten</title>
        %else:
            <title>Projekt hinzufügen</title>
        %endif
        <link rel="stylesheet" type="text/css" href="/../style.css">
    </head>
    <body>
        <form action="save" method="post">
            <table class ="collapse">
                <tr>
                    <th>Projektnummer:</th>
                    <th>Bezeichnung:</th>
                    <th>Beschreibung:</th>
                    <th>Budget:</th>
                    <th>Kundenverweis</th>
                    <th>Mitarbeiterverweis:</th>
                    <th>Max. Aufwand in Tagen:</th>
                    <th>Bearbeitungszeitraum:</th>
                    <th>Aktion:</th>
                </tr>
        #######################################################################################################################################
                <tr>
                    <td>
                        <input type="text"
                            %if action is not UNDEFINED:
                                value="${projekte['projektnummer']}"
                            %else:
                                value=""
                            %endif
                                id="projektnummer"
                                name="projektnummer"/>
                    </td>
        #######################################################################################################################################
                    <td>
                        <input type="text"
                            %if action is not UNDEFINED:
                                value="${projekte['bezeichnung']}"
                            %else:
                                value=""
                            %endif
                                id="bezeichnung" name="bezeichnung"/>
                    </td>
        #######################################################################################################################################
                    <td>
                        <input type="text"
                            %if action is not UNDEFINED:
                                value="${projekte['beschreibung']}"
                            %else:
                                value=""
                            %endif
                                id="beschreibung" name="beschreibung"/>
                    </td>

        #######################################################################################################################################
                    <td>
                        <input type="text"
                            %if action is not UNDEFINED:
                                value="${projekte['budget']}"
                            %else:
                                value=""
                            %endif
                                id="budget" name="budget"/>
                    </td>
        #######################################################################################################################################
                    <td>
                        <input list="kunden" 
                                %if action is not UNDEFINED:
                                    value="${projekte['kundenverweis']}"
                                %else:
                                    value=""
                                %endif
                                    id="kundenverweis" name="kundenverweis">
                                
                        <datalist id="kunden">
                            % for kunden in liste:
                            <option value="${kunden['id']}">${kunden['bezeichnung']}</option>
                            % endfor
                        </datalist> 
                    </td>
        #######################################################################################################################################
                    <td>
                        <select multiple id="mitarbeiterverweis" name="mitarbeiterverweis">
                            % for mitarbeiter in liste2:
                            <option value="${mitarbeiter['name']} ${mitarbeiter['vorname']}">${mitarbeiter['vorname']} ${mitarbeiter['name']}</option> 
                            % endfor    
                        </select>
                    </td> 
        #######################################################################################################################################          
                    <td>
                        <input type="text" disabled
                            %if action is not UNDEFINED:
                                value="${projekte['aufwandMax']}"
                            %else:
                                value=""
                            %endif
                                id="aufwandMax" name="aufwandMax"/>
                    </td>
        #######################################################################################################################################
                    <td>
                        <input type="date"
                            %if action is not UNDEFINED:
                                value="${projekte['bearbeitungszeitraumA']}"
                            %endif
                                id="bearbeitungszeitraumA" name="bearbeitungszeitraumA"/>

                        <input type="date"
                            %if action is not UNDEFINED:
                                value="${projekte['bearbeitungszeitraumB']}"
                            %endif
                                id="bearbeitungszeitraumB" name="bearbeitungszeitraumB"/>
                    </td>
        #######################################################################################################################################
                    <td>
                        <input type="submit" value="Speichern"/>
                        <input type="button" value="Abbrechen" onclick="location.href='/projekte/';"/>
                    </td>
                </tr>
            </table>
            %if action is not UNDEFINED:
            <input type="hidden" value="${projekte['id']}" name="key" />
            %endif  
        </form>
    </body>
</html>