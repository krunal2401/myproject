
from django.contrib import admin

from .models import Post, Like, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','body', 'created']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body','created']


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment, CommentAdmin)