from Post.models import Post
from .models import Profile
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import UpdateProfileForm

# Create your views here.

def profile_view(request):
    if request.user.is_anonymous:
        return redirect('Blogs:home-view')
    pro = Profile.objects.get(user=request.user)
    
    p_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=pro)
    if request.method == 'POST':
        if p_form.is_valid():
            p_form.save()
    p_form = UpdateProfileForm(instance=pro)
    context = {
        'profile':pro,
        'form':p_form
    }
    return render(request, 'profile/profile.html', context)

def delete_post(request, id):
    print(id, "###################")
    # profile = Profile.objects.get(user=request.user)
    my_post = Post.objects.get(id= id)
    my_post.delete()
    print("hello")
    # context = {
    #     'profile':profile,
    # }
    return redirect('Profiles:profile-view')

# def profile_update_view(request):
#     if request.method == 'POST' and request.FILES['upload']:
#         m = Profile(user = request.user)
#         m.firstname = request.POST['firstname']
#         m.lastname = request.POST['lastname']
#         m.email = request.POST['email']
#         m.avatar = request.FILES['upload']
#         m.save()
#         return redirect('profile-view')
#     return render(request, 'profile/profile.html')
