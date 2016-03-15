#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''
__author__ = 'cherry'

from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required
 
class LoginForm(Form):
    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)
