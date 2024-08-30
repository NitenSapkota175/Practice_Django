from django.shortcuts import render
from datetime import datetime,timedelta

def setcookie(request):
        
        # response = render(request,'student/setcookies.html')
        # response.set_cookie('name','sonam',max_age=120)
        
        # # set when cookies are going to expires using date time format
        # # response.set_cookie('name','sonam',expires=datetime.utcnow()+timedelta(days=2))
        # return response

        response = render(request,'student/setcookies.html')
        response.set_signed_cookie('name','niten',salt='nm',expires=datetime.now()+timedelta(days=2))
        return response




def getcookie(request):
        
        # name = request.COOKIES.get('name','Guest')
        name = request.get_signed_cookie('name',salt='nm')
        return  render(request,'student/getcookies.html',{'name' : name})


def delcookie(request):
        
        reponse = render(request,'student/delcookies.html',)
        reponse.delete_cookie('name')
        return reponse
