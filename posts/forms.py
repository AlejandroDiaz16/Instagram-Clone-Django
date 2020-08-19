""""post forms"""
from django import forms

from posts.models import Posts

class PostForm(forms.ModelForm):
    """post model form"""
    class Meta:
        """form settings"""
        model = Posts
        fields = ('user', 'profile', 'title', 'photo')