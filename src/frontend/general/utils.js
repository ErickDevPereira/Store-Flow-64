function go_to(path) {
    window.location.href = path //path must be the path to a HTML document.
}

export function getData() {
    const query_params = new URLSearchParams(window.location.search);
    return {
        store_id: query_params.get("store_id"),
        company_name: query_params.get("company_name"),
        reg_date: query_params.get("reg_date"),
        category_qtt: query_params.get("category_qtt"),
        customer_qtt: query_params.get("customer_qtt"),
        employees_qtt: query_params.get("employees_qtt"),
        product_qtt: query_params.get("product_qtt"),
        supplier_qtt: query_params.get("supplier_qtt")
    }
}

function transportWithData(basePath) {

    const data = getData();
    const fullPath = basePath + `?store_id=${data["store_id"]}
&company_name=${encodeURIComponent(data["company_name"])}
&reg_date=${data["reg_date"]}
&category_qtt=${data["category_qtt"]}
&customer_qtt=${data["customer_qtt"]}
&employees_qtt=${data["employees_qtt"]}
&product_qtt=${data["product_qtt"]}
&supplier_qtt=${data["supplier_qtt"]}`;
    window.location.href = fullPath;
}

/*The file has export, so we must use type = "module" inside the
<script> tag, however it will mess with the onclick attribute. To 
correct this for the functions that will be aligned to onclick, 
we must do window.function_name = function_name;, unlocking its 
use for onclick.
*/
window.transportWithData = transportWithData;
window.go_to = go_to;