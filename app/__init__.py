from flask import Flask
from config import load_config
from sqlalchemy import MetaData
from flask.ext.sqlalchemy import SQLAlchemy


app=Flask(__name__)
config = load_config()
app.config.from_object(config)
#print app.config.get('OPENID_PROVIDERS')
#print type(app.config.get('OPENID_PROVIDERS'))
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(app)

from app import views, models


