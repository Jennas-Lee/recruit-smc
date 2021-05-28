from django import forms
from django.views.generic import FormView
import re


class SignupForm(forms.Form):
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'signup-id-input'
            }
        ),
        required=False,
        strip=False
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
        strip=False
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
        strip=False
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
        strip=False
    )
    user_team = forms.ChoiceField(
        label='부서',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'signup-team-input'
            }
        ),
        required=False,
        choices=(
            ("0", "선택"),
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
        user_confirm_password = self.cleaned_data['user_confirm_password']
        user_name = self.cleaned_data['user_name']
        user_team = self.cleaned_data['user_team']

        user_id_re = re.compile('^[0-9a-zA-Z]*$')
        user_password_check_other_re = re.compile(
            """
            ^(?=.*[a-z])(?=.*\d)(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+])[A-Za-z\d$`~!@$!%*#^?&\\(\\)\-_=+]
            """)
        user_password_check_require_re = re.compile(
            ''
        )

        if len(user_id) == 0:
            self.inputValidate('user_id', '아이디를 입력하세요.')
        elif len(user_id) < 6:
            self.inputValidate('user_id', '아이디는 6자 이상으로 입력해주세요.')
        elif len(user_id) > 15:
            self.inputValidate('user_id', '아이디는 15자 이하로 입력해주세요.')
        elif ' ' in user_id:
            self.inputValidate('user_id', '아이디에 공백은 입력할 수 없습니다.')
        elif user_id_re.match(user_id) is None:
            self.inputValidate('user_id', '아이디에는 알파벳과 숫자만 입력할 수 있습니다.')
        else:
            pass

        if len(user_password) == 0:
            self.inputValidate('user_password', '비밀번호를 입력하세요.')
        elif len(user_password) < 8:
            self.inputValidate('user_password', '비밀번호는 8자 이상으로 입력해주세요.')
        elif len(user_password) > 20:
            self.inputValidate('user_password', '비밀번호는 20자 이하로 입력해주세요.')
        elif ' ' in user_password:
            self.inputValidate('user_password', '비밀번호에 공백은 입력할 수 없습니다.')
        elif user_password_check_other_re(user_password) is None:   # TODO: Fix password validation logic
            self.inputValidate('user_password', '비밀번호에는 알파벳과 숫자, 특수문자만 입력할 수 있습니다.')

        if len(user_confirm_password) == 0:
            self.inputValidate('user_confirm_password', '비밀번호를 한번 더 입력하세요.')

        if len(user_name) == 0:
            self.inputValidate('user_name', '이름을 입력하세요.')

        if user_team == "0":
            self.inputValidate('user_team', '부서를 선택하세요.')

    def inputValidate(self, input_field, error_message):
        """
        폼의 에러를 처리하는 메소드입니다.

        :param input_field: 에러를 표시할 `input` 태그입니다.
        :param error_message: 에러 메세지입니댜.
        :return: HTML에 에러 메세지를 표시합니다.
        """
        self.add_error(input_field, forms.ValidationError(error_message))
        self.fields[input_field].widget.attrs['class'] += ' is-invalid'


class SignupFormView(FormView):
    form_class = SignupForm
    template_name = 'teacher/signup.html'
    success_url = '/teacher/signin/'

    def form_valid(self, form):
        return super(SignupFormView, self).form_valid(form)
