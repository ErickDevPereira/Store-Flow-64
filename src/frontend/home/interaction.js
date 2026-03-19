const menu = document.getElementById("hamburger-but");
const opts = document.getElementById("options");

let show_menu = false;

menu.onclick = function() {
    if (!show_menu) {
        opts.style.display = "block";
    } else {
        opts.style.display = "none";
    }
    show_menu = !show_menu;
}

function correctTogleMenuBug() {
    if (window.innerWidth > 430 && opts.style.display === "none") {
        opts.style.display = "block";
    }
    if (window.innerWidth < 430 && opts.style.display === "block") {
        opts.style.display = "none";
    }
}