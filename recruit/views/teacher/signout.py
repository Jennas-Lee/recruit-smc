from django.shortcuts import redirect


def signout(request):
    response = redirect('/')
    response.delete_cookie('USER_JWT')
    return response
