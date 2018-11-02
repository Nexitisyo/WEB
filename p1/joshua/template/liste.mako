## coding: utf-8

<table id="idList">
    <tr>
        <th>Name</th>
        <th>Typ</th>
    </tr>

    ## man verwendet hier Zugriff auf das Dictionary "data_o"

% for key_s in data_o:
    <tr id="r${key_s}">
        <td>${data_o[key_s]['name']}</td>
        <td>${data_o[key_s]['typ']}</td>
    </tr>
% endfor
</table>
## Mako-Kommentare verwenden zwei #-Zeichen
