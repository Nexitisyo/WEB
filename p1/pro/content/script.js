var stdCol = "#333333";
var mrkCol = "#b32626";
var selNum = 0;
var idList = [];

function colorToHex(color) {
    if (color.substr(0, 1) === '#') {
        return color;
    }
    var digits = /(.*?)rgb\((\d+), (\d+), (\d+)\)/.exec(color);
    
    var red = parseInt(digits[2]);
    var green = parseInt(digits[3]);
    var blue = parseInt(digits[4]);
    
    var rgb = blue | (green << 8) | (red << 16);
    return digits[1] + '#' + rgb.toString(16).padStart(6, '0');
};

function selectionMarker(id) {
    var elementWithID = document.getElementById(id)
    var curCol = colorToHex(elementWithID.style.backgroundColor);

    if(curCol == stdCol){
        idList.push(id);
        document.getElementById("inputID").value = idList; //[idList]

        elementWithID.style.backgroundColor = mrkCol;
        selNum++;
        document.getElementById("delBut").style.display = "";
        if(selNum == 1) {
            document.getElementById("edtBut").style.display = "";
            document.getElementById("orgBut").style.display = "";
        }
        else {
            document.getElementById("edtBut").style.display = "none";
            document.getElementById("orgBut").style.display = "none";
        }
    }
    else {
        idList.pop(id);
        document.getElementById("inputID").value = [idList];
        elementWithID.style.backgroundColor = stdCol;
        selNum--;

        if(selNum == 0){
            document.getElementById("delBut").style.display = "none";
        }

        if(selNum == 1) {
            document.getElementById("edtBut").style.display = "";
            document.getElementById("orgBut").style.display = "";
        }
        
        else {
            document.getElementById("edtBut").style.display = "none";
            document.getElementById("orgBut").style.display = "none";

        }
    }
}

function editHref() {
    window.location.href = 'edit?key=' + idList[0];
}

function orgaHref() {
    window.location.href = '/../orga/edit?key=' + idList[0];
}