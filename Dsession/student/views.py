from django.shortcuts import render
from django.http import HttpResponse
def set_session(request):

    request.session['name'] = "Niten"
    # request.session.set_expiry(600)
    return render(request,'student/setsession.html')
    # request.session['name'] = "Niten"
    # request.session['lname'] = "Sapkota"
    # return render(request,'student/setsession.html')


def get_session(request):
    
    name = request.session.get('name',default="Guest")
    if 'name' in request.session:
        # print(request.session.get_session_cookie_age())
        # print(request.session.get_expiry_age())
        # print(request.session.get_expiry_date())
        # print(request.session.get_expire_at_browser_close())
         request.session.modified = True
         return render(request,'student/getsession.html',{'name' : name})


    else:
        return HttpResponse("Your session has been expired")
   

    # name = request.session.get('name',default="Guest")
    # lname = request.session.get('lname',default="Guest")
    # keys = request.session.keys()
    # items = request.session.items()
    # age = request.session.setdefault('age','26')
    # return render(request,'student/getsession.html',{'name' : name , 'lname' : lname , 'keys' : keys , 'items' : items , 'age' : age})
   

def delsession(request):

    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')
