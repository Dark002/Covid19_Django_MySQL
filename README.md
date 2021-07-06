# Covid-19 Patient management or data visualization 
This is a django and mysql project for Course ITW-2

The project have 3 main components
  - Home page
  - Dashboard
  - Data-center

# To run project locally
First clone this repo using following command
```console
root@project:~$ git clone https://github.com/Dark002/Covid19_Django_MySQL.git
```

# Main-Requirements
  - Python 3.7 or 3.8 , you can also use anaconda
  - Django
  - mysql 

Other library packages used in this project are listed in requirements.txt

Install them by following command
```console
root@project:~$ pip install -r requirements.txt
```
It is preferred to create a virtual environemnt and install then install this packages in that environment.

Create a new user named django on local server with password 'USER@123'.
create database named COVID19.

Now we just need to run two commands before starting the project.
```console
root@project:-$ python manage.py makemigrations
root@project:-$ python manage.py migrate
```
 Now run the project using following command
 
```console
root@project:-$ python manage.py runserver
```

# Data Source
- Johns Hopkins University: [CSSE](https://systems.jhu.edu/) 2019-ncov data repository, found [here](https://github.com/CSSEGISandData/COVID-19).
- COVID19-India API ,found [here](https://api.covid19india.org/)
- COVID19 API by Kyle Redelinghuys ,found [here](https://covid19api.com/)

# Contributors
 - [Lakshay Jindal](https://github.com/Dark002)
 - [Jatin Garg](https://github.com/rivalq)




