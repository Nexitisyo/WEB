function selectionMarker(id) {
    document.getElementById(id).style.backgroundColor = "#b3262667";
    //document.getElementById(id).style.color = "#cecece";
}

function deselectionMarker(id) {
    document.getElementById(id).style.backgroundColor = "#333333";
    //document.getElementById(id).style.color = "#cecece";

}

function editPy(id) {
    window.location.href = 'edit?key=' + id;
}