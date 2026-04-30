const opt = document.getElementById("hamburguer-opt");
if (window.innerWidth < 750) {
    opt.style.display = "none";
}

function viewOpt() {
    const opt_status = opt.style.display;
    if (opt_status === "none") {
        opt.style.display = "flex";
        opt.style.flexDirection =  "column";
    } else if (opt_status === "flex") {
        opt.style.display = "none";
    }
}

function correctDisplayBug() {
    if (window.innerWidth < 750) {
        opt.style.display = "none";
    } else {
        opt.style.display = "flex";
        opt.style.flexDirection =  "row";
    }
}