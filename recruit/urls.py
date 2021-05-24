from django.contrib import admin
from django.urls import path
from recruit.views import base
from recruit.views.teacher import signin, signup

urlpatterns = [
    path('', base.index, name='index'),
    path('index/', base.index, name='index'),
    path('recruit/', base.recruit, name='recruit'),
    path('confirm/', base.confirm, name='confirm'),
    path('docs/', base.docs, name='docs'),
    path('status/', base.status, name='status'),

    path('teacher/signin/', signin.SigninFormView.as_view(), name='teacher-signin'),
    path('teacher/signup/', signup.SignupFormView.as_view(), name='teacher-signup'),

    path('healthcheck/', base.healthCheck, name='health-check'),
    path('admin/', admin.site.urls),
]
