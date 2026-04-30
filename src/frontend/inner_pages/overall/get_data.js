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