const submitButton = document.getElementById('signup-btn');
const submitButtonSpinner = document.getElementById('signup-btn-spinner');
const signupIdInput = document.getElementById('signup-id-input');
const signupPasswordInput = document.getElementById('signup-password-input');
const signupPasswordConfirmInput = document.getElementById('signup-confirm-password-input');
const signupNameInput = document.getElementById('signup-name-input');
const signupTeamInput = document.getElementById('signup-team-input');

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfSafeMethod = (method) => {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

const csrftoken = getCookie('csrftoken');

const signupInputFocus = (tag) => {
    tag.classList.remove('is-invalid');
}

signupIdInput.oninput = () => {
    signupInputFocus(signupIdInput);
}

signupPasswordInput.oninput = () => {
    signupInputFocus(signupPasswordInput);
}

signupPasswordConfirmInput.oninput = () => {
    signupInputFocus(signupPasswordConfirmInput);
}

signupNameInput.oninput = () => {
    signupInputFocus(signupNameInput);
}

signupTeamInput.oninput = () => {
    signupInputFocus(signupTeamInput);
}

submitButton.onclick = () => {

    // submitButton.classList.add('disabled');
    // submitButtonSpinner.classList.remove('visually-hidden');
}

document.getElementById('signup-form').addEventListener('submit', (event) => {
    submitButton.classList.add('disabled');
    submitButtonSpinner.classList.remove('visually-hidden');

    let data = {
        'user_id': signupIdInput.value,
        'user_password': signupPasswordInput.value,
        'user_password_confirm': signupPasswordConfirmInput.value,
        'user_name': signupNameInput.value,
        'user_team': signupTeamInput.value
    }

    event.preventDefault();
    fetch('/teacher/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
        .then((response) => {
            response.status
        })
});