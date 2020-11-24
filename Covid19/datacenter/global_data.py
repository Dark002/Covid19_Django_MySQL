import plotly.express as px
import pandas as pd
import json
import requests
import plotly.offline as plot
import plotly.graph_objs as go
import chart_studio.plotly as py
import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data/date.txt')
con_path = os.path.join(module_dir,'data/confirmed.csv')
rec_path = os.path.join(module_dir,'data/recovered.csv')
de_path = os.path.join(module_dir,'data/deaths.csv')
map_path = os.path.join(module_dir,'data/map.csv')

def get_map():
    df = pd.read_csv(map_path)
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
    graph = fig.to_html(full_html=False, default_height=700)
    return graph 
def get_confirmed():
    df  = pd.read_csv(con_path)
    df.drop(columns=['Province/State'],inplace=True,axis=1)
    return df
def get_deaths():
    df  = pd.read_csv(de_path)
    df.drop(columns=['Province/State'],inplace=True,axis=1)
    return df
def get_recovered():
    df  = pd.read_csv(rec_path)
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

