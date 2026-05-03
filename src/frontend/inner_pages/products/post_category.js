export default function postCategory(basePath, catJSON, fieldToFill) {
    fetch(
        basePath,
        {
            credentials: "include",
            method: "POST",
            body: JSON.stringify(catJSON),
            headers: {"Content-Type": "application/json"}
        }
    ).then(resp => {
        if (resp.status === 401) {
            window.location.href = "../../login/index.html"; //Redirecting the user to the outside when the cooke or jwt has been expired.
        }
        return resp.json();
    }).then(json => {
        fieldToFill.innerText = json["message"];//message is an attribute of the upcoming JSON.
    }).catch(err => {
        console.log(err);
    })
}