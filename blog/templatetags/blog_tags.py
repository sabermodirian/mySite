from django import template

register = template.Library()


@register.simple_tag
def function(a=4):
    return a+2


register.simple_tag(lambda x: x - 2, name="minustwo")


@register.simple_tag(name='minusone')
def some_function(value=6):
    return value - 1


from blog.models import post

@register.simple_tag(name="totalposts") 
def totalposts():
    posts = post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="posts") 
def totalposts():
    posts = post.objects.filter(status=1)
    return posts

