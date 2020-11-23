from datetime import datetime
import pandas as pd
import os
import requests,json
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data/date.txt')
con_path = os.path.join(module_dir,'data/confirmed.csv')
rec_path = os.path.join(module_dir,'data/recovered.csv')
de_path = os.path.join(module_dir,'data/deaths.csv')
map_path = os.path.join(module_dir,'data/map.csv')
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
today = str(year)+'-'+str(month)+'-'+str(day)+'\n'
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_"
def save():
        df = pd.read_csv(url+'confirmed'+'_global.csv')
        df.to_csv(con_path,index=False)
        df = pd.read_csv(url+'deaths'+'_global.csv')
        df.to_csv(de_path,index=False)
        df = pd.read_csv(url+'recovered'+'_global.csv')
        df.to_csv(rec_path,index=False)
        data = requests.get('https://api.covid19api.com/summary')
        df = pd.DataFrame(data.json()['Countries'])
        df.to_csv(map_path,index=False)
def run():
    f = open(file_path,'r+')
    ls = "".join(list(f)).split("\n")
    if(ls[0]==''):
        save()
        f.write(today)
    else:
        st = ls[-2].split('-')
        pre_year = int(st[0])
        pre_month = int(st[1])
        pre_day = int(st[2])
        if(pre_year < year or pre_month < month or pre_day < day ):
            save()
            f.write(today)
    f.close()        
