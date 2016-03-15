#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''
__author__ = 'cherry'

from flask import Flask
from flask import abort
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import request, redirect

from app import app
from forms import LoginForm


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }  # fake user
    return render_template("index.html",
        title='Home',
        user=user)

@app.route('/test', methods=['GET'])
def test():
    user = { 'nickname': 'Miguel' }  # fake user
    posts = [  # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index2.html",
        title='Home',
        user=user,
        posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title='Sign In',
        form=form,
        providers=app.config['OPENID_PROVIDERS'])
