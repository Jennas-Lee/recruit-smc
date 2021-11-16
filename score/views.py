from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

from authentication.models import User
from recruit.models import Student


def score_index(request):
    apply_user_count = User.objects.filter(permission=0).count()

    return render(request, 'score_index.html', {'apply_user_count': apply_user_count})


def score_student_list(request):
    page = request.GET.get('page', 1)

    student = Student.objects.select_related('document').select_related('score').order_by('pk')
    paginator = Paginator(student, 15)
    page_obj = paginator.get_page(page)
    previous = page_obj.previous_page_number if page_obj.has_previous() else 1
    next = page_obj.next_page_number if page_obj.has_next() else page_obj.paginator.num_pages

    return render(request, 'score_student_list.html', {'page_obj': page_obj, 'previous': previous, 'next': next})


def score_set_neis_number(request, id):
    if request.method == 'GET':
        student = Student.objects.filter(pk=id).last()
        # student.

        return render(request, 'score_set_neis_number.html', {'student': student})

    elif request.method == 'POST':
        student = Student.objects.filter(pk=id).last()
        response_text = ""

        if student:
            if student.neis_number:
                response_text = "이미 수험번호가 할당된 학생입니다."
            else:
                neis_number = request.POST.get('neis_number')
                page = request.GET.get('page')

                if Student.objects.filter(neis_number=neis_number).count() > 0:
                    response_text = "이미 해당 수험번호가 할당된 학생이 있습니다."
                else:
                    try:
                        student.neis_number = neis_number
                        student.save()

                        return HttpResponse("""
                                <script>
                                    alert('수험번호 할당에 성공했습니다.');
                                    location.href = '/score/student/list/?page=""" + page + """';
                                </script>
                            """)
                    except:
                        response_text = "오류가 발생했습니다. 이 오류가 지속되면 개발자에게 연락주세요."
        else:
            response_text = "존재하지 않는 학생입니다."

        return HttpResponse("""
                                <script>
                                    alert('""" + response_text + """');
                                    location.href = document.referrer;
                                </script>
                            """)
