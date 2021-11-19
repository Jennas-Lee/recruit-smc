import os
import traceback
import re
import boto3

from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from config.settings import AWS_S3_BUCKET, STATIC_CDN_LINK

from recruit.models import Student, Document
from score.models import Score

start_timestamp = 1637625600
end_timestamp = 1637740800
now_timestamp = timezone.now().timestamp()

if start_timestamp < now_timestamp < end_timestamp:
    recruit_available = True
else:
    recruit_available = False

# TODO: Update recruit_available
recruit_available = True


class NotFoundDocuIntegratedException(Exception):
    pass


def index(request):
    return render(request, 'recruit_index.html', {'recruit_available': recruit_available})


def form_receive(request):
    if request.method == 'GET':
        return render(request, 'recruit_form_receive.html', {'recruit_available': recruit_available})

    elif request.method == 'POST':
        name = request.POST.get('name')
        first_major = request.POST.get('first_major')
        second_major = request.POST.get('second_major')
        school = request.POST.get('school')
        grade = request.POST.get('grade', None)
        class_ = request.POST.get('class_', None)
        number = request.POST.get('number', None)
        tel_st = request.POST.get('tel_st')
        tel_pa = request.POST.get('tel_pa')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        agree = request.POST.get('agree')

        response_data = {
            'name': name,
            'first_major': first_major,
            'second_major': second_major,
            'school': school,
            'grade': grade,
            'class_': class_,
            'number': number,
            'tel_st': tel_st,
            'tel_pa': tel_pa,
            'password': password,
            'confirm_password': confirm_password,
            'agree': agree,
            'error_messages': [],
            'recruit_available': recruit_available
        }

        # Name Validation
        if len(name) <= 0:
            response_data['error_messages'].append('이름을 입력하세요.')
        elif 2 > len(name) or len(name) > 5:
            response_data['error_messages'].append('이름은 2자 이상 5자 이하로 입력해야 합니다.')
        else:
            pass

        # First Major Validation
        if int(first_major) == 0:
            response_data['error_messages'].append('1지망 학과를 반드시 선택하세요.')
        elif 0 > int(first_major) or int(first_major) > 5:
            response_data['error_messages'].append('1지망 학과를 올바르게 선택하세요.')
        else:
            pass

        # Second Major Validation
        if -1 > int(second_major) or int(second_major) > 5:
            response_data['error_messages'].append('2지망 학과를 올바르게 선택하세요.')
        elif int(first_major) != 0 and first_major == second_major:
            response_data['error_messages'].append('1지망과 2지망은 같은 학과를 선택할 수 없습니다.')
        else:
            pass

        # School Validation
        if len(school) <= 0:
            response_data['error_messages'].append('학교를 입력하세요.')
        elif len(school) < 4:
            response_data['error_messages'].append('학교 이름을 올바르게 입력하세요.')
        else:
            pass

        # Grade Validation
        if school != "검정고시" and len(grade) <= 0:
            response_data['error_messages'].append('학년을 입력하세요.')
        elif school != "검정고시" and re.match('^\\d$', grade) is None:
            response_data['error_messages'].append('학년을 올바르게 입력하세요.')
        else:
            pass

        # Class_ Validation
        if school != "검정고시" and len(class_) <= 0:
            response_data['error_messages'].append('반을 입력하세요.')
        elif school != "검정고시" and re.match('^[0-9]{1,2}$', class_) is None:
            response_data['error_messages'].append('반을 올바르게 입력하세요.')
        else:
            pass

        # Number Validation
        if school != "검정고시" and len(number) <= 0:
            response_data['error_messages'].append('번호를 입력하세요.')
        elif school != "검정고시" and re.match('^[0-9]{1,2}$', number) is None:
            response_data['error_messages'].append('번호를 올바르게 입력하세요.')
        else:
            pass

        # Tel_st Validation
        if len(tel_st) <= 0:
            response_data['error_messages'].append('학생 전화번호를 입력하세요.')
        elif re.match('^01\\d{8,9}$', tel_st) is None:
            response_data['error_messages'].append('학생 전화번호를 올바르게 입력하세요.')
        elif Student.objects.filter(tel_st=tel_st).count() > 0:
            response_data['error_messages'].append('이미 접수가 진행된 전화번호입니다. 접수 결과를 조회하세요.')
        else:
            pass

        # Tel_pa Validation
        if len(tel_pa) <= 0:
            response_data['error_messages'].append('학부모 전화번호를 입력하세요.')
        elif re.match('^01\\d{8,9}$', tel_pa) is None:
            response_data['error_messages'].append('학부모 전화번호를 올바르게 입력하세요.')
        else:
            pass

        # Password Validation
        if len(password) <= 0:
            response_data['error_messages'].append('비밀번호를 입력하세요.')
        elif re.match('^\\d{4}$', password) is None:
            response_data['error_messages'].append('올바른 비밀번호를 입력하세요. 숫자 4자리를 입력하세요.')
        else:
            pass

        # Confirm_password Validation
        if len(confirm_password) <= 0:
            response_data['error_messages'].append('비밀번호 확인을 입력하세요.')
        elif password != confirm_password:
            response_data['error_messages'].append('비밀번호 확인이 올바르지 않습니다.')
        else:
            pass

        # Agree Validation
        if agree != 'on':
            response_data['error_messages'].append('개인정보 제공에 동의해주세요.')
        else:
            pass

        if response_data['error_messages']:
            return render(request, 'recruit_form_receive.html', response_data)

        else:
            try:
                student = Student(name=name, first_major=first_major, second_major=second_major, school=school,
                                  grade=grade, Class=class_, number=number, tel_st=tel_st, tel_pa=tel_pa,
                                  password=password)
                student.save()

                request.session['tel_st'] = tel_st

                return redirect('/recruit/documents/')

            except:
                return HttpResponse("""
                    <script>
                        alert('오류가 발생했습니다. 다시 시도해주세요. 이 알림이 계속되면 교무실로 연락주세요.');
                        window.history.back();
                    </script>
                """)


