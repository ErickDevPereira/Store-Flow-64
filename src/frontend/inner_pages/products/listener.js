import postCategory from "./post_category.js";
import { getData } from "../../general/utils.js";

const productForm = document.querySelectorAll("form")[0];
const catForm = document.querySelectorAll("form")[1];

const storeId = getData().store_id;

catForm.addEventListener("submit", (evt) => {
    evt.preventDefault();
    const fieldToFill = document.getElementById("info-msg");
    const catName = document.getElementById("ctn").value;
    const description = document.getElementById("cdesc").value;
    postCategory(
        "http://127.0.0.1:5000/store/categories",
        {
            "store-id" : storeId,
            "category-name" : catName,
            "description" : description
        },
        fieldToFill
    );
});