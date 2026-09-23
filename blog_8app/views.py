from ast import mod

from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Blog

# Create your views here.
class BlogListView(ListView):
    model = Blog 
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog 
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog 
    template_name = 'blog_create.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    queryset = Blog.objects.all()
    models = Blog 
    template_name = 'blog_update.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Blog 
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')

def custom_logout_view(request):
    logout(request)
    # return redirect('home')
    return redirect('login')