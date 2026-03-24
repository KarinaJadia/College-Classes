let user = document.getElementById('user').value;
let pwd = document.getElementById('pwd').value;

usernameInput.addEventListener('input', handleInput);
passwordInput.addEventListener('input', handleInput);

function handleInput() {
    let user = document.getElementById('user').value;
    document.getElementById("result").innerHTML = user;
    return 0;
}

function handleKeyPress(event, functionName) {
    if (event.key === "Enter") {
        window[functionName](); 
        return 0;
    }
}