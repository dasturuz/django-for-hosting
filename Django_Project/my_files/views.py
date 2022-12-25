from django.shortcuts import render
from django.views.generic import  ListView,TemplateView,DetailView,UpdateView,DeleteView
from . models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class HomePage(ListView):
     model = Post
     template_name = 'index.html'

class About(TemplateView):
     template_name = 'about.html'

class BlogDetailView(DetailView):
     model = Post
     template_name = 'blog.html'

class CreaterBlog(CreateView):
     model = Post
     template_name = 'blog_creator.html'
     fields = ['title', 'author', 'text']

class BlogUpdateView(UpdateView):
     model = Post
     template_name = 'blog_editor.html'
     fields = ['title', 'text']

class BlogDeleteView(DeleteView):
     model = Post
     template_name = 'blog_delete.html'
     success_url = reverse_lazy('home')
     
