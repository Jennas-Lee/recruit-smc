from django.shortcuts import render
from django.core.paginator import Paginator

from recruit.models import Student, Document
from score.models import Score

def score_index(request):
    return render(request, 'score_index.html')


def score_student_list(request):
    page = request.GET.get('page', 1)

    page_obj = Student.objects.all().select_related(Document).select_related(Score)

    return render(request, 'score_student_list.html')


def score_neis_number(request):
    return render(request, 'score_')
