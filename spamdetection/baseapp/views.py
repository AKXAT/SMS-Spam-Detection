from tkinter.tix import Tree
from django.template.response import TemplateResponse
from django.http import HttpResponse
from baseapp import detectSpam

# Create your views here.

def homePageView(request):
    return TemplateResponse(request, 'baseapp/app.html',{})

def resultPageView(request):
    if request.method == 'POST':
        #do something
        mystring = str(request.POST['sms'])
        if detectSpam.main(mystring) == True:
            #print('YESSS')
            return TemplateResponse(request, 'baseapp/result.html',{})
        else:
            #print('noooo')
            return TemplateResponse(request, 'baseapp/result.html',{})
    
    return TemplateResponse(request, 'baseapp/result.html',{})

