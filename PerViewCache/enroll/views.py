from django.shortcuts import render

# from django.views.decorators.cache import cache_page

# @cache_page(30)
# def home(request):
#     return render(request,'enroll/home.html')


def home(request):
    return render(request,'enroll/home.html')


def contact(request):
    return render(request,'enroll/contact.html')