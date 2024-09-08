from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'پیام'
        # verbose_name_plural = 'پیام ها'
    def __str__(self):
        return self.name
    
class NewsLetter(models.Model):
    email = models.EmailField(max_length=255) 
    
    def __str__(self):
        return self.email   