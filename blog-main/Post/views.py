from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from django.core import serializers

from Profiles.models import Profile
from .models import Post,Like
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.paginator import Paginator
# from .form import CommentForm
# Create your views here.

def post_view(request):
    page_number=1
    posts = Post.objects.select_related('author').all().order_by('-id')


    

    # print(posts)    
    paginator = Paginator(posts, 10)
    # c_form = CommentForm(request.POST or None, request.user)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    # print(like_post.get_my_likes())
    
    
    # if request.user.is_authenticated:
    #     pro = Profile.objects.get(user = request.user)

        
    context  = {
        'page_obj':page_obj,
        'range':range(1,page_obj.paginator.num_pages+1),
    
        # 'profile':pro
    }
    return render(request, 'post/post.html',context)

def post_save(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            img = request.FILES.get('image')
            body = request.POST['body']

            pro = Profile.objects.get(user = request.user)
            post_data = Post(title = title, img = img, body = body, author =pro)
            post_data.save()
            return redirect('Posts:post-view')
        pass
    return redirect('Posts:post-view')

def like_post_view(request,post_id):
    if request.user.is_authenticated:
    

        post_obj = Post.objects.get(id=post_id)
        print(post_obj)
        profile = Profile.objects.get(user=request.user)
        is_existed = Like.objects.filter(user=profile, post = post_obj).first()
        if is_existed:
            is_existed.delete()
        else:
            like = Like(user=profile, post=post_obj)
            like.save()

        return redirect('Posts:post-view')
    return redirect('Posts:post-view')