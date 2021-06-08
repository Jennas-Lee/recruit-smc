from django.contrib import admin
from django.urls import path
from recruit.views import base
from recruit.views.teacher import signin, signup, signout
from recruit.views.management import teacher

urlpatterns = [
    path('', base.index, name='index'),
    path('index/', base.index, name='index'),
    path('recruit/', base.recruit, name='recruit'),
    path('confirm/', base.confirm, name='confirm'),
    path('docs/', base.docs, name='docs'),
    path('status/', base.status, name='status'),

    path('management/teacher/', teacher.TeacherListView.as_view(), name='management-teacher-list'),
    path('management/teacher/<str:user_id>', teacher.TeacherPersonalManagementView.as_view(),
         name='management-teacher-info'),

    path('teacher/signin/', signin.SigninView.as_view(), name='teacher-signin'),
    path('teacher/signup/', signup.SignupView.as_view(), name='teacher-signup'),
    path('teacher/signout/', signout.signout, name='teacher-signout'),

    path('healthcheck/', base.healthCheck, name='health-check'),
    path('admin/', admin.site.urls),
]
