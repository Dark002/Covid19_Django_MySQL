from django.http import HttpResponse
from django.shortcuts import render
import json
from . import database
# Create your views here.


def home(request):
    return render(request,'index/home.html')

def get_data(request):
    df = database.daily_report(date_string=None)
    df = df[['Confirmed', 'Deaths', 'Recovered']].sum()
    death_rate = f'{(df.Deaths / df.Confirmed)*100:.02f}%'

    data = {
        'num_confirmed': int(df.Confirmed),
        'num_recovered': int(df.Recovered),
        'num_deaths': int(df.Deaths),
        'death_rate': death_rate
    }

    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')

