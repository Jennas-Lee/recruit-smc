from django.urls import path

from docs.views import docs

urlpatterns = [
    path('', docs, name='docs'),
]
