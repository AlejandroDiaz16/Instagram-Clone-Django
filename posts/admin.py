"""posts admin"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from posts.models import Posts
from users.models import Profile
from  django.contrib.auth.models import User

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'user',
        'profile',
        'title',
        'photo',
    )

    list_display_links = ('pk', 'user',)

    list_editable = ('title', 'photo')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'title',
    )

    list_filter = (
        'created',
        'modified',
    )


