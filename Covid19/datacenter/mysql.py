import datetime
import pandas as pd
import math
import mysql.connector
import sys

def daily_report(date_string):
    # Reports aggegrade data, dating as far back to 01-22-2020
    # If passing arg, must use above date formatting '01-22-2020'
    report_directory = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    
    if date_string is None: 
        yesterday = datetime.date.today() - datetime.timedelta(days=2)
        file_date = yesterday.strftime('%m-%d-%Y')
    else: 
        file_date = date_string 
    
    df = pd.read_csv(report_directory + file_date + '.csv', dtype={"FIPS": str})
    return df


"""[summary]: Creates a table on total statistics of all countries,
    sorted by confirmations.

    Returns:
        [pd.DataFrame]
    """ 
def global_report(date_string):
	df = daily_report(date_string)[['Country_Region', 'Confirmed', 'Recovered', 'Deaths', 'Active']]
	df.rename(columns={'Country_Region':'Country'}, inplace=True) 
	df = df.groupby('Country', as_index=False).sum()  # Dataframe mapper, combines rows where country value is the same
	df.sort_values(by=['Country'], ascending=False, inplace=True)

	rows=[]
	counter=0

	for i in df['Country']:
		s=df['Country'][counter]
		tc=int(df['Confirmed'][counter])
		td=int(df['Deaths'][counter])
		tr=int(df['Recovered'][counter])
		a=int(df['Active'][counter])
		if(math.isnan(tc)): tc=0
		if(math.isnan(td)): td=0
		if(math.isnan(tr)): tr=0
		if(math.isnan(a)): a=0
		tc=int(tc)
		td=int(td)
		tr=int(tr)
		a=int(a)
		rows.append((s,tc,td,tr,a))
		counter+=1  

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="django",
	  password="USER@123",
	  database="COVID19"
	)

	mycursor = mydb.cursor()
	sql1="DELETE FROM datacenter_world where country_name IS NOT NULL"
	mycursor.execute(sql1)
	mydb.commit()
	sql2 = "INSERT INTO datacenter_world (country_name,total_cases,total_deaths,total_recovered,active_cases) VALUES (%s,%s,%s,%s,%s)"
	mycursor.executemany(sql2,rows)
	mydb.commit()  # to save final changes
		
"""a = sys.argv[1].split('-')
year=int(a[2])
month=int(a[0])
day=int(a[1])
date1 = datetime.date(year, month, day)
date1=date1.strftime('%m-%d-%Y')
global_report(date1)
"""
