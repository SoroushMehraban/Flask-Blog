# Flask blog
This project is my first flask project. It's based on [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) series of videos on YouTube.

# Important notes
### Setup
Before running the project, we need to set the environment variable `FLASK_APP`. the command on windows is `set` and on
linux it's `export`. So we have to write the following command:  
`set FLASK_APP=<MAIN_FILE>`
### DEBUG
To enable the debug mode, we have to write the following command:  
`set FLASK_DEBUG=1`
### Running the project
`flask run`
### Form Validation
`pip install flask-wtf`   
`pip install email_validator`
### ORM
`pip install flask-sqlalchemy`
#### Creating tables
1. Open shell
2. `from <FILE> import db`
3. db.create_all()
#### Creating instances
1. `<VARIABLE> = <MODEL>(<FIELDS>)`
2. `db.session.add(<VARIABLE>)`
3. `db.session.commit()`
#### Query
- `<MODEL>.query.all()`
- `<MODEL>.query.first()`
- `<MODEL>.query.filter_by(<FIELD>=<VALUE>).all()`
- `<MODEL>.query.get(<ID>)`
#### Delete all the tables
`db.drop_all()`
