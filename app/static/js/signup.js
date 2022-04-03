const signUp = async (e) => {
    e.preventDefault();
    const usernameInput = document.querySelector('#usernameInputSignUp').value.trim();
    const passwordInput = document.querySelector('#passwordInputSignUp').value.trim();

    if (usernameInput && passwordInput) {
        const response = await fetch('/api/users/signup', {
            method: 'POST',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify({ user: usernameInput, password: passwordInput })
        })
        if (response.ok) {
            document.location.replace('/dashboard')
        } else {
            console.log(response)
            alert('Unable to create an account')
        }
    } else {
        alert('you MUST enter both a username AND a password')
    }
};

document.querySelector('#signupButton').addEventListener('click', signUp)