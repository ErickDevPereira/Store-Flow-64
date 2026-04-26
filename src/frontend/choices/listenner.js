import {createNewStore} from "./new_store.js";
import {disableModal, enableModal} from "./modal.js";
import {selectStore} from "./select_store.js";

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

const store = document.getElementById("stores-place");
store.addEventListener("click", evt => {
    const identifier = evt.target.id;
    if (identifier !== "shop-img") {
            const path = "http://127.0.0.1:5000";
            selectStore(path, identifier);
        }
    }
)