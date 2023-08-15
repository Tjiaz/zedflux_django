from django.shortcuts import render
from .models import BlogPost, BlogDetail

# Create your views here.
def index(request):
  return render(request,'index.html')

def blog(request):
   blog_posts  = BlogPost.objects.all()
   return render(request,'blog.html',{'blog_posts': blog_posts })

def blogdetails(request,pk):
  blog_details = BlogPost.objects.get(id=pk)
  return render(request,'blog-details.html',{'blog_details':blog_details})