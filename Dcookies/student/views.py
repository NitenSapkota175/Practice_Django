from django.shortcuts import render

def setcookie(request):
        
        response = render(request,'student/setcookies.html')
        response.set_cookie('name','sonam')
        return response


def getcookie(request):
        
        name = request.COOKIES.get('name')
        return  render(request,'student/getcookies.html',{'name' : name})


def delcookie(request):
        
        reponse = render(request,'student/delcookies.html',)
        reponse.delete_cookie('name')
        return reponse
