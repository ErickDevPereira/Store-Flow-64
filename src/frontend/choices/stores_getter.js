import { load_stores_divs } from "./load_stores_divs.js";

export function get_stores() {
    const PATH = "http://127.0.0.1:5000/store";
    let ok = false;
    let JSON;
    fetch(PATH, {credentials: "include", method: "GET"}) //credentials as 'include' will allow the frontend to send back the cookies to the backend
    .then(resp => {
        if (resp.status === 200) {
            ok = true; //Everything went fine and the JSON with the stores was sent to the frontend
        } else {
            window.location.href = "../login/index.html"; //Redirect back to the login area when the status is other than 200, like 401 (Unauthorized)
        }
        return resp.json(); //The stores are inside this JSON.
    })
    .then(data =>
        {
            if (ok) {
                JSON = data;
                load_stores_divs(JSON); //Loading the data that came from the server over the divs.
            }
        }
    )
    .catch(err => {
            window.location.href = "../login/index.html";
            console.log(err);
        }
    )
}//Detail: I've implemented httponly = True in Flask, so the JS won't be able to read the cookies, but will be able to send it back to the server.