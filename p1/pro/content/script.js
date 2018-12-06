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

    var curCol =(colorToHex(document.getElementById(id).style.backgroundColor));

    if(curCol == stdCol){
        document.getElementById(id).classList.add("selected");
        idList.push(id);
        document.getElementById("inputID").value = [idList];
        document.getElementById(id).style.backgroundColor = mrkCol;
        selNum++;
        document.getElementById("delBut").style.display = "";
        if(selNum == 1) {
            document.getElementById("edtBut").style.display ="";
        }
        else {
            document.getElementById("edtBut").style.display ="none";
        }
    }

    else {
        document.getElementById(id).classList.remove("selected");
        idList.pop(id);
        document.getElementById("inputID").value = [idList];
        document.getElementById(id).style.backgroundColor = stdCol;
        selNum--;

        if(selNum == 0){
            document.getElementById("delBut").style.display = "none";
        }
        if(selNum == 1) {
            document.getElementById("edtBut").style.display ="";
        }
        else {
            document.getElementById("edtBut").style.display ="none";
        }
    }
}

function editHref() {
    window.location.href = 'edit?key=' + idList[0];
}