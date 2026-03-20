export function createUser(fname, lname, email, password, birthdate, path = "http://127.0.0.1:5000/user") {
    fetch(path, {
        method: "POST",
        body: JSON.stringify({
            "first_name": fname,
            "last_name": lname,
            "password": password,
            "email": email,
            "birthdate": birthdate
        }),
        headers: {"Content-Type": "application/json"}
        })
    .then(resp => {
        const fadingDiv = document.getElementById("fading-msg");
        const stdMsg = document.querySelector("#fading-msg p");
        const status = resp.status;
        fadingDiv.style.display = "block";
        switch (status) {
            case 201:
                stdMsg.innerText = "Now, you are one of us";
                break;
            case 400:
                stdMsg.innerText = "All fields must be filed";
                break;
            case 403:
                stdMsg.innerText = "This email already exists.";
                break;
            case 500:
                stdMsg.innerText = "Something went wrong on the server side. Try later.";
                break;
        }
    })
    .catch(err => console.log(err));
}