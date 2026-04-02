export function enableModal() {
    const modal = document.getElementById("modal-cont");
    const others = document.querySelectorAll("body > main")[0];
    others.style.opacity = "0.2";
    others.inert = true;
    others.style.filter = "blur(2px)";
    modal.style.display = "block";
}

export function disableModal() {
    const modal = document.getElementById("modal-cont");
    const others = document.querySelectorAll("body > main")[0];
    const msg = document.getElementById("err-msg");
    const input_txt = document.getElementById("icompany");
    others.style.opacity = "1.0";
    others.inert = false;
    others.style.filter = "blur(0px)";
    modal.style.display = "none";
    msg.innerText = "";
    input_txt.value = ""; //Won't let the previous value remains in the input box.
}