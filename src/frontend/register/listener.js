
import {createUser} from "./api_post.js";

document.querySelectorAll("form")[0]
.addEventListener("submit", event => {
    event.preventDefault();//Won't allow the page to reload itself and will allow JS to run smoothly.
    const f_name = document.getElementById("ifname").value;
    const l_name = document.getElementById("ilname").value;
    const email = document.getElementById("iemail").value;
    const password = document.getElementById("ipw").value;
    const birthdate = document.getElementById("ibtd").value;
    createUser(f_name, l_name, email, password, birthdate);
});