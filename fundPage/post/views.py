from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import post, donate
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model=post
    template_name='home.html'
    ordering=['-id']

class AddPost(CreateView):
    model=post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'

class UpdatePost(UpdateView):
    model=post
    form_class=UpdateForm
    template_name='update_post.html'
    # fields=['body']

class DeletePost(DeleteView):
    model=post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
