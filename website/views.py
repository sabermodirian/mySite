from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import contact
from website.forms import NameForm , ContactForm , NewsLetterForm
from django.contrib import messages as msg

def index_view(request):
    return render(request , 'website\index.html')

def about_view(request):
    return render(request , 'website\About.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg.add_message(request, msg.SUCCESS, 'Form submitted successfully')
            #msg.success(request, "Form submitted successfully.")
        else:
            msg.add_message(request, msg.ERROR, 'Form is not valid')
            #msg.ERROR(request, 'Form is not valid')

    form = ContactForm()   
    return render(request ,'website/contact.html',{'form': form})     
           
def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            msg.add_message(request, msg.SUCCESS, 'Form submitted successfully')
        else:
            msg.add_message(request, msg.ERROR, 'Form is not valid')    
            
            #return HttpResponseRedirect('/') #redirect to homepage.html
    else:
        return HttpResponseRedirect('/') 
        
                
    #return render(request ,'website/NewsLetter.html')    

# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
def test_view(request):
    if request.method == 'POST':
        # form = NameForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            #print(name, email, subject, message)
            form.save()
            return HttpResponse('Form submitted successfully')
        else:
            return HttpResponse('Form is not valid')
    # form = NameForm() 
    form = ContactForm()
    return render(request, 'test.html', {'form': form})  



     
            
                

