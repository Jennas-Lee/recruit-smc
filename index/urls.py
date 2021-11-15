from django.urls import path

from index.views import index, healthcheck

urlpatterns = [
    path('', index, name='index'),
    path('healthcheck/', healthcheck, name='healthcheck'),
]
