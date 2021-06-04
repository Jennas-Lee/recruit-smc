import bcrypt
from django import forms
from django.views.generic import View, FormView
from django.shortcuts import render
from recruit.models import TcrUserTb


class SigninForm(forms.Form):
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'signin-id-input',
                'placeholder': '아이디'
            }
        ),
        required=False
    )
    user_password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'signin-password-input',
                'placeholder': '비밀번호'
            }
        ),
        required=False
    )
    authorize = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'id': 'authorize-value'
            }
        )
    )

    def clean(self):
        user_id = self.cleaned_data['user_id']
        user_password = self.cleaned_data['user_password']

        if len(user_id) == 0:
            self.add_error('user_id', forms.ValidationError('아이디를 입력하세요.'))
            self.fields['user_id'].widget.attrs['class'] += ' is-invalid'
        elif TcrUserTb.objects.filter(USER_ID_TXT=user_id).count() == 0:
            self.add_error('user_id', forms.ValidationError('아이디를 찾을 수 없습니다.'))
            self.fields['user_id'].widget.attrs['class'] += ' is-invalid'
        else:
            pass

        if len(user_password) == 0:
            self.add_error('user_password', forms.ValidationError('비밀번호를 입력하세요.'))
            self.fields['user_password'].widget.attrs['class'] += ' is-invalid'
        else:
            hashed_password = TcrUserTb.objects.get(USER_ID_TXT=user_id).USER_PASSWORD_TXT
            if bcrypt.checkpw(user_password.encode('UTF-8'), hashed_password.encode('UTF-8')):
                if TcrUserTb.objects.get(USER_ID_TXT=user_id).USER_ST == -1:
                    self.fields['authorize'].widget.attrs['value'] = '-1'
                else:
                    pass
            else:
                self.add_error('user_password', forms.ValidationError('비밀번호가 잘못되었습니다.'))
                self.fields['user_password'].widget.attrs['class'] += ' is-invalid'


class SigninFormView(FormView):
    form_class = SigninForm
    template_name = 'teacher/signin.html'
    success_url = '/healthcheck/'

    def form_valid(self, form):
        self.request.set_cookie
        return super(SigninFormView, self).form_valid(form)


class SigninView(View):
    def get(self, request):
        return render(request, 'teacher/signin.html')

    # def post(self, request):
