from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
def home(request):
    print('I am in Home view')
    return HttpResponse('This is Home page')

def excp(request):
    print('I am Excp view')
    a = 10/0
    return HttpResponse("This is Home page")


def  user_info(request):
    print('I am user info view')
    context = {
        'name' : 'Niten'
    }

    return TemplateResponse(request,'blog/user.html',context)