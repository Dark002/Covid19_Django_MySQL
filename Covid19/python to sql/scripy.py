import datetime
import pandas as pd
import math

df=pd.read_csv("covid.csv") # csv file, you can also download directly from python 
df=df[['location','date','total_cases','total_deaths']]
df=dict(df)
rows=[]
counter=0

for i in df['date']:
    if(i=='2020-10-20'):
        s=df['location'][counter]
        tc=int(df['total_cases'][counter])
        td=df['total_deaths'][counter]
        if(math.isnan(td)):td=0
        td=int(td)
        rows.append((s,tc,td))
    counter+=1  


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="password",
  database="database"
)

mycursor = mydb.cursor()
sql = "INSERT INTO total_cases (country,total_case,total_death) VALUES (%s,%s,%s)"
mycursor.executemany(sql,rows)
mydb.commit()  # to save final changes




