from django.shortcuts import render
from django.utils import timezone
from datetime import date


def auth(request):
    return render(request, 'auth.html')


def confirm(request):
    return render(request, 'confirm.html', {'navbar': 'confirm'})


def docs(request):
    return render(request, 'docs.html', {'navbar': 'docs'})


def status(request):
    return render(request, 'status.html', {'navbar': 'status'})
