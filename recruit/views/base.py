from django.shortcuts import render
from django.utils import timezone
from datetime import date
import jwt
from config.settings import SECRET_KEY, ALGORITHM


def index(request):
    now_date = timezone.now().date()
    recruit_date = date(2021, 11, 25)
    d_day = (recruit_date - now_date).days
    user_st = 0
    user_st_bit = []

    if d_day == 0 or d_day == -1:
        d_day_color = "text-primary"
        d_day = "-DAY"
        recruit_status = '<span class="text-primary">원서접수가 가능합니다.</span>'
    elif d_day > 0:
        d_day_color = "text-danger"
        d_day = d_day * -1
        recruit_status = '<span class="text-danger">접수가능한 날짜가 아닙니다.</span>'
    else:
        d_day_color = "text-success"
        d_day = "+" + str((d_day + 1) * -1)
        recruit_status = '<span class="text-danger">접수가 종료되었습니다.</span>'

    user_st, user_st_bit = verifyToken(request.COOKIES.get('USER_JWT'))

    return render(request, 'index.html',
                  {'d_day_color': d_day_color, 'd_day': d_day, 'recruit_status': recruit_status, 'user_st': user_st,
                   'user_st_bit': user_st_bit})


def recruit(request):
    now_date = timezone.now().date()
    recruit_date = date(2021, 11, 25)
    d_day = (recruit_date - now_date).days

    if d_day == 0 or d_day == -1:
        recruit_available = True
    else:
        recruit_available = False

    return render(request, 'recruit.html', {'navbar': 'recruit', 'recruit_available': recruit_available})


def confirm(request):
    return render(request, 'confirm.html', {'navbar': 'confirm'})


def docs(request):
    return render(request, 'docs.html', {'navbar': 'docs'})


def status(request):
    return render(request, 'status.html', {'navbar': 'status'})


def healthCheck(request):
    return render(request, 'healthcheck.html')


def verifyToken(token):
    verify_token = validateToken(token)
    user_st = 0
    user_st_bit = []

    if verify_token is None:
        user_st = 0
    else:
        user_st = verify_token['user_st']
        user_st_bit = makeBit(user_st)

    return user_st, user_st_bit


def validateToken(token):
    try:
        verity_token = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    else:
        return verity_token


def makeBit(user_st):
    user_st_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = user_st
    t = []
    j = 1
    while n != 0:
        t.append(n % 2)
        n = n // 2

    for i in range(len(t) - 1, -1, -1):
        user_st_arr[j] = t[i]
        j += 1

    return user_st_arr
