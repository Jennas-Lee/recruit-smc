from django.shortcuts import render, redirect

from recruit.models import Student


def check_index(request):
    if request.method == 'GET':
        return render(request, 'check_index.html')

    elif request.method == 'POST':
        name = request.POST.get('name')
        tel_st = request.POST.get('tel_st')
        password = request.POST.get('password')

        response_data = {
            'name': name,
            'tel_st': tel_st,
            'password': password,
            'error_messages': False
        }

        student = Student.objects.filter(name=name, tel_st=tel_st, password=password).last()

        if student is None:
            response_data['error_messages'] = True

            return render(request, 'check_index.html', response_data)

        else:
            request.session['tel_st'] = tel_st

            return redirect('/check/status/')


def check_status(request):
    if request.session.get('tel_st') and Student.objects.filter(tel_st=request.session.get('tel_st')).count():
        student = Student.objects.filter(tel_st=request.session.get('tel_st')).select_related('document').last()

        if student.document is None:
            return redirect('/recruit/documents/')

        else:
            response_data = {
                'name': student.name,
                'neis_number': student.neis_number,
                'first_major': student.first_major,
                'second_major': student.second_major,
                'school': student.school,
                'grade': student.grade,
                'class_': student.Class,
                'number': student.number,
                'tel_st': student.tel_st,
                'tel_pa': student.tel_pa,
                'docu_integrated': student.document.docu_integrated,
                'interview': student.document.interview,
                'cert_online': student.document.cert_online,
                'cert_offline': student.document.cert_offline,
                'cert_contest': student.document.cert_contest,
            }

            del request.session['tel_st']
            request.session.modified = True

            return render(request, 'check_status.html', response_data)
    else:
        return redirect('/check/')
