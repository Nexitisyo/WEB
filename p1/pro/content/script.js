console.log("Hello World")

var collapseMarker = document.getElementsByClassName("collapse");
function selectionMarker(id) {
    document.getElementById(id).style.backgroundColor = "#b32626";
    document.getElementById(id).style.color = "#ececec";

}
function deselectionMarker(id) {
    document.getElementById(id).style.backgroundColor = "#ececec";
    document.getElementById(id).style.color = "#444141";

}