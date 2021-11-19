from django.urls import path

from score.views import score_index, score_student_list, score_set_neis_number, score_set_docu_integrated, \
    score_set_docu_plan, score_set_interview, score_set_addition, download_excel

urlpatterns = [
    path('', score_index, name='score-index'),
    path('student/list/', score_student_list, name='score-student-list'),
    path('student/set/neis/<int:id>', score_set_neis_number, name='score-set-neis-number'),
    path('student/set/docu_integrated/<int:id>', score_set_docu_integrated, name='score-set-docu-integrated'),
    path('student/set/docu_plan/<int:id>', score_set_docu_plan, name='score-set-docu-plan'),
    path('student/set/interview/<int:id>', score_set_interview, name='score-set-interview'),
    path('student/set/addition/<int:id>', score_set_addition, name='score-set-addition'),
    path('download/', download_excel, name='score-download-excel'),
]
