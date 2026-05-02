function callInnerModal(classModalPosition = 0) {
    const modal = document.getElementsByClassName("inner-modal")[classModalPosition];
    const main = document.querySelectorAll("main")[0];
    modal.style.opacity = 1;
    modal.inert = false;
    main.inert = true;
    main.style.filter = "blur(2px)"; /* filter: blur(xpx); will create a blur effect on the element and its children, the greater the x, greater will be the blur effect*/
}

function closeInnerModal(classModalPosition = 0) {
    const modal = document.getElementsByClassName("inner-modal")[classModalPosition];
    const main = document.querySelectorAll("main")[0];
    modal.style.opacity = 0;
    modal.inert = true;
    main.inert = false;
    main.style.filter = "blur(0px)";
}