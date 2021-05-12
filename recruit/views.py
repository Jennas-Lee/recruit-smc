from django.shortcuts import render
from django.utils import timezone
from datetime import date


def index(request):
    now_date = timezone.now()
    recruit_date = timezone.make_aware(date(2021, 11, 25))  # TODO: Check Timezone
    d_day = recruit_date-now_date
    d_day_color = "text-primary"
    return render(request, 'index.html', {'d_day_color': d_day_color, 'd_day': d_day})


def recruit(request):
    return render(request, 'recruit.html', {'navbar': 'recruit'})


def confirm(request):
    return render(request, 'confirm.html', {'navbar': 'confirm'})


def docs(request):
    return render(request, 'docs.html', {'navbar': 'docs'})


def status(request):
    return render(request, 'status.html', {'navbar': 'status'})
