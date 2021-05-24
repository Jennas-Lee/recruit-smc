from django.contrib import admin
from django.urls import path
from recruit.views import base, teacher

urlpatterns = [
    path('', base.index, name='index'),
    path('index/', base.index, name='index'),
    path('recruit/', base.recruit, name='recruit'),
    path('confirm/', base.confirm, name='confirm'),
    path('docs/', base.docs, name='docs'),
    path('status/', base.status, name='status'),

    # path('teacher/login/', teacher.Login.as_view(), name='teacher-login'),
    path('teacher/login/', teacher.LoginFormView.as_view(), name='teacher-login'),

    path('healthcheck/', base.healthCheck, name='health-check'),
    path('admin/', admin.site.urls),
]
