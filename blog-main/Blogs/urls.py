

from django.urls import path, include
from .views import home_view,logoutUser, userReg, userlogin, user_validation,home
app_name = "Blogs"
urlpatterns = [
    path('', home_view, name='home-view'),
    path('blog/', home, name='home'),
    path('logout/',logoutUser, name='logout-view'),
    path('login/', userlogin, name='login'),
    path('register/', userReg, name='register'),
    path('validate/', user_validation, name='validate')

]
