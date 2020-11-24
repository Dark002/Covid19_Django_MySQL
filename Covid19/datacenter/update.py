from datetime import datetime
import pandas as pd
import os
import requests,json
import mysql.connector
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
def database(df):
    mydb = mysql.connector.connect(
	  host="localhost",
	  user="django",
	  password="USER@123",
	  database="COVID19")
    mycursor = mydb.cursor()
    mycursor.execute('create table if not exists world_data (Country varchar(255),CounrtyCode varchar(10),slug varchar(255),NewConfirmed int,TotalConfirmed int,NewDeaths int,TotalDeaths int,NewRecovered int,TotalRecovered int,Date varchar(255))')
    mycursor.execute('DELETE from india_data')
    df.drop(columns=['Premium'],inplace=True,axis=1)
    sql = "INSERT INTO world_data (Country,CounrtyCode,slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered,Date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    ls = []
    for i,row in df.iterrows():
	    ls.append(tuple(row))
    mycursor.executemany(sql,ls)
    mydb.commit()
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
        database(df)
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
