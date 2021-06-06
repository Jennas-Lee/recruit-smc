from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render
from datetime import datetime, timedelta
from recruit.models import TcrUserTb
from config.settings import SECRET_KEY, ALGORITHM
import json
import bcrypt
import jwt


class SigninView(View):
    def get(self, request):
        return render(request, 'teacher/signin.html')

    def post(self, request):
        request_data = json.loads(request.body)
        response_code = 400
        response_data = {}

        if request_data.get('user_id') == '':
            response_code = 200
            response_data['user_id'] = '아이디를 입력하세요.'
        elif TcrUserTb.objects.filter(USER_ID_TXT=request_data.get('user_id')).count() == 0:
            response_code = 200
            response_data['user_id'] = '아이디를 찾을 수 없습니다.'
        else:
            response_code = 200

        if request_data.get('user_password') == '':
            response_code = 200
            response_data['user_password'] = '비밀번호를 입력해주세요.'
        else:
            try:
                user_object = TcrUserTb.objects.get(USER_ID_TXT=request_data.get('user_id'))
                hashed_password = user_object.USER_PASSWORD_TXT
                user_authorize = user_object.USER_ST
                if bcrypt.checkpw(request_data.get('user_password').encode('UTF-8'), hashed_password.encode('UTF-8')):
                    response_data['user_authorize'] = user_authorize
                    if user_authorize >= 0:
                        jwt_data = {'user_id': user_object.USER_ID_TXT, 'user_name': user_object.USER_NM,
                                    'user_st': user_object.USER_ST, 'exp': datetime.utcnow() + timedelta(hours=15)}
                        token = jwt.encode(jwt_data, SECRET_KEY, ALGORITHM)
                        response_data['user_jwt'] = token
                else:
                    response_data['user_password'] = '비밀번호가 잘못되었습니다'
                response_code = 200
            except Exception as e:
                response_data['success'] = -1

        return JsonResponse(response_data, status=response_code)
