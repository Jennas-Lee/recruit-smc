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
                // 성공
            } else {
                console.log(xhr.status);
                alert('오류가 발생했습니다. 다시 시도해주세요. 이 알림이 계속되면 교무실로 연락주세요.');
            }
        }
    }

    xhr.open('POST', url, true);
    xhr.send(form_data);
});