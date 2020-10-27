from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.

      

def dashboard(request):
    if(request.method=='POST'):
           return HttpResponse(request.post)
            
    return render(request,"dashboard/base.html")