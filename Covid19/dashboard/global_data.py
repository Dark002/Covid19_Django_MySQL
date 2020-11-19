import plotly.express as px
import pandas as pd
import json
import requests


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
                        height=600

                       ).update_layout(clickmode='event+select')
    fig.show()                   


get_map()    