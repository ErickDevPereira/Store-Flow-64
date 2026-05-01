function callInnerModal() {
    const modal = document.getElementById("inner-modal");
    const main = document.querySelectorAll("main")[0];
    modal.style.opacity = 1;
    modal.inert = false;
    main.inert = true;
}

function closeInnerModal() {
    const modal = document.getElementById("inner-modal");
    const main = document.querySelectorAll("main")[0];
    modal.style.opacity = 0;
    modal.inert = true;
    main.inert = false;
}