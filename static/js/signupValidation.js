const submitButton = document.getElementById('signup-btn');
const submitButtonSpinner = document.getElementById('signup-btn-spinner');
const signupIdInput = document.getElementById('signup-id-input');
const signupPasswordInput = document.getElementById('signup-password-input');
const signupPasswordConfirmInput = document.getElementById('signup-password-confirm-input');
const signupNameInput = document.getElementById('signup-name-input');
const signupTeamInput = document.getElementById('signup-team-input');

const signupInputFocus = (tag) => {
    tag.classList.remove('is-invalid');
}

submitButton.onclick = () => {

    submitButton.classList.add('disabled');
    submitButtonSpinner.classList.remove('visually-hidden');
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