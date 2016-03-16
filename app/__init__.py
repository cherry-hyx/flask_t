import os

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import load_config

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
lm = LoginManager()
lm.init_app(app)
lm.session_protection = "strong"
lm.login_view = "login"

lm.login_message = u'test!!'
print app.config.get('basedir')

oid = OpenID(app, os.path.join(os.path.dirname(os.getcwd()), 'tmp'))

from . import views, models


if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(os.path.join(os.path.dirname(os.getcwd()), 'tmp')+'/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

