from django.shortcuts import render
from django.utils import timezone
from datetime import date


def recruit(request):
    now_date = timezone.now().date()
    recruit_date = date(2021, 11, 25)
    d_day = (recruit_date - now_date).days

    if d_day == 0 or d_day == -1:
        recruit_available = True
    else:
        recruit_available = False

    return render(request, 'recruit.old.html', {'navbar': 'recruit.old', 'recruit_available': recruit_available})
