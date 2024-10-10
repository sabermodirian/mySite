from django.shortcuts import render , get_object_or_404
from blog.models import post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, **kwargs):
    posts = post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get("tag_name") != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)        
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(posts.num_pages)    
    contex = {'posts':posts}
    return render(request, 'blog/blog-home.html',contex)

def blog_single(request, pid):
    posts = post.objects.filter(status=1)
    pst = get_object_or_404(posts, pk=pid )
    context = {'post':pst}
    return render(request, 'blog/blog-single.html',context)

def blog_category(request,cat_name):
    posts = post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
    
def blog_search(request):
   # print(request.__dict__)    
    #query = request.GET.get('q')
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):#  Used python Warlus operator
            posts = posts.filter(content__contains=s)#  Used python Warlus operator

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)    

# def test(request, pid):
#     pst = get_object_or_404(post, pk=pid)
#     context = {'post':pst}
#     return render(request,'test.html',context)

def test(request):
    return render(request,'test.html')
