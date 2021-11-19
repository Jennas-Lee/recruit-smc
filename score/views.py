import re

from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from django.utils.timezone import now

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


def score_set_docu_integrated(request, id):
    if request.method == 'GET':
        student = Student.objects.filter(pk=id).select_related('document').select_related('score').last()

        return render(request, 'score_set_docu_integrated.html', {'student': student})

    elif request.method == 'POST':
        student = Student.objects.filter(pk=id).select_related('document').select_related('score').last()
        response_text = ""

        if student:
            if student.score.score_1:
                response_text = "이미 자기소개서 채점이 완료된 학생입니다."
            else:
                docu_integrated = request.POST.get('docu_integrated')
                page = request.GET.get('page')

                try:
                    if re.match('^[0-9]{1,2}$', docu_integrated) is None:
                        response_text = "자기소개서 점수 형식이 올바르지 않습니다."
                    else:
                        student.score.score_1 = int(docu_integrated)
                        student.score.score_1_created_at = now()
                        student.save()

                        return HttpResponse("""
                                <script>
                                    alert('자기소개서 채점이 완료되었습니다.');
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


def score_set_docu_plan(request, id):
    if request.method == 'GET':
        student = Student.objects.filter(pk=id).select_related('document').select_related('score').last()

        return render(request, 'score_set_docu_plan.html', {'student': student})

    elif request.method == 'POST':
        student = Student.objects.filter(pk=id).select_related('document').select_related('score').last()
        response_text = ""

        if student:
            if student.score.score_2:
                response_text = "이미 학업계획서 채점이 완료된 학생입니다."
            else:
                docu_plan = request.POST.get('docu_plan')
                page = request.GET.get('page')

                try:
                    if re.match('^[0-9]{1,2}$', docu_plan) is None:
                        response_text = "학업계획서 점수 형식이 올바르지 않습니다."
                    else:
                        student.score.score_2 = int(docu_plan)
                        student.score.score_2_created_at = now()
                        student.save()

                        return HttpResponse("""
                                <script>
                                    alert('학업계획서 채점이 완료되었습니다.');
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


def score_set_interview(request, id):
    if request.method == 'GET':
        student = Student.objects.filter(pk=id).select_related('document').select_related('score').last()

        return render(request, 'score_set_interview.html', {'student': student})

    elif request.method == 'POST':
        student = Student.objects.filter(pk=id).select_related('document').select_related('score').last()
        response_text = ""

        if student:
            if student.score.score_2:
                response_text = "이미 심층면접 채점이 완료된 학생입니다."
            else:
                interview = request.POST.get('interview')
                page = request.GET.get('page')

                try:
                    if re.match('^[0-9]{1,2}$', interview) is None:
                        response_text = "심층면접 점수 형식이 올바르지 않습니다."
                    else:
                        student.score.score_3 = int(interview)
                        student.score.score_3_created_at = now()
                        student.save()

                        return HttpResponse("""
                                <script>
                                    alert('심층면접 채점이 완료되었습니다.');
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
