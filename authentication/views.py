from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from authentication.models import User

import re


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        name = request.POST.get('name')

        password_re = re.compile("""^.*(?=^.{8,20}$)(?=.*\d)(?!.*\s)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$""")

        alert = ""

        if User.objects.filter(email=email).count() > 0:
            alert = "이미 사용중인 이메일입니다."
        elif password_re.match(password) is None:
            alert = "비밀번호는 반드시 8~20자의 문자와 숫자, 특수문자를 포함해야 합니다."
        elif password != confirm_password:
            alert = "비밀번호가 일치하지 않습니다."
        elif len(name) < 2 or len(name) > 5:
            alert = "이름은 반드시 2~5자 이내로 작성해야 합니다."
        elif ' ' in name:
            alert = "이름은 공백을 포함할 수 없습니다."
        else:
            pass

        if alert:
            return render(request, 'signup.html',
                          {'alert': alert, 'email': email, 'password': password, 'confirm_password': confirm_password,
                           'name': name})
        else:
            try:
                user = User.objects.create_user(email=email, name=name, password=password)
                user.save()

                return HttpResponse("""
                    <script>
                        alert('회원가입이 완료되었습니다. 승인 후 사용가능합니다. 교사가 아니면 승인이 거절당할 수 있습니다.');
                        location.href='/';
                    </script>
                """)

            except Exception as e:
                return render(request, 'signup.html',
                              {'alert': '오류가 발생했습니다. 이 오류가 반복되면 개발자에게 연락주세요.', 'email': email,
                               'password': password, 'confirm_password': confirm_password, 'name': name})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.permission == -1:
                return HttpResponse("""
                    <script>
                        alert('승인이 거절되었습니다.');
                        location.href='/';
                    </script>
                """)
            elif user.permission == 0:
                return HttpResponse("""
                    <script>
                        alert('승인이 완료되지 않았습니다.');
                        location.href='/';
                    </script>
                """)
            else:
                login(request, user)

                return redirect('/')
        else:
            return render(request, 'signin.html',
                          {'alert': '이메일 또는 비밀번호가 잘못되었습니다.', 'email': email, 'password': password})


def signout(request):
    logout(request)

    return redirect('/')
