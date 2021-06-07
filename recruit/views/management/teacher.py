from django.views.generic import ListView
from recruit.models import TcrUserTb


class TeacherListView(ListView):
    # paginate_by = 15
    paginate_by = 1  # TODO: Change to 15
    model = TcrUserTb
    template_name = 'management/teacher.html'

    def get_queryset(self):
        return TcrUserTb.objects.filter(USER_ST__gt=0).order_by('-IDX')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wait_user'] = TcrUserTb.objects.filter(USER_ST__lte=0).count()
        context['navbar'] = 'management'
        return context
