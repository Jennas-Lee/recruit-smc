from django import forms
from django.views.generic import FormView


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

    def clean(self):
        user_id = self.cleaned_data['user_id']
        user_password = self.cleaned_data['user_password']

        if len(user_id) == 0:
            self.add_error('user_id', forms.ValidationError('아이디를 입력하세요.'))
            self.fields['user_id'].widget.attrs['class'] += ' is-invalid'

        if len(user_password) == 0:
            self.add_error('user_password', forms.ValidationError('비밀번호를 입력하세요.'))
            self.fields['user_password'].widget.attrs['class'] += ' is-invalid'


class SigninFormView(FormView):
    form_class = SigninForm
    template_name = 'teacher/signin.html'
    success_url = '/healthcheck/'

    def form_valid(self, form):
        return super(SigninFormView, self).form_valid(form)
