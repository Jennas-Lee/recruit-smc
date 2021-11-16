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

const createSpinner = () => {
    const spinner = document.createElement('div');
    const hidden = document.createElement('span');

    spinner.setAttribute('id', 'spinner');
    spinner.setAttribute('class', 'spinner-border spinner-border-sm');
    spinner.setAttribute('role', 'status');
    hidden.setAttribute('class', 'visually-hidden');
    hidden.innerText = 'Loading...';

    spinner.appendChild(hidden);

    return spinner;
}

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

    document.getElementById('document-submit').appendChild(createSpinner());

    let form_data = new FormData();
    let xhr = new XMLHttpRequest();
    let interview_files = document.getElementById('inputInterview').files;

    form_data.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken').item(0).value);
    form_data.append('docu_integrated', document.getElementById('inputDocuIntegrated').files[0]);
    form_data.append('cert_online', document.getElementById('inputCertOnline').files[0]);
    form_data.append('cert_offline', document.getElementById('inputCertOffline').files[0]);
    form_data.append('cert_contest', document.getElementById('inputCertContest').files[0]);
    form_data.append('cert_license', document.getElementById('inputCertLicense').files[0]);

    for (let i = 0; i < interview_files.length; i++) {
        form_data.append('interview', interview_files[i]);
    }

    xhr.onreadystatechange = () => {
        if (xhr.readyState === xhr.DONE) {
            if (xhr.status === 200) {
                alert('원서접수에 성공했습니다. 감사합니다.');
                location.href = '/';
            } else if (xhr.status === 400) {
                createAlert(JSON.parse(xhr.responseText)['error_messages']);
                document.getElementById('spinner').remove();
            } else {
                // 서버 실패
                console.log(xhr.status);
                alert('오류가 발생했습니다. 다시 시도해주세요. 이 알림이 계속되면 교무실로 연락주세요.');
                document.getElementById('spinner').remove();
            }
        }
    }

    xhr.open('POST', url, true);
    xhr.send(form_data);
});