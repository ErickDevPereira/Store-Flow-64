import {createNewStore} from "./new_store.js";
import { disableModal, enableModal } from "./modal.js";

const form = document.getElementById("new-store-form");
form.addEventListener('submit', evt => {
    evt.preventDefault();
    const company_name = document.getElementById("icompany").value;
    createNewStore("http://127.0.0.1:5000/store", company_name);
})

const adder = document.getElementById("adder");
adder.addEventListener("click", evt => {
    enableModal();
    }
);

const exit = document.getElementById("close");
exit.addEventListener("click", evt => {
    disableModal();
    }
);