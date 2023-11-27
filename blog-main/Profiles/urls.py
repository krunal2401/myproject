
from django.urls import path, include
from .views import profile_view, delete_post
app_name = "Profiles"
urlpatterns = [
    path('my-profile/', profile_view, name='profile-view'),
    path('delete-post/<int:id>',delete_post, name='delete_post')
    # path('update/',profile_update_view, name='update')

]
