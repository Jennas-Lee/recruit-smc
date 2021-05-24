from django import forms
from django.shortcuts import render
from django.views.generic import View, FormView


class SignupForm(forms.Form):
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'signup-id-input'
            }
        ),
        required=False
    )
    user_password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'signup-password-input'
            }
        ),
        required=False,
        min_length=8,
        max_length=20
    )
    user_confirm_password = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'signup-password-confirm-input'
            }
        ),
        required=False,
        min_length=8,
        max_length=20
    )
    user_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'signup-name-input'
            }
        ),
        required=False,
        min_length=2,
        max_length=5
    )
    user_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'signup-name-input'
            }
        ),
        required=False,
        min_length=2,
        max_length=5
    )
    user_team = forms.ChoiceField(
        label='이름',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'signup-team-input'
            }
        ),
        required=False,
        choices=(
            ("1", "교무기획부"),
            ("2", "교육연구부"),
            ("3", "생활안전부"),
            ("4", "교과교육부"),
            ("5", "창의체험부"),
            ("6", "취업지원부"),
            ("7", "진로상담부"),
            ("8", "홍보기획부"),
            ("9", "실과도제교육부"),
            ("10", "스마트보안솔루션과"),
            ("11", "디바이스소프트웨어과"),
            ("12", "인공지능소프트웨어과"),
            ("13", "게임소프트웨어과")
        )
    )

    def clean(self):
        user_id = self.cleaned_data['user_id']
        user_password = self.cleaned_data['user_password']

        if len(user_id) == 0:
            self.add_error('user_id', forms.ValidationError('아이디를 입력하세요.'))


class SignupFormView(FormView):
    form_class = SignupForm
    template_name = 'teacher/signup.html'
    success_url = '/teacher/signin/'

    def form_valid(self, form):
        return super(SignupFormView, self).form_valid(form)
