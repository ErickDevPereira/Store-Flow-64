import {startUserSession} from "./login_api.js";

const form = document.querySelectorAll("form")[0];
form.addEventListener("submit", evt => {
    evt.preventDefault(); 
    const email = document.getElementById("iemail").value;
    const password = document.getElementById("ipw").value;
    startUserSession(email, password);
})