
import requests
from bs4 import BeautifulSoup

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
url = "https://covidindia.org/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)