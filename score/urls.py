from django.urls import path

from score.views import score_index, score_student_list

urlpatterns = [
    path('', score_index, name='score-index'),
    path('student/list/', score_student_list, name='score-student-list')
]
