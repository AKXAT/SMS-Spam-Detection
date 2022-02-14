from django.template.response import TemplateResponse
from django.http import HttpResponse
# Create your views here.


def homePageView(request):
    return TemplateResponse(request, 'baseapp/app.html',{})

