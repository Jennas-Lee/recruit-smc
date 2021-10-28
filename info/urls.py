from django.urls import path

from info.views import info

urlpatterns = [
    path('', info, name='info'),
]
