from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import PostForm,CommentForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})



@login_required
def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})



@login_required(login_url='/login/')
def detail(request, pk):
    current_user = request.user
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        current_user = request.user
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
        
    return render(request, 'detail.html', {'post': post,'form': form})



@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')



@login_required(login_url='/login/')
def update(request,pk):
    instance = Post.objects.get(pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=instance)
    return render(request,'update.html',{'form':form})


@login_required
def my_post(request):
    current_user = request.user
    posts =  Post.objects.filter(author=current_user)
    return render(request, 'my_post.html', {'posts': posts})



