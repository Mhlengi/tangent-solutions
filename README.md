# Tangent-Solutions-API 
[Live REST API App](https://tangent-solutions.herokuapp.com/api/docs/)

## Requirements
- Python 3.7+
- PostgreSQL 9.6+

Please consult Google if you need to install any of the pre-requisites

## Installation
- Clone/Download the git repo - `git clone https://github.com/Mhlengi/tangent-solutions.git`.
- Create a Postgres database `db_tangent_solutions` with user `postgres` and password `postgres`
- Navigate to the project folder`tangent-solutions`
- Install python3 `brew install python3`
- Install pip3 `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate a virtual environment: `. venv/bin/activate`
- Install all the python dependencies `pip install -r requirements.txt`
- Run the database migrations `python manage.py migrate`
- Run collect static files `python manage.py collectstatic`
- Start the WebServer `python manage.py runserver`
(*Please note everytime you pull from master you may need to run the migrations and install any new dependencies
- as per the above instructions*)

### Running django pytest
`py.test -xvv --create-db`.

### Running django pytest with code-coverage report
`coverage run -m py.test -xvv --create-db; coverage html; coverage report;`

![PyTest Image](https://github.com/Mhlengi/tangent-solutions/blob/master/Screenshot%202019-12-02%20at%2012.39.34.png)

### Test Localhost Browser Application
- Access [localhost application](http://localhost:8000) on your browser.

### Test Heroku Live Browser Application
- Access heroku application [https://tangent-solutions.herokuapp.com](https://tangent-solutions.herokuapp.com) on your browser.
#### Swagger Docs
- Access swagger docs [https://tangent-solutions.herokuapp.com/api/docs/](https://tangent-solutions.herokuapp.com/api/docs/) on your browser.

### Application Demo or REST-API usage
```
To demonstrate REST-API's, We choosen Swagger docs or any other REST-API client(Example: Postman).
```
### Step 0: 
- Create/Register a normal system-user or super-user.
- By making a `POST` through the endpoint [https://tangent-solutions.herokuapp.com/api/accounts/register/](https://tangent-solutions.herokuapp.com/api/accounts/register/) on your browser. 
- With data payload as 
- `{
  "username": "admin",
  "first_name": "Joe",
  "last_name": "Doe",
  "email": "admin@gmail.com",
  "password": "admin12345",
  "password_confirm": "admin12345"
  }`
- OR curl command
`curl -X POST "https://tangent-solutions.herokuapp.com/api/accounts/register/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: xuHuB4OROKUzpieNt9q9prYDGyNVRiseb6caJlvKK90rTgyargsWq54eVNhzGT8c" -d "{ \"username\": \"admin\", \"first_name\": \"Joe\", \"last_name\": \"Doe\", \"email\": \"admin@gmail.com\", \"password\": \"admin12345\", \"password_confirm\": \"admin12345\"}"
`
- If you everything went well.      
- Response body with correct status code `201`
- `{
  "id": 1,
  "username": "admin",
  "first_name": "Joe",
  "last_name": "Doe",
  "email": "admin@gmail.com"
}
`

### Step 1: 
- Now we can make any system-user an company `Employee`.
- That can submit `Leave` requests applications through the system with valid dates.
- By making a `POST` through the endpoint [https://tangent-solutions.herokuapp.com/api/employee/](https://tangent-solutions.herokuapp.com/api/employee/) on your browser. 
- With data payload as 
- Note that `first_name` and `last_name` are not added in payload because were save during system user creation. 
- `{
  "user": 1,
  "phone_number": "+27723208261"
}`
- OR curl command
- `curl -X POST "https://tangent-solutions.herokuapp.com/api/employee/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: xuHuB4OROKUzpieNt9q9prYDGyNVRiseb6caJlvKK90rTgyargsWq54eVNhzGT8c" -d "{ \"user\": 1, \"phone_number\": \"+27723208261\"}"
`
- If you everything went well.      
- Response body with correct status code `201`
- `{
  "user": 1,
  "first_name": "Joe",
  "last_name": "Doe",
  "phone_number": "+27723208261"
}
`

### Step 2: 
- Now the `Employee` that was created at `Step 1` can apply for leave.
- By making a `POST` through the endpoint [https://tangent-solutions.herokuapp.com/api/v1/apply/employee/leave/](https://tangent-solutions.herokuapp.com/api/v1/apply/employee/leave/) on your browser. 
- `Note:` POST with valid dates and end-date must be greater than start-date. 
- Otherwise you can not submit `Leave` application.  
- With data payload as  
- `{
  "employee": 1,
  "status": "New",
  "days_of_leave": 15,
  "start_date": "2019-03-21",
  "end_date": "2019-04-21"
}`
- OR curl command
- `curl -X POST "https://tangent-solutions.herokuapp.com/api/v1/apply/employee/leave/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: xuHuB4OROKUzpieNt9q9prYDGyNVRiseb6caJlvKK90rTgyargsWq54eVNhzGT8c" -d "{ \"employee\": 1, \"status\": \"New\", \"days_of_leave\": 15, \"start_date\": \"2019-03-21\", \"end_date\": \"2019-04-21\"}"
`
- If you everything went well.      
- Response body with correct status code `201`
- `{
  "employee": 1,
  "status": "New",
  "days_of_leave": 15,
  "start_date": "2019-03-21",
  "end_date": "2019-04-21"
}
`

### Test Docker-Container Browser Application
- Loading...
