
from django.urls import path, include
from .views import post_view,post_save,like_post_view
app_name = "Posts"
urlpatterns = [
    path('all-post/', post_view, name='post-view'),
    path('add_like/<int:post_id>',like_post_view,name= 'like'),
    path('add_post/',post_save, name='save'),
    
]

