const submitButton = document.getElementById('signup-btn');
const submitButtonSpinner = document.getElementById('signup-btn-spinner');
const signupIdInput = document.getElementById('signup-id-input');
const signupPasswordInput = document.getElementById('signup-password-input');
const signupPasswordConfirmInput = document.getElementById('signup-confirm-password-input');
const signupNameInput = document.getElementById('signup-name-input');
const signupTeamInput = document.getElementById('signup-team-input');

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

const printValidateError = (inputId, validateId, errorText) => {
    document.getElementById(inputId).classList.add('is-invalid');
    document.getElementById(validateId).innerText = errorText;
    submitButton.classList.remove('disabled');
    submitButtonSpinner.classList.add('visually-hidden');
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
        .then((response) => response.json())
        .then((data) => {
            if (data['user_id'] !== undefined) {
                printValidateError('signup-id-input', 'signup-id-validation-feedback', data['user_id']);
            }
            if (data['user_password'] !== undefined) {
                printValidateError('signup-password-input', 'signup-password-validation-feedback', data['user_password']);
            }
            if (data['user_password_confirm'] !== undefined) {
                printValidateError('signup-confirm-password-input', 'signup-confirm-password-validation-feedback', data['user_password_confirm']);
            }
            if (data['user_name'] !== undefined) {
                printValidateError('signup-name-input', 'signup-name-validation-feedback', data['user_name']);
            }
            if (data['user_team'] !== undefined) {
                printValidateError('signup-team-input', 'signup-team-validation-feedback', data['user_team']);
            }
            if (data['success'] === 1) {
                alert('가입이 완료되었습니다. 관리자 승인 후 로그인할 수 있습니다.');
                location.href = '/';
            }
            if (data['success'] === -1) {
                new Error('Server Error');
            }
        })
        .catch((error) => {
            alert('문제가 발생했습니다. 잠시후에 다시 시도해주세요. 이 문구가 계속되면 관리자에게 연락해주세요.');
            submitButton.classList.remove('disabled');
            submitButtonSpinner.classList.add('visually-hidden');
        });
});