"""posts views"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm
from posts.models import Posts

# Create your views here.
from datetime import datetime

@login_required
def list_posts(request):
    """list existing posts"""
    posts = Posts.objects.all().order_by('created')
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(
        request= request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )