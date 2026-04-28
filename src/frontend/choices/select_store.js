export function selectStore(basePath, store_id) {
    let status_code;
    fetch(basePath + `/store_bridge?store-id=${store_id}`, {
        method: "GET",
        credentials: "include"
    }).then(resp => {
        status_code = resp.status;
        return resp.json();
    }).then(json => {
        if (status_code === 200) {
            const data = json['data'];
            window.location.href = 
`../overall/index.html?store_id=${data["store_id"]}
&company_name=${encodeURIComponent(data["company_name"])}
&reg_date=${data["reg_date"]}
&category_qtt=${data["category_qtt"]}
&customer_qtt=${data["customer_qtt"]}
&employees_qtt=${data["employees_qtt"]}
&product_qtt=${data["product_qtt"]}
&supplier_qtt=${data["supplier_qtt"]}`;
        } else if (status_code === 401) {
            window.location.href = "../login/index.html"; //jwt or cookie has been expired
        } else {
            console.log(status_code);
        }
    }).catch((err) => {
        console.log(err);
    })
}