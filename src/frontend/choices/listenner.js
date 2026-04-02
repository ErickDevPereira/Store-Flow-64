import {createNewStore} from "./new_store.js";

const form = document.getElementById("new-store-form");
form.addEventListener('submit', evt => {
    evt.preventDefault();
    console.log(1);
    const company_name = document.getElementById("icompany").value;
    createNewStore("http://127.0.0.1:5000/store", company_name);
})