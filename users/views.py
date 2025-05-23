from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib. auth.models import User
from main.models import Post

# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    posts = Post.objects.filter(name=user)

    context = {
        'user':user,
        'posts':posts
    }
    
    return render(request, 'users/mypage.html', context)
