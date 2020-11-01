from django.shortcuts import render
from .forms import *
from .models import world
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
            x=world.objects.filter(country_name=country).values('total_cases')
            for a in x:
                x1=a['total_cases']
            y=world.objects.filter(country_name=country).values('total_deaths')
            for a in y:
                y1=a['total_deaths']
            z=world.objects.filter(country_name=country).values('total_recovered')
            for a in z:
                z1=a['total_recovered']
            w=world.objects.filter(country_name=country).values('active_cases')
            for a in w:
                w1=a['active_cases']
            context={'form':world_form,'flag':flag,'country':country,'date':date1,'total_cases':x1,
            'total_deaths':y1,'total_recovered':z1,'active_cases':w1,
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
