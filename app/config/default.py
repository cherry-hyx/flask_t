#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''
__author__ = 'cherry'

class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    OPENID_PROVIDERS = [
        { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
        { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
        { 'name': 'AOL', 'url': 'http://openid.aol.com/ttt' },
        { 'name': 'Flickr', 'url': 'http://www.flickr.com/ttt' },
        { 'name': 'openoid', 'url': 'http://cherryhz.openid.org.cn/' }]

    import os
    basedir = os.path.abspath(os.path.dirname(__file__))
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径。
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    #SQLALCHEMY_MIGRATE_REPO 是用来存储SQLAlchemy-migrate数据库文件的文件夹
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = None
    MAIL_PASSWORD = None

    # administrator list
    ADMINS = ['you@example.com']
    @staticmethod
    def init_app(app):
        pass

# development.py
class DevelopmentConfig(Config):
    pass

# production.py
class ProductionConfig(Config):
    pass

# testing.py
class TestingConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': Config
}