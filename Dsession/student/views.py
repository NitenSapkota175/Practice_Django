from django.shortcuts import render

def set_session(request):
    request.session['name'] = "Niten"
    request.session['lname'] = "Sapkota"
    return render(request,'student/setsession.html')


def get_session(request):
    name = request.session.get('name',default="Guest")
    lname = request.session.get('lname',default="Guest")
    return render(request,'student/getsession.html',{'name' : name , 'lname' : lname})

def delsession(request):

    if 'name' in request.session:
        del request.session['name']

    return render(request,'student/delsession.html')
