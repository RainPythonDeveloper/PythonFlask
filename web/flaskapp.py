from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

# app object (literally web server)
app = Flask(__name__)



# # Adding SQLite3 database URI to a config
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///E:\VS Code Python\Project-ASS3\complex_example.db'

# # Adding PostgreSQL database URI to a config
# # pip install psycopg2
# app.config['SQLALCHEMY_DATABASE_URI'] = r"postgresql://postgres:postgres@localhost:5432/lecture7pt2"

# Adding PostgreSQL database URI to a config
# pip install pymysql
# app.config['SQLALCHEMY_DATABASE_URI'] = r'mysql+pymysql://root:root@localhost:3306/lecture7pt2'

with app.app_context():
    db.init_app(app)

# Used to create a session object
# user can look at the session contents, but can’t modify it 
# unless they know the secret key, so make sure to set that to something complex and unguessable.
app.config['SECRET_KEY']="my secret key here"

