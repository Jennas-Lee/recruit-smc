from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render
from recruit.models import TcrUserTb
import re
import json
import bcrypt


class SignupView(View):
    def get(self, request):
        return render(request, 'teacher/signup.html')

    def post(self, request):
        request_data = json.loads(request.body)
        user_id_re = re.compile("""^[A-Za-z0-9]{6,15}$""")
        user_password_re = re.compile("""^.*(?=^.{8,15}$)(?=.*\d)(?!.*\s)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$""")
        response_code = 400
        response_data = {}

        if request_data.get('user_id') == '':
            response_code = 200
            response_data['user_id'] = '아이디를 입력하세요.'
        elif len(request_data.get('user_id')) < 6 or len(request_data.get('user_id')) > 15:
            response_code = 200
            response_data['user_id'] = '아이디는 6자 이상 15자 이하로 입력해주세요.'
        elif user_id_re.match(request_data.get('user_id')) is None:
            response_code = 200
            response_data['user_id'] = '아이디는 알파벳 대소문자와 숫자만 사용가능합니다.'
        elif TcrUserTb.objects.filter(USER_ID_TXT=request_data.get('user_id')).count() > 0:
            response_code = 200
            response_data['user_id'] = '이미 사용중인 아이디입니다.'
        else:  # TODO: Deny duplicate user_id
            response_code = 200

        if request_data.get('user_password') == '':
            response_code = 200
            response_data['user_password'] = '비밀번호를 입력해주세요.'
        elif len(request_data.get('user_password')) < 8 or len(request_data.get('user_password')) > 20:
            response_code = 200
            response_data['user_password'] = '비밀번호는 8자 이상 20자 이하로 입력해주세요.'
        elif user_password_re.match(request_data.get('user_password')) is None:
            response_code = 200
            response_data['user_password'] = '비밀번호는 알파벳 대소문자와 숫자, 특수문자(!, @, #, $, %, ^, &, +, =)를 반드시 포함해야합니다.'
        else:
            response_code = 200

        if request_data.get('user_password_confirm') == '':
            response_code = 200
            response_data['user_password_confirm'] = '비밀번호를 한번 더 입력해주세요.'
        elif request_data.get('user_password_confirm') != request_data.get('user_password'):
            response_code = 200
            response_data['user_password_confirm'] = '비밀번호가 일치하지 않습니다.'
        else:
            response_code = 200

        if request_data.get('user_name') == '':
            response_code = 200
            response_data['user_name'] = '이름을 입력해주세요.'
        elif len(request_data.get('user_name')) < 2 or len(request_data.get('user_name')) > 5:
            response_code = 200
            response_data['user_name'] = '이름은 2자 이상 5자 이하로 입력할 수 있습니다.'
        elif ' ' in request_data.get('user_name'):
            response_code = 200
            response_data['user_name'] = '이름에는 공백을 포함할 수 없습니다.'
        else:
            response_code = 200

        if request_data.get('user_team') == '0':
            response_code = 200
            response_data['user_team'] = '부서를 선택해주세요.'
        elif int(request_data.get('user_team')) < 1 or int(request_data.get('user_team')) > 13:
            response_code = 200
            response_data['user_team'] = '부서를 찾을 수 없습니다. 다시 선택해주세요.'
        else:
            response_code = 200

        if len(response_data) == 0:
            user_id = request_data.get('user_id')
            user_password = request_data.get('user_password')
            user_name = request_data.get('user_name')
            user_team = int(request_data.get('user_team'))

            hashed_password = bcrypt.hashpw(user_password.encode('UTF-8'), bcrypt.gensalt())

            try:
                TcrUserTb.objects.create(USER_ID_TXT=user_id, USER_PASSWORD_TXT=hashed_password.decode('UTF-8'),
                                         USER_NM=user_name, USER_TEAM_CD=user_team, USER_ST=-1)
                response_data['success'] = 1
            except (Exception,):
                response_data['success'] = -1

        return JsonResponse(response_data, status=response_code)
