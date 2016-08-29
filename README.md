#### Learning objectives:
- To get started with migration tools to handle changes in db schema (add/drop tables, add/drop columns)
- Practice customizing migration scripts (adding a table column where nullable=false)
- Incorporate external scripts using flask-script


#### Technologies Used:

- Alembic
- Flask-Script: support for writing external scripts in Flask
- Flask-SQLAlchemy
- Bootstrap, CSS, HTML, Postgres, Flask


#### Running locally:
Create a database by entering the following in terminal:

`createdb -h localhost -U <username> <nameofdb>`

To access db:

`psql -h localhost -U <username> <nameofdb>`

Create virtual environment and activate it:

`virualenv env`

`source env/bin/activate`

Install requirements:

`pip install -r requirements.txt`

Export app settings to environment:

`export APP_SETTINGS="config.DevelopmentConfig"`

Export db uri to environment:

`export DATABASE_URL="postgresql://<username>:<pasword>@localhost/alembicdb"`

To run server:

`python manage.py runserver`

If you make changes to you db schema, you can update the db by entering the following in terminal:

`python manage.py db migrate`

`python manage.py db upgrade`

To view app in browser, navigate to localhost:5000