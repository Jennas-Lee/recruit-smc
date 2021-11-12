from django.shortcuts import render, redirect

from recruit.models import Student, Document


def check_index(request):
    if request.method == 'GET':
        if request.session.get('tel_st') and Student.objects.filter(tel_st=request.session.get('tel_st')).count():
            return redirect('/check/status/')
        else:
            return render(request, 'check_index.html')


def check_status(request):
    if request.session.get('tel_st') and Student.objects.filter(tel_st=request.session.get('tel_st')).count():
        student = Student.objects.filter(tel_st=request.session.get('tel_st')).last()
        document = Document.objects.filter(student_id=student).last()

        response_data = {
            'name': student.name,
            'school': student.school,
            'grade': student.grade,
            'class_': student._class,
            'number': student.number,
            'tel_st': student.tel_st,
            'tel_pa': student.tel_pa,
            'docu_integrated': document.docu_integrated,
            'cert_online': document.cert_online,
            'cert_offline': document.cert_offline,
            'cert_license': document.cert_license,
        }

        return render(request, 'check_status.html', response_data)
    else:
        return redirect('/check/')
