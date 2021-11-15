from django.urls import path

from score.views import score_index, score_student_list, score_set_neis_number

urlpatterns = [
    path('', score_index, name='score-index'),
    path('student/list/', score_student_list, name='score-student-list'),
    path('student/set/neis/<int:id>', score_set_neis_number, name='score-set-neis-number'),
]
