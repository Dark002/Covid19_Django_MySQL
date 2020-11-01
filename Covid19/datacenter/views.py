from django.shortcuts import render
from .forms import *
from .models import *
from .mysql import *

# Create your views here.
def home(request):
    context={}
    flag=0
    if request.method == 'POST':
        form=world_form(request.POST)
        if form.is_valid():
            flag=1
            country=form.cleaned_data['country']
            date2=form.cleaned_data['date']
            date=date2.strftime('%m-%d-%Y')
            date1=date2.strftime('%d-%m-%Y')
            global_report(date)
            context={'form':world_form,'flag':flag,'country':country,'date':date1,'total_cases':get_total_cases(country),
            'total_deaths':get_total_deaths(country),'total_recovered':get_total_recovered(country),'active_cases':get_active_cases(country),
            'flag':flag}
            #context["form"]=world_form
            #context['country']=country
            #context['date']=date
            #context['total_cases']=get_total_cases(country)
            #context['total_deaths']=get_total_deaths(country)
            #context['total_recovered']=get_total_recovered(country)
            #context['active_cases']=get_active_cases(country)
            #context['flag']=flag
            return render(request, 'datacenter/home.html',context)
        else :
            context={'form':world_form,'flag':flag}
            return render(request, 'datacenter/home.html',context)

    else :
        form=world_form()
        context={'form':world_form,'flag':flag}
        return render(request, 'datacenter/home.html',context)
