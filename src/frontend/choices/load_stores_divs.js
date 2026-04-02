export function load_stores_divs(JSON) {
    const placement = document.getElementById("stores-place");
    const reference = document.getElementById("adder");
    for ( let i = 0; i < JSON['stores'].length; i++ ) {
        const store$div = document.createElement("div");
        store$div.className = "store";
        store$div.innerHTML = `${JSON['stores'][i]['company_name']}
                                <hr>
                                Registration date: ${JSON['stores'][i]['registration_date']}`;
        placement.insertBefore(store$div, reference); //Inserting the element inside the frontend.
    }
}