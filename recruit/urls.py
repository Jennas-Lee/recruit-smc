from django.urls import path

from recruit.views import index, form_info

urlpatterns = [
    path('', index, name='recruit-index'),
    path('receive/', form_info, name='recruit-form-info')
]
