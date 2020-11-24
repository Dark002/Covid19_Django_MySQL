from datetime import datetime
import pandas as pd
import os
import requests,json
import mysql.connector
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'data/date.txt')
act_path = os.path.join(module_dir,'data/active.csv')
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
today = str(year)+'-'+str(month)+'-'+str(day)+'\n'
url = "https://api.covid19india.org/csv/latest/states.csv"
def database(df):
    mydb = mysql.connector.connect(
	  host="localhost",
	  user="django",
	  password="USER@123",
	  database="COVID19")
    mycursor = mydb.cursor()
    mycursor.execute('create table if not exists india_data (Date varchar(20),State varchar(200),Confirmed int,Recovered int,Deceased int)')
    mycursor.execute('DELETE from india_data')
    df.drop(columns=['Other','Tested'],inplace=True,axis=1)
    sql = "INSERT INTO india_data (Date,State,Confirmed,Recovered,Deceased) VALUES(%s,%s,%s,%s,%s)"
    ls = []
    for i,row in df.iterrows():
	    ls.append(tuple(row))
    mycursor.executemany(sql,ls)
    mydb.commit()
def save():
       df  = pd.read_csv(url)
       df.to_csv(act_path,index=False)
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
