from django.shortcuts import render, HttpResponse
from django.utils import timezone
from datetime import date


def recruit_time():
    start_timestamp = 1637625600
    end_timestamp = 1637741100
    now_timestamp = timezone.now().timestamp()

    if now_timestamp > end_timestamp:
        recruit_available = 2
    elif start_timestamp < now_timestamp < end_timestamp:
        recruit_available = 1
    else:
        recruit_available = 0

    return recruit_available


def index(request):
    now_date = timezone.now().date()
    recruit_date = date(2021, 11, 23)
    d_day = (recruit_date - now_date).days

    if recruit_time() == 0:
        d_day_color = "text-danger"
        recruit_status = 0
    elif recruit_time() == 1:
        d_day_color = "text-primary"
        recruit_status = 1
    elif recruit_time() == 2:
        d_day_color = "text-success"
        recruit_status = 2
    else:
        pass

    if d_day == 0 or d_day == -1:
        d_day = "-DAY"
    elif d_day > 0:
        d_day = d_day * -1
    else:
        d_day = "+" + str((d_day + 1) * -1)

    return render(request, 'index.html',
                  {'navbar': 'index', 'd_day_color': d_day_color, 'd_day': d_day, 'recruit_status': recruit_status})


def healthcheck(request):
    return HttpResponse(status=200)
