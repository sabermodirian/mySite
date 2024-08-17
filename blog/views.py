from django.shortcuts import render , get_object_or_404
from blog.models import post


def blog_view(request):
    posts = post.objects.filter(status=1)
    contex = {'posts':posts}
    return render(request, 'blog/blog-home.html',contex)

def blog_single(request, pid):
    posts = post.objects.filter(status=1)
    pst = get_object_or_404(posts, pk=pid )
    context = {'post':pst}
    return render(request, 'blog/blog-single.html',context)

def test(request, pid):
    pst = get_object_or_404(post, pk=pid)
    context = {'post':pst}
    return render(request,'test.html',context)
