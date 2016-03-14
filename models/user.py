__author__ = 'julien'

from mongoengine import *

class User(Document):
    user_id = IntField(unique=True, required=True)
    stories = DictField(default={})
    reads = ListField(ReferenceField('Read'))
    avg_speed = FloatField(default=0)

    meta = {
        'indexes' : [
            ('user_id')
        ],
		'collection': 'User'
    }

    def average_speed():
        pass
