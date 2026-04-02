export function loadSingleStore(company_name, date) {
    const placement = document.getElementById("stores-place");
    const store$div = document.createElement("div");
    store$div.className = "store";
    const date_parts = date.split("-");
    const clean_date = date_parts[2] + '/' + date_parts[1] + '/' + date_parts[0];
    store$div.innerHTML = `<h2>${company_name}</h2>
                            <hr>
                            <p>Registration date: ${clean_date}</p>`;
    placement.append(store$div); //Inserting the element inside the frontend.
}