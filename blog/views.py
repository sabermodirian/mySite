from django.shortcuts import render
from blog.models import post


def blog_view(request):
    posts = post.objects.filter(status=1)
    contex = {'posts':posts}
    return render(request, 'blog/blog-home.html',contex)

def blog_single(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    posts = post.objects.all()
    context = {'posts':posts}
    return render(request,'test.html',context)
