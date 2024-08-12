from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fee_structure(request):
    return render(request,'fee/fees.html')

