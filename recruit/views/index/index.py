from django.shortcuts import render
from django.utils import timezone
from datetime import date


def index(request):
    now_date = timezone.now().date()
    recruit_date = date(2021, 11, 23)
    d_day = (recruit_date - now_date).days

    if d_day == 0 or d_day == -1:
        d_day_color = "text-primary"
        d_day = "-DAY"
        recruit_status = 1
    elif d_day > 0:
        d_day_color = "text-danger"
        d_day = d_day * -1
        recruit_status = 0
    else:
        d_day_color = "text-success"
        d_day = "+" + str((d_day + 1) * -1)
        recruit_status = 2

    return render(request, 'index.html', {'navbar': 'index', 'd_day_color': d_day_color, 'd_day': d_day, 'recruit_status': recruit_status})
