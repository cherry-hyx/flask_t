#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-

'''
Created on 2016年3月14日

@author: cherry
'''
__author__ = 'cherry'

if __name__ == '__main__' :
    from app import app
    #app=create_app()
    app.run(debug=True)
