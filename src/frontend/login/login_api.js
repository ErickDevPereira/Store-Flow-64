export function startUserSession(email, password, ip, base_path = `http://127.0.0.1:5000/login`) {
    const msgDiv = document.getElementById("err-msg");
    const stdMsg = document.querySelectorAll("#err-msg > p")[0]; //Getting the area where the error text will be
    let status;
    fetch(base_path, 
        {method: "POST",
        credentials: "include",
        body: JSON.stringify(
            {"ip": ip, 
            "email": email,
            "password": password}),
        headers : {"Content-Type": "application/json"}})
    .then(resp => {
        status = resp.status;
        return resp.json();
    })
    .then(data => {
        if (status === 200) {
            window.location.href = "../choices/index.html"; //User has logged into his/her account
        } else {
            msgDiv.style.display = "block";
            stdMsg.innerText = data["message"];
        }
    })
    .catch(err => {
        msgDiv.style.display = "block";
        stdMsg.innerText = String(err);
        console.log("ERROR NÉ PAEE")
    })
}