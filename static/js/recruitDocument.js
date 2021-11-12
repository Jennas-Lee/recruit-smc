let student_info = document.getElementById('student-info');

setInterval(() => {
    if (student_info.classList.contains('text-danger')) {
        student_info.classList.replace('text-danger', 'text-primary');
    } else {
        student_info.classList.replace('text-primary', 'text-danger');
    }
    setTimeout(() => {
    }, 500);
}, 1000);

const createAlert = (message) => {
    const alert = document.createElement('div');
    const closeBtn = document.createElement('button');

    closeBtn.setAttribute('type', 'button');
    closeBtn.setAttribute('class', 'btn-close');
    closeBtn.setAttribute('data-bs-dismiss', 'alert');
    closeBtn.setAttribute('aria-label', 'Close');

    alert.setAttribute('class', 'alert alert-danger alert-dismissible fade show');
    alert.setAttribute('role', 'alert');
    alert.innerText = message;
    alert.appendChild(closeBtn);

    document.getElementById('alert').appendChild(alert);
}

document.getElementById('recruit-documents-form').addEventListener('submit', (event) => {
    event.preventDefault();

    let form_data = new FormData();
    let xhr = new XMLHttpRequest();

    form_data.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken').item(0).value)
    form_data.append('docu_integrated', document.getElementById('inputDocuIntegrated').files[0]);
    form_data.append('cert_online', document.getElementById('inputCertOnline').files[0]);
    form_data.append('cert_offline', document.getElementById('inputCertOffline').files[0]);
    form_data.append('cert_license', document.getElementById('inputCertLicense').files[0]);

    xhr.onreadystatechange = () => {
        if (xhr.readyState === xhr.DONE) {
            if (xhr.status === 200) {
                alert('원서접수에 성공했습니다. 감사합니다.');
                location.href = '/';
            } else if (xhr.status === 400) {
                createAlert(JSON.parse(xhr.responseText)['error_messages']);
            } else {
                // 서버 실패
                console.log(xhr.status);
                alert('오류가 발생했습니다. 다시 시도해주세요. 이 알림이 계속되면 교무실로 연락주세요.');
            }
        }
    }

    xhr.open('POST', url, true);
    xhr.send(form_data);
});