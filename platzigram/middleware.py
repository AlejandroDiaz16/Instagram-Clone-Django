"""platzigram middleware catalog"""

#django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """
    ensure every user is interacting with the platform
    have their profile picture and biography
    """
    def __init__(self, get_response):
        """middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """code to be execute for each request before the view is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        response = self.get_response(request)
        return response