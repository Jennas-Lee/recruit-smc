from django import forms
from django.shortcuts import render
from django.views.generic import View, FormView


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

    def clean(self):
        user_id = self.cleaned_data['user_id']
        user_password = self.cleaned_data['user_password']

        if len(user_id) == 0:
            self.add_error('user_id', forms.ValidationError('아이디를 입력하세요.'))


class Login(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()

        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        return 'TEST'


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/healthcheck/'

    def form_valid(self, form):
        return super(LoginFormView, self).form_valid(form)
