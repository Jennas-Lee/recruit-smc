from django.shortcuts import render
from django.utils import timezone

start_timestamp = 1637625600
end_timestamp = 1637740800
now_timestamp = timezone.now().timestamp()

if start_timestamp < now_timestamp < end_timestamp:
    recruit_available = True
else:
    recruit_available = False

# TODO: Update recruit_available
recruit_available = True


def index(request):
    return render(request, 'recruit_index.html', {'recruit_available': recruit_available})


def form_info(request):
    if request.method == 'GET':
        return render(request, 'recruit_form_info.html', {'recruit_available': recruit_available})
