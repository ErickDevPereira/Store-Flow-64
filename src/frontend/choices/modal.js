function enableModal() {
    const modal = document.getElementById("modal-cont");
    const others = document.querySelectorAll("body > main")[0];
    others.style.opacity = "0.2";
    others.inert = true;
    others.style.filter = "blur(2px)";
    modal.style.display = "block";
}

function disableModal() {
    const modal = document.getElementById("modal-cont");
    const others = document.querySelectorAll("body > main")[0];
    others.style.opacity = "1.0";
    others.inert = false;
    others.style.filter = "blur(0px)";
    modal.style.display = "none";
}