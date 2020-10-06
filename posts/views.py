"""posts views"""

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from posts.forms import PostForm
from posts.models import Posts

# Create your views here.


class PostDetailView(LoginRequiredMixin, DetailView):
    """posts detail view"""
    template_name = 'posts/detail.html'
    queryset = Posts.objects.all()
    context_object_name = 'post'



class PostsFeedView(LoginRequiredMixin, ListView):
    """return all publisehd posts"""
    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    """create new post """

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

