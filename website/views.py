from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import contact
from website.forms import NameForm


def index_view(request):
    return render(request, 'website\index.html')


def about_view(request):
    return render(request, 'website\About.html')


def contact_view(request):
    return render(request, 'website\contact.html')

# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('Form submitted successfully')
        else:
            return HttpResponse('Form is not valid')
    form = NameForm() 
    return render(request, 'test.html', {'form': form})  



     
            
                # name = form.cleaned_data['name']
                # email = form.cleaned_data['email']
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # c = contact()
                # c.name = name
                # c.email = email
                # c.subject = subject
                # c.message = message
                # c.save()
                # print(name,email,subject,message)
                # return JsonResponse({'message': 'Form submitted successfully'})
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     c = contact()
    #     c.name = name
    #     c.email = email
    #     c.subject = subject
    #     c.message = message
    #     c.save()
    #     print(name,email,subject,message)
    # elif request.method == 'GET': 
    #     print('GET')   
    # return render(request,'test.html',{})    


