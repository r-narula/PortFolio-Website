from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import DetailView
 

def home(request):
    context = {
        'posts':Post.objects.all(),
        'title':"mononoke's Blog",
    }
    counter = 0
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'title':'About Me'
    }
    return render(request,'blog/about.html',context)


# presenting views of your database content
class PostView(DetailView):
    model = Post
    template_name = 'blog/separate_view.html'




    