#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''
__author__ = 'cherry'

from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import StringField, BooleanField,TextAreaField

from models import User


class LoginForm(Form):
    openid = StringField(u'Full Name', [validators.required(), validators.length(max=80)])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(Form):
    nickname = StringField(u'nickname', [validators.required(), validators.length(max=80)])
    about_me = TextAreaField(u'about_me', [validators.required(), validators.length(max=80)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True