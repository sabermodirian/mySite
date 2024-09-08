from django import forms
from website.models import contact , NewsLetter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm): 
    # last_name = forms.CharField(max_length=255)
    class Meta:
        model = contact
        fields = '__all__' #fields = ('name', 'email', 'subject','message')  
        
        # exclude = ['name'] --> remove name field from form' fields 
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"  #"fields = ('email',)        
        