__author__ = 'julien'

from mongoengine import *

class Story(Document):
    title = StringField(required=True, unique=True)
    users = ListField()
    reads = ListField(ReferenceField('Read'))
    max_chapter = IntField()

    meta = {
        'indexes' : [
            ('title')
        ],
		'collection': 'Story'
    }
