from django.contrib import admin
from website.models import contact , NewsLetter


# Register your models here.
class contactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'subject','created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    empty_value_display = '-empty-'
    
admin.site.register(contact, contactAdmin)
admin.site.register(NewsLetter)