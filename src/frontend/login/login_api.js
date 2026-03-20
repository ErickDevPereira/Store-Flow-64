export function startUserSession(email, password, base_path = `http://127.0.0.1:5000/user`) {
    const msgDiv = document.getElementById("err-msg");
    const stdMsg = document.querySelectorAll("#err-msg > p")[0]; //Getting the area where the error text will be
    let status;
    fetch(base_path + `?email=${email}&password=${password}`, {method: "GET"})
    .then(resp => {
        status = resp.status;
        return resp.json();
    })
    .then(data => {
        if (status === 200) {
            console.log("To be redirected in the future");
        } else {
            msgDiv.style.display = "block";
            stdMsg.innerText = data["message"];
        }
    })
    .catch(err => {
        msgDiv.style.display = "block";
        stdMsg.innerText = String(err);
    })
}