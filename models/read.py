__author__ = 'julien'

from mongoengine import *

class Read(Document):
    user_id = IntField()
    story_title = StringField()
    chapter = IntField()
    timestamp = DateTimeField()
    device_type = StringField()
    meta = {
        'indexes' : [
            ('user_id',
			 'story_title')
        ],
		'collection': 'Read'
    }
