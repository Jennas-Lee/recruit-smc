from django.urls import path

from check.views import check_index, check_status

urlpatterns = [
    path('', check_index, name='check-index'),
    path('status/', check_status, name='check-status')
]
