from django.shortcuts import render
from django.utils import timezone
from datetime import date


def index(request):
    now_date = timezone.now().date()
    recruit_date = date(2021, 11, 25)
    d_day = (recruit_date - now_date).days

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

    return render(request, 'index.html', {'d_day_color': d_day_color, 'd_day': d_day, 'recruit_status': recruit_status})


def login(request):
    return render(request, 'auth.html')


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
