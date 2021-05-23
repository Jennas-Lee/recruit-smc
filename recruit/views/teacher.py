from django import forms
from django.shortcuts import render
from django.views.generic import View


class LoginForm(forms.Form):
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'login-id-input',
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
                'id': 'login-password-input',
                'placeholder': '비밀번호'
            }
        ),
        required=False
    )


class Login(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()

        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        return 'TEST'
