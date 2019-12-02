# Tangent-Solutions-API

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

### Browser application tests
- Type the following URLs in your browser URL bar.
- Home Page :-> `http://localhost:8000/#/`
- About-Us Page :-> `http://localhost:8000/#/about`
- Add New Carousel :-> `http://localhost:8000/#/carousel`
- Additional Contact-Us Page :-> `http://localhost:8000/#/contact`
- Delete button is available to delete a carousel on home page.


