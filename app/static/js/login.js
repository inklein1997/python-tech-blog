const logIn = async (e) => {
    e.preventDefault();
    const usernameInput = document.querySelector('#usernameInputSignIn').value.trim();
    const passwordInput = document.querySelector('#passwordInputSignIn').value.trim();

    if (usernameInput && passwordInput) {
        const response = await fetch('/api/users/login', {
            method: 'POST',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify({ user: usernameInput, password: passwordInput })
        })
        if (response.ok) {
            document.location.replace('/dashboard')
        } else {
            console.log(response)
            alert('unable to log into account')
        }
    } else {
        alert('you MUST enter both a username AND a password')
    }
};

document.querySelector('#loginButton').addEventListener('click', logIn)