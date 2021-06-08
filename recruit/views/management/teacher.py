from django.views.generic import View, ListView
from django.shortcuts import render
from recruit.models import TcrUserTb
from recruit.views.base import makeBit

class TeacherListView(ListView):
    # paginate_by = 15
    paginate_by = 1  # TODO: Change to 15
    model = TcrUserTb
    template_name = 'management/teacherList.html'

    def get_queryset(self):
        return TcrUserTb.objects.filter(USER_ST__gt=0).order_by('-IDX')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wait_user'] = TcrUserTb.objects.filter(USER_ST__lte=0).count()
        context['navbar'] = 'management'
        return context


class TeacherPersonalManagementView(View):
    def get(self, request, user_id):
        try:
            if TcrUserTb.objects.filter(USER_ID_TXT=user_id).exists():
                model = TcrUserTb.objects.get(USER_ID_TXT=user_id)
                user_authorize_list = makeBit(model.USER_ST)
                return render(request, 'management/teacherManagement.html', {
                    'user_exist': True,
                    'user_id': user_id,
                    'user_name': model.USER_NM,
                    'user_team': model.USER_TEAM_CD,
                    'user_authorize': user_authorize_list
                })
            else:
                raise KeyError
        except KeyError:
            return render(request, 'management/teacherManagement.html', {'user_exist': False})

    def post(self, request):
        return 0
