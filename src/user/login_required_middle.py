import re

from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL)]

if hasattr(settings, "LOGIN_EXEMPT_URLS"):
    EXEMPT_URLS += ['register/', 'login/']

# print('-------------', EXEMPT_URLS)


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('---------------------', request)
        assert hasattr(request, 'user')
        if not request.user.is_authenticated:
            if not any(['register/', 'login/']):
                a = ['register/', 'login/']
                print(a)
                return redirect(['register/', 'login/'])
        elif request.user.is_authenticated:
            return None
        else:
            return redirect(settings.LOGIN_URL)