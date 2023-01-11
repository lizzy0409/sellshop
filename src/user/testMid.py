from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout


class BlacklistMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> HttpResponse:
        self.handle_request(request)

        response = self.get_response(request)

        self.handle_response(response)
        return response

    def handle_request(self, request) -> None:
        user = request.user

        if not user:
            return
        if user.is_authenticated:
            blacklist, _ = Group.objects.get_or_create(name="Blacklist")

            if blacklist.user_set.filter(email=user.email).exists():
                logout(request)
                raise PermissionDenied()

    def handle_response(self, request) -> None:
        ...
