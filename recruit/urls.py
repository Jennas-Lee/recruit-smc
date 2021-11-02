from django.urls import path

from recruit.views import index, form_receive, form_documents

urlpatterns = [
    path('', index, name='recruit-index'),
    path('receive/', form_receive, name='recruit-form-receive'),
    path('documents/', form_documents, name='recruit-form-documents'),
]
