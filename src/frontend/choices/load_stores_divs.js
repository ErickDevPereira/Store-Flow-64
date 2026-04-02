export function load_stores_divs(JSON) {
    const placement = document.getElementById("stores-place");
    const reference = document.getElementById("adder");
    for ( let i = 0; i < JSON['stores'].length; i++ ) {
        const store$div = document.createElement("div");
        store$div.className = "store";
        const date_parts = JSON['stores'][i]['registration_date'].split("-");
        const clean_date = date_parts[2] + '/' + date_parts[1] + '/' + date_parts[0];
        store$div.innerHTML = `<h2>${JSON['stores'][i]['company_name']}</h2>
                                <hr>
                                <p>Registration date: ${clean_date}</p>`;
        placement.insertBefore(store$div, reference); //Inserting the element inside the frontend.
    }
}