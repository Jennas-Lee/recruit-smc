from django.urls import path

from recruit.views import index

urlpatterns = [
    path('', index, name='recruit-index'),
]
