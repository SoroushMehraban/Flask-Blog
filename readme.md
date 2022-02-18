# Flask blog

This project is my first flask project. It's based
on [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) series of videos
on YouTube.

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

### Password encryption

1. `pip install flask-bcrypt`
2. `from flask_bcrypt import Bcrypt`
3. `bcrypt = Bcrypt(<APP>)`
4. `bcrypt.generate_password_hash('<PASSWORD>').decode('utf-8')`  
   **Note that hash is always different. even on the same password. So how to verify?**   
   `bcrypt.check_password_hash(<hashed_password>, <password>)`

### Login

1. `pip install flask-login`
2. On `__init__.py` file, add `login_manager = LoginManager(app)`
3. On `models.py`, import `login_manager`.
4. Now Extension needs to know to find a user by ID. So we create a `def load_user(user_id)` that gets a user from
   database by ID. Then we add the `@login_manager.user_loader` decorator.
5. The extension expects our user model to have certain attributes: `is_authenticated`, `is_active`, `is_anonymous`
   , `get_id()`. Therefore, we can import `UserMixin` from `flask_login` and finally our user model inherits from that.

### Pagination

- `posts = Post.query.paginate()`
- `posts.per_page`: Items per page
- `posts.page`: current page
- `for post in posts.items`: iterate over page items
- `posts = Post.query.paginate(page=2)`: get the second page's items.
- `posts = Post.query.paginate(per_page=5)`: 5 posts per page.
- `posts.total`: Total number of posts in all pages.
- `for page_number in posts.iter_pages(left_edge=1, right_edge=1, left_current=1, right_current=2)`: iterate over page
  numbers

### Generate time-sensitive token

1. `from itsdangerous import TimedJSONWebSignatureSerializer as Serializer`
2. `s = Serializer('secret_key_here', expires_in=30)`  # expires in 30 seconds.
3. `token = s.dumps({"user_id": 1}).decode('utf-8')`
4. `s.loads(token)`  # works only within 30 seconds.

### Send emails
1. 'pip install flask-mail'
2. On `__init__.py` file, add `app.config['MAIL_SERVER'] = 'smtp.gmail.com'` (or your host's smtp server)
3. Add `app.config['MAIL_PORT'] = 587`
4. Add `app.config['MAIL_USE_TLS'] = True`
5. Add `app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')`
6. Add `app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')`
7. Add `mail = Mail(app)`
