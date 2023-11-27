

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from Post.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }    
    return render(request, 'blogs/blog.html', context)

def home_view(request):
    return redirect('Posts:post-view')
    # return render(request, 'blogs/blog.html')

def userlogin(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST.get('u_name')
        password = request.POST.get('pass')
        print(username)
        print(password)
        if User.objects.filter(username=username):
            if User.objects.filter(password=password):
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    print(login(request, user))
                    msg += "You are Logged In successfully...!"
                else:
                    msg+= "Server side Error.."

            else:
                msg += "please Enter valid password ..."
        else:
            msg += "please Enter valid username ..."
    return JsonResponse({"status":msg})


def logoutUser(request):
    logout(request)
    return redirect('Posts:post-view')

def userReg(request):
    # username = None
    data = {}
    if request.method == 'GET':
        data['username'] = request.GET.get('username')
        data['email'] = request.GET.get('email')
        data['pass1'] = request.GET.get('pass1')
        data['pass2'] = request.GET.get('pass2')
    # data = {
    #     'username' : request.GET['username'],
    #     'email':request.GET['email'.GET]
    # }
    if request.user. is_authenticated:
        return redirect('Posts:post-view')    
    return render(request, 'blogs/userRegform.html', data)

        
def user_validation(request):
    msg = ""
    if request.method == 'POST':
        u_name = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        if not User.objects.filter(username=u_name):
            if pass1==pass2:
                newUser = User.objects.create_user(username = u_name, email=email, password = pass1)
                newUser.save()
                user = authenticate(username=u_name, password=pass1)
                login(request, user)
                msg = "success"
                messages.success(request, msg)
                return redirect('/')    
            
            msg = "Your password is not matched!!"        
            messages.warning(request, msg)    
            url = "/register/?username={}&email={}".format(u_name,email)
            return redirect(url)       
        
        msg = "Username already exist!! please try another"
        messages.warning(request, msg)
        url = "/register/?pass1={}&pass2={}&email={}".format(pass1,pass2,email)    
        return redirect(url)

    