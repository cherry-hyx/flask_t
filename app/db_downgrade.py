#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''

from migrate.versioning import api

from config import load_config
config = load_config()
SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
SQLALCHEMY_MIGRATE_REPO = config.SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
