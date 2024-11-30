from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow unauthenticated access to login, logout, and static paths
        whitelisted_paths = [
            settings.LOGIN_URL, 
            '/accounts/logout/',
            '/static/',  # Tabler's assets
        ]
        if not request.user.is_authenticated and not any(request.path.startswith(path) for path in whitelisted_paths):
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return self.get_response(request)
