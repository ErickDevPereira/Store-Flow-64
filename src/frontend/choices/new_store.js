import { loadSingleStore } from "./load_single_store.js";
import { disableModal } from "./modal.js";

export function createNewStore(path, company_name) {
    let ok = false;
    fetch(path, {
        credentials: "include",
        method: "POST",
        body: JSON.stringify({"company_name": company_name}),
        headers: {"Content-Type": "application/json"}
        }
    ).then(resp => {
        if (resp.status === 201) {
            ok = !ok;
        } else if (resp.status === 401) { //The cookie has expired, so we move the user back to the login area.
            window.location.href = "../login/index.html";
        }
        return resp.json();
    }
    ).then(data => {
        if (ok) {
            const today = new Date().toISOString().split("T")[0] //Today's date (formated as YYYY-MM-DD)
            loadSingleStore(company_name, today);
            disableModal(); //Exiting the modal
        } else {
            document.getElementById("err-msg").innerText = data["message"];
        }
    }
    ).catch(err => {
        console.log(err);
    })
}