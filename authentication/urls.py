from django.urls import path

from authentication.views import signup, signin, signout, teacher_list, teacher_info, teacher_apply_list, \
    teacher_deny_list

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('list/', teacher_list, name='teacher-list'),
    path('info/<int:id>', teacher_info, name='teacher-info'),
    path('list/apply/', teacher_apply_list, name='teacher-apply-list'),
    path('list/deny/', teacher_deny_list, name='teacher-deny-list'),
]
