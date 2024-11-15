from django import template
from blog.models import post, Comment
from blog.models import Category

register = template.Library()


@register.simple_tag
def function(a=4):
    return a+2


register.simple_tag(lambda x: x - 2, name="minustwo")


@register.simple_tag(name='minusone')
def some_function(value=6):
    return value - 1


# from blog.models import post

@register.simple_tag(name="totalposts") 
def totalposts():
    posts = post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="comments_count")
def function(pid):
    comments = Comment.objects.filter(post=pid,approved=True).count()
    return comments


@register.simple_tag(name="posts") 
def totalposts():
    posts = post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=33):
    return value[:arg]+'.....'

# @register.inclusion_tag('popularposts.html')
# def popularposts():
#     posts = post.objects.filter(status=1).order_by('published_date')[:2]
#     return {'posts':posts}
  
    
@register.inclusion_tag("blog/blog-popular-posts.html")
def latestposts(arg=3):
    posts = post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}


# from blog.models import Category

@register.inclusion_tag("blog/blog-post-categories.html")
def postcategories():
    posts = post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for cat_name in categories:
        cat_dict[cat_name] = posts.filter(category=cat_name).count()
    return {'categories': cat_dict}