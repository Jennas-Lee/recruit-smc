const submitButton = document.getElementById('signin-btn');
const submitButtonSpinner = document.getElementById('signin-btn-spinner');
const signinIdInput = document.getElementById('signin-id-input');
const signinPasswordInput = document.getElementById('signin-password-input');

submitButton.onclick = () => {

    submitButton.classList.add('disabled');
    submitButtonSpinner.classList.remove('visually-hidden');
}

signinIdInput.onfocus = () => {
    signinIdInput.classList.remove('is-invalid');
}

signinPasswordInput.onfocus = () => {
    signinPasswordInput.classList.remove('is-invalid');
}