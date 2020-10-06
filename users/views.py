"""users views"""

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

from django.contrib.auth.models import User
from posts.models import Posts
from django.http import HttpResponseRedirect

#forms
from users.forms import SignupForm, fakeForm
from users.models import Profile, DataFake



class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    #lo que se pide en el path
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):

        """add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        #context['user'] = self.get_object()
        #print(user)
        context['posts'] = Posts.objects.filter(user=user)
        return context


class LoginView(auth_views.LoginView):
    """login view"""
    template_name = 'users/login.html'



class UpdateProfileView(CreateView):
    """uodate profile view"""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self, queryset=None):
        """return user'sprofile"""
        return self.request.user.profile

    def get_success_url(self):
        """return to users profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """logout view"""
    template_name = 'users/logged_out.html'

class SignupView(FormView):
    """Users sign up view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """save form data"""
        form.save()
        return super().form_valid(form)

class fakeLogin(FormView):
    template_name = 'users/login.html'
    form_class = fakeForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

