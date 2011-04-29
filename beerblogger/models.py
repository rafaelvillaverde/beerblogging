#coding: utf-8

import peewee
from . import app

from members import *

database = peewee.Database(peewee.SqliteAdapter(), app.config['DATABASE_NAME'])

class BlogEntry(peewee.Model):
    title =     peewee.CharField()
    eid =       peewee.CharField()
    link =      peewee.CharField()

    author_email = peewee.CharField()

    summary =   peewee.TextField() 
    tags =      peewee.CharField()
    content =   peewee.TextField()

    date =      peewee.DateTimeField()
    updated =   peewee.DateTimeField()
    
    class Meta:
        database = database

    @property
    def author(self):
        return Members().by_email(self.author_email)