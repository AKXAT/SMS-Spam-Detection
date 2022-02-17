from django.template.response import TemplateResponse
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
            context = {
                'Spam':True
            }
        else:
            #print('noooo')
            context = {
                'Spam':False
            }
    
    return TemplateResponse(request, 'baseapp/result.html',context)

