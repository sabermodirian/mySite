from django.contrib import admin
from blog.models import post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# @Admin.register(post)
class postAdmin(SummernoteModelAdmin):
    list_display = ('title','author', 'counted_views', 'status', 'published_date', 'updated_date')
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    #fields = ('title', 'content', 'status')
    list_filter = ('status','author')
    #ordering = ('-created_date',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)
 
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_date', 'approved') 
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    #fields = ('title', 'content', 'status')
    list_filter = ('post','approved')
    #ordering = ('-created_date',)
    search_fields = ('name', 'post')
    summernote_fields = ('content',) 
      
admin.site.register(Comment , CommentAdmin)    
admin.site.register(post , postAdmin)
admin.site.register(Category)