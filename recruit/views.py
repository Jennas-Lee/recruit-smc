import re

from django.shortcuts import render, reverse, HttpResponse
from django.utils import timezone

from recruit.models import Student

start_timestamp = 1637625600
end_timestamp = 1637740800
now_timestamp = timezone.now().timestamp()

if start_timestamp < now_timestamp < end_timestamp:
    recruit_available = True
else:
    recruit_available = False

# TODO: Update recruit_available
recruit_available = True


def index(request):
    return render(request, 'recruit_index.html', {'recruit_available': recruit_available})


def form_receive(request):
    if request.method == 'GET':
        return render(request, 'recruit_form_receive.html', {'recruit_available': recruit_available})

    elif request.method == 'POST':
        name = request.POST.get('name')
        school = request.POST.get('school')
        grade = request.POST.get('grade')
        class_ = request.POST.get('class_')
        number = request.POST.get('number')
        tel_st = request.POST.get('tel_st')
        tel_pa = request.POST.get('tel_pa')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        agree = request.POST.get('agree')

        response_data = {
            'name': name,
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

        # School Validation
        if len(school) <= 0:
            response_data['error_messages'].append('학교를 입력하세요.')
        elif len(school) < 4:
            response_data['error_messages'].append('학교 이름을 올바르게 입력하세요.')
        else:
            pass

        # Grade Validation
        if len(grade) <= 0 and school != "검정고시":
            response_data['error_messages'].append('학년을 입력하세요.')
        elif re.match('^\\d$', grade) is None and school != "검정고시":
            print(re.match(grade, '^\\d$'))
            print(grade)
            response_data['error_messages'].append('학년을 올바르게 입력하세요.')
        else:
            pass

        # Class_ Validation
        if len(class_) <= 0 and school != "검정고시":
            response_data['error_messages'].append('반을 입력하세요.')
        elif re.match('^\\d{1,2}$', class_) is None and school != "검정고시":
            response_data['error_messages'].append('반을 올바르게 입력하세요.')
        else:
            pass

        # Number Validation
        if len(number) <= 0 and school != "검정고시":
            response_data['error_messages'].append('번호를 입력하세요.')
        elif re.match('^\\d{1,2}$', number) is None and school != "검정고시":
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
                student = Student(name=name, school=school, grade=grade, _class=class_, number=number, tel_st=tel_st,
                                  tel_pa=tel_pa, password=password)
                student.save()

                request.session['tel_st'] = tel_st

                return reverse('recruit-form-documents')
            except:
                HttpResponse("""
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
        s