def form_documents(request):
    if request.method == 'GET':
        response_data = {
            'recruit_available': recruit_available,
            'name': None,
            'school': None
        }
        if request.session.get('tel_st'):
            student = Student.objects.filter(tel_st=request.session.get('tel_st'))

            if student.count():
                response_data['name'] = student.get().name
                response_data['school'] = student.get().school
            else:
                pass

        else:
            pass

        return render(request, 'recruit_form_documents.html', response_data)

    elif request.method == 'POST':
        response_data = {
            'error_messages': "",
            'status_code': 0
        }

        if request.session.get('tel_st') and Student.objects.filter(tel_st=request.session.get('tel_st')).count():
            student = Student.objects.filter(tel_st=request.session.get('tel_st')).last()
            files_data = {
                'docu_integrated': {
                    'file': request.FILES.get('docu_integrated', None),
                    'name': "[자기소개서 및 학업계획서] " + student.school + " " + student.name
                },
                'cert_online': {
                    'file': request.FILES.get('cert_online', None),
                    'name': "[온라인 SW 아카데미] " + student.school + " " + student.name
                },
                'cert_offline': {
                    'file': request.FILES.get('cert_offline', None),
                    'name': "[수요진로체험] " + student.school + " " + student.name
                },
                'cert_contest': {
                    'file': request.FILES.get('cert_contest', None),
                    'name': "[SW경진대회] " + student.school + " " + student.name
                },
            }
            interview_files = request.FILES.getlist('interview', None)
            url = 'student/' + str(int(now_timestamp)) + '/' + str(student.pk) + '/'

            try:
                document = Document()
                client = boto3.client('s3')

                if len(interview_files) == 0:
                    raise NotFoundDocuIntegratedException

                else:
                    interview_data = {'files': []}
                    for file in interview_files:
                        root, extension = os.path.splitext(file.name)
                        filename = "[심층면접 영상] " + student.school + " " + student.name + "(" + file.name + ")" + extension
                        full_url = url + filename
                        cdn_url = STATIC_CDN_LINK + full_url

                        client.upload_fileobj(
                            file,
                            AWS_S3_BUCKET,
                            full_url,
                            ExtraArgs={
                                "ContentType": file.content_type
                            }
                        )

                        interview_data['files'].append(cdn_url)

                document.interview = interview_data

                for key, values in files_data.items():
                    if key == 'docu_integrated' and values['file'] is None:
                        raise NotFoundDocuIntegratedException

                    else:
                        if values['file']:
                            root, extension = os.path.splitext(values['file'].name)
                            filename = values['name'] + extension
                            full_url = url + filename
                            cdn_url = STATIC_CDN_LINK + full_url

                            client.upload_fileobj(
                                values['file'],
                                AWS_S3_BUCKET,
                                full_url,
                                ExtraArgs={
                                    "ContentType": values['file'].content_type
                                }
                            )

                            if key == 'docu_integrated':
                                document.docu_integrated = cdn_url
                            elif key == 'cert_online':
                                document.cert_online = cdn_url
                            elif key == 'cert_offline':
                                document.cert_offline = cdn_url
                            elif key == 'cert_contest':
                                document.cert_contest = cdn_url

                document.save()
                student.document = document
                score = Score()
                score.save()
                student.score = score
                student.save()

                response_data['status_code'] = 200

                del request.session['tel_st']
                request.session.modified = True

            except NotFoundDocuIntegratedException:
                response_data['error_messages'] = "자기소개서 및 학업계획서, 심층면접 영상을 입력해주세요."
                response_data['status_code'] = 400

            except Exception:
                traceback.print_exc()
                response_data['status_code'] = 500

            finally:
                pass

        else:
            response_data['error_messages'] = "<a href=\"#\" class=\"alert-link\">이곳에서</a> 먼저 접수 확인을 해주시기 바랍니다."
            response_data['status_code'] = 400

        return JsonResponse(response_data, status=response_data['status_code'],
                            json_dumps_params={'ensure_ascii': False})
