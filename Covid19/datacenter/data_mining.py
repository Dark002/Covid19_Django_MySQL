import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from fbprophet import Prophet
import plotly.graph_objs as go
import plotly.offline as py
import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data/date.txt')
con_path = os.path.join(module_dir,'data/confirmed.csv')
rec_path = os.path.join(module_dir,'data/recovered.csv')
de_path = os.path.join(module_dir,'data/deaths.csv')

def get_confirmed():
    df  = pd.read_csv(con_path)
    df.drop(columns=['Province/State','Country/Region','Lat','Long'],inplace=True,axis=1)
    dates = []
    for i in df:
        ls = i.split("/")
        st = "2020"+"-"+ls[0]+"-"+ls[1] 
        dates.append(st)
    df = df.sum(axis=0)  
    new_df = pd.DataFrame(columns=['Date','Confirmed']) 
    confirmed = []
    for  i in df:
        confirmed.append(i)
    for  i in range(len(confirmed)):
        data = {'Date':dates[i],'Confirmed':confirmed[i]}
        new_df.loc[i]=data     
    return new_df

# machine learning in covid19
def prediction():
     
     confirmed = get_confirmed()
     confirmed.columns = ['ds','y']
     confirmed['ds'] = pd.to_datetime(confirmed['ds'])
     m = Prophet(interval_width=0.95)
     m.fit(confirmed)
     future = m.make_future_dataframe(periods=7)
     forecast = m.predict(future)
     trace = go.Scatter(
        name = 'Actual Cases',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(confirmed['y']),
        marker=dict(
        color='#FFBAD2',
        line=dict(width=1)
        )
     )   
     trace1 = go.Scatter(
        name = 'trend',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(forecast['yhat']),
        marker=dict(
        color='red',
        line=dict(width=3)
       )
    )
     upper_band = go.Scatter(
        name = 'upper limit',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(forecast['yhat_upper']),
        line= dict(color='#57b88f'),
        fill = 'tonexty'
    ) 
     lower_band = go.Scatter(
        name= 'lower limit',
        mode = 'lines',
        x = list(forecast['ds']),
        y = list(forecast['yhat_lower']),
        line= dict(color='#1705ff')
    )
     data = [trace1, lower_band, upper_band, trace]
     layout = dict(title='Confirmed Cases Estimation Using FbProphet',
             xaxis=dict(title = 'Dates', ticklen=2, zeroline=True),
             yaxis=dict(title='Cases'))   
     figure=dict(data=data,layout=layout)
     fig=go.Figure(data,layout)
     plot_div = plot(fig,output_type="div")
     return plot_div 

