from django.contrib import admin
from blog.models import post


# Register your models here.

# @Admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'counted_views', 'status', 'published_date', 'updated_date')
    date_hierarchy ='created_date'
    empty_value_display = '-empty-'
    #fields = ('title', 'content', 'status')
    list_filter = ('status',)
    #ordering = ('-created_date',)
    search_fields = ('title', 'content')
    
admin.site.register(post , postAdmin)