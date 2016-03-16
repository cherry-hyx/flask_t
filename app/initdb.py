#!/usr/local/bin/python2.7
# -*-encoding: utf-8-*-
'''
Created on 2016年3月14日

@author: cherry
'''


from app import models

#u = models.User(nickname='john', email='john@email.com', role=models.ROLE_USER)
#db.session.add(u)
#u = models.User(nickname='susan', email='susan@email.com', role=models.ROLE_USER)
#db.session.add(u)
#db.session.commit()
#u = models.User.query.get(1)
#p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
#db.session.add(p)
#db.session.commit()


users = models.User.query.all()
for x in users:
    print x.nickname


#for u in users:
#    db.session.delete(u)