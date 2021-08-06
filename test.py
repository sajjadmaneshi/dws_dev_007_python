
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

from logger import stdout_logger



db=SQLAlchemy()

app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
stdout_logger(app.config['SQLALCHEMY_DATABASE_URI'])
if __name__=="__main__":
    app.run();


