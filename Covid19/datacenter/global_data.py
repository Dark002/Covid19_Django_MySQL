import plotly.express as px
import pandas as pd
import json
import requests
import plotly.offline as plot
import plotly.graph_objs as go
import chart_studio.plotly as py
from datetime import datetime

def get_map():
    url = 'https://api.covid19api.com/summary'
    data = requests.get(url)
    df = pd.DataFrame(data.json()['Countries'])
    fig = px.choropleth( df, locations="Country",
                        color="TotalConfirmed", 
                        hover_name="Country", 
                        hover_data=[ 'CountryCode',
                            'NewConfirmed','TotalConfirmed',
                            'NewDeaths','TotalDeaths','NewRecovered',
                            'TotalRecovered','Date', 'Slug'
                                   ], 
                        locationmode="country names",
                        projection="orthographic",
                        color_continuous_scale=px.colors.sequential.dense,
                        height=700,
                        width=1800
                       ).update_layout(clickmode='event+select')
    graph = fig.to_html(full_html=False, default_height=800)
    return graph 
def get_confirmed():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df  = pd.read_csv(url)
    df.drop(columns=['Province/State'],inplace=True,axis=1)
    return df
def get_deaths():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    df  = pd.read_csv(url)
    df.drop(columns=['Province/State'],inplace=True,axis=1)
    return df
def get_recovered():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    df  = pd.read_csv(url)
    df.drop(columns=['Province/State'],inplace=True,axis=1)
    return df
def get_graph():
    df_confirmed = get_confirmed()
    df_deaths = get_deaths()
    df_recovered = get_recovered()
    df_confirmed.drop(columns=['Country/Region','Lat','Long'],inplace=True,axis=1) 
    df_deaths.drop(columns=['Country/Region','Lat','Long'],inplace=True,axis=1) 
    df_recovered.drop(columns=['Country/Region','Lat','Long'],inplace=True,axis=1)  
    dates = []
    for i in df_confirmed:
        ls = i.split("/")
        st = "2020"+"-"+ls[0]+"-"+ls[1] 
        dates.append(st)   
    df = pd.DataFrame(columns=['Date','Type','Number'])
    confirmed,active,deaths,recovered = [],[],[],[]
    df_confirmed = df_confirmed.sum(axis=0)
    df_deaths = df_deaths.sum(axis=0)
    df_recovered = df_recovered.sum(axis=0) 
    for  i in df_confirmed:
        confirmed.append(i)
    for  i in df_deaths:
        deaths.append(i)
    for  i in df_recovered:
        recovered.append(i)       
    for  i in range(len(confirmed)):
        data = {'Date':dates[i],'Type':'Confirmed','Number':confirmed[i]}
        df.loc[4*i]=data
        data = {'Date':dates[i],'Type':'Deaths','Number':deaths[i]}
        df.loc[4*i+1]=data
        data = {'Date':dates[i],'Type':'Recovered','Number':recovered[i]}
        df.loc[4*i+2]=data
        data = {'Date':dates[i],'Type':'Active','Number':confirmed[i]-deaths[i]-recovered[i]}
        df.loc[4*i+3]=data
    fig = px.line(df,x='Date',y='Number',color='Type',title="Line Chart of Global Cases/Deaths")    
    graph = fig.to_html(full_html=False, default_height=800)
    return graph 

