from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.
from . import data_mining
      

def home(request):
    tab = data_mining.get_table()
    plot_confirmed = data_mining.get_confirmed()
    plot_active = data_mining.get_active()
    plot_death = data_mining.get_deaths()
    plot_recovered = data_mining.get_recovered()

    total_cases=0
    active_cases=0
    recoverd=0
    deaths=0
    for i in tab:
           total_cases+=int(i[1])
           recoverd+=int(i[2])
           deaths+=int(i[3])
    active_cases=total_cases-recoverd-deaths      
    context={
           'tab':tab,
           'total_cases':total_cases,
           'active_cases':active_cases,
           'recoverd':recoverd,
           'deaths': deaths,
           'plot_confirmed':plot_confirmed,
           'plot_active':plot_active,
           'plot_death':plot_death,
           'plot_recovered':plot_recovered
    }          
    return render(request,"dashboard/base.html",context)