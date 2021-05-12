from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def recruit(request):
    return render(request, 'recruit.html', {'navbar': 'recruit'})


def confirm(request):
    return render(request, 'confirm.html', {'navbar': 'confirm'})


def status(request):
    return render(request, 'status.html', {'navbar': 'status'})
