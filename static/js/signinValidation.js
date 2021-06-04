const signinIdInput = document.getElementById('signin-id-input');
const signinPasswordInput = document.getElementById('signin-password-input');

signinIdInput.onfocus = () => {
    signinIdInput.classList.remove('is-invalid');
}

signinPasswordInput.onfocus = () => {
    signinPasswordInput.classList.remove('is-invalid');
}

const csrftoken = getCookie('csrftoken');

document.getElementById('signin-form').addEventListener('submit', (event) => {
    let data = {
        'user_id': signinIdInput.value,
        'user_password': signinPasswordInput.value,
    }

    event.preventDefault();

    fetch('/teacher/signin/', {
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
            if (data['user_authorize'] === -1) {
                alert('관리자가 아직 승인하지 않았습니다.');
                location.href = '/';
            } else if (data['user_authorize'] === -2) {
                alert('관리자가 승인을 거부했습니다.');
                location.href = '/';
            } else {    // TODO: Create Success Authorize Logic

            }
        })
        .catch((error) => {
            alert('문제가 발생했습니다. 잠시후에 다시 시도해주세요. 이 문구가 계속되면 관리자에게 연락해주세요.');
        })

});