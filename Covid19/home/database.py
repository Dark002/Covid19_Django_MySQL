import datetime
import platform

import pandas as pd

if platform.system() == 'Linux':
    STRFTIME_DATA_FRAME_FORMAT = '%-m/%-d/%y'
elif platform.system() == 'Windows':
    STRFTIME_DATA_FRAME_FORMAT = '%#m/%#d/%y'
else:
    STRFTIME_DATA_FRAME_FORMAT = '%-m/%-d/%y'


def daily_report(date_string=None):
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

