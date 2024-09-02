from django.shortcuts import render,HttpResponse
def home(request):
    print('I am in Home view')
    return HttpResponse('This is Home page')