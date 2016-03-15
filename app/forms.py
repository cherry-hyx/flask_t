#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''
__author__ = 'cherry'

from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField
from wtforms import validators
 
class LoginForm(Form):
    openid = StringField(u'Full Name', [validators.required(), validators.length(max=80)])
    remember_me = BooleanField('remember_me', default=False)
