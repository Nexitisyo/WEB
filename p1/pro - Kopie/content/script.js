function selectionMarker(id) {
    document.getElementById(id).style.backgroundColor = "#b3262667";
}

function deselectionMarker(id) {
    document.getElementById(id).style.backgroundColor = "#333333";
}

function editPy(id) {
    window.location.href = 'edit?key=' + id;
}