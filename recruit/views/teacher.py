from django import forms
from django.shortcuts import render
from django.views.generic import View


class LoginForm(forms.Form):
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디'
            }
        )
    )

    user_password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호'
            }
        )
    )


class Login(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()

        return render(request, 'login.html', {'form': form})

    def post(self, request):
        return 'POST TEST'
