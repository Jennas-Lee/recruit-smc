const loginValidation = () => {
    let idInput = document.getElementById('login-id-input');
    let passwordInput = document.getElementById('login-id-password');
    let idFeedback = document.getElementById('login-id-validation-feedback');
    let passwordFeedback = document.getElementById('login-password-validation-feedback')
    let submitButton = document.getElementById('login-btn');
    let submitButtonSpinner = document.getElementById('login-btn-spinner');

    submitButton.classList.add('disabled');
    submitButtonSpinner.classList.remove('visually-hidden');

    if(idInput.value.length === 0) {
        idInput.classList.add('is-invalid');
        idFeedback.textContent = '아이디를 입력하세요.';
        return false;
    }

    // const xhr = new XMLHttpRequest();
    // xhr.open('POST', '');

    return false;
};