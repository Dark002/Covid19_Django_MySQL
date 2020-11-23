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
file_path = os.path.join(module_dir, 'data/active.csv')
def get_table():
    headers={'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    url = "https://covidindia.org/"
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find('table')
    tab = []
    counter = 0
    temp = []

    for link in tb.find_all('td'):
        temp.append(link.get_text('title'))
        counter+=1
        if(counter==4):
            counter=0
            tab.append(temp)
            temp=[]
    tab=tab[:-1]
    return tab
def get_confirmed():
    tdf = pd.read_csv(file_path)
    fig = px.line(tdf, x="Date", y="Confirmed", color='State')
    plot_div = plot(fig,output_type="div",link_text=False)
    return plot_div

def get_deaths():
    tdf = pd.read_csv(file_path)
    fig = px.line(tdf, x="Date", y="Deceased", color='State')
    plot_div = plot(fig,output_type="div",link_text=False)
    return plot_div

def get_recovered():
    tdf = pd.read_csv(file_path)
    fig = px.line(tdf, x="Date", y="Recovered", color='State')
    plot_div = plot(fig,output_type="div",link_text=False)
    return plot_div    
def get_active():
    tdf = pd.read_csv(file_path)
    active = []
    # active = confirmed - deaths -recovered
    counter = 0
    for i in range(len(tdf['Confirmed'])):
        val = tdf['Confirmed'][counter] - tdf['Deceased'][counter] - tdf['Recovered'][counter]
        active.append(val)
        counter+=1
    tdf.insert(7,"Active",active,True)    
    fig = px.line(tdf, x="Date", y="Active", color='State')
    plot_div = plot(fig,output_type="div",link_text=False)
    return plot_div 
