from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import cookie
from django.shortcuts import (
    get_object_or_404, redirect, render, HttpResponse
)
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.hashers import CryptPasswordHasher
from app.forms import SignUpUserForm, SignUpProfileForm, ToPostForm
from app.models import Post, Profile
from django import template


class Index(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('date').reverse()
        listaPosts = list(posts)
        if len(posts) > 0:
            return render(request, 'index.html', {'posts':listaPosts[1:4], 'first':listaPosts[0]})
        return render(request, 'index.html')
class SignUp(View):
    def get(self, request, *args, **kwargs):
        userForm = SignUpUserForm()
        profileForm = SignUpProfileForm
        return render(request, 'registration/signup.html', {'userForm': userForm, 'profileForm': profileForm })

    def post(self, request, *args, **kwargs):
        userForm = SignUpUserForm(request.POST)
        profileForm = SignUpProfileForm(request.POST, request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = User.objects.create_user(
                username=userForm.cleaned_data['username'],
                email=userForm.cleaned_data['email'],
                last_name=userForm.cleaned_data['last_name'],
                first_name=userForm.cleaned_data['first_name'],
                password=userForm.cleaned_data['password'],
            )
            profile = Profile.objects.create(
                user = user,
                image=profileForm.cleaned_data['image'],
                about_me=profileForm.cleaned_data['about_me']
            )
            user.save()
            profile.save()
            return redirect('login')
        else:
            print(userForm.errors)
            print(profileForm.errors)
            input("DEU RUIM")
        return redirect('login')

class ShowProfile(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.filter(user=request.user).first()
            return render(request, 'auth/profile.html', {'profile':profile})
        return redirect('login')

        
class ShowArticle(View):
    
    def get(self, request, *args, **kwargs):
        article = Post.objects.filter(id=self.kwargs['id']).first()
        return render(request, 'openArticle.html', {'article':article})


class Articles(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            articles = Post.objects.all().order_by('date').reverse()
            return render(request, 'auth/articles.html', {'articles':articles})
        return redirect('login')


class ToPost(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = ToPostForm()
            return render(request, 'auth/topost.html', {'form': form})
        return redirect('login')

    def post(self, request, *args, **kwargs):
        form = ToPostForm(request.POST, request.FILES)
        if form.is_valid():
            formPost = Post(
                title=form.cleaned_data['title'],
                subtitle=form.cleaned_data['subtitle'],
                lide=form.cleaned_data['lide'],
                text=form.cleaned_data['text'],
                image=form.cleaned_data['image'],
                date=datetime.utcnow(),
                author=request.user
            )
            formPost.save()
        print(form.errors)
        return redirect('articles')


class Users(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            users = User.objects.all()
            return render(request, 'auth/users.html', {'users':users})
        return redirect('login')


def trashUser(request, id):
    if request.user.is_authenticated:
        user = User.objects.filter(id=id).first()
        user.delete()
        return redirect('users')
    return redirect('login')


def trashArticle(request, id):
    if request.user.is_authenticated:
        article = Post.objects.filter(id=id).first()
        article.delete()
        return redirect('articles')
    return redirect('login')
