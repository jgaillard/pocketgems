from scoring import user_scoring_function
from models.user import User
from models.story import Story
from models.read import Read
from mongoengine import connect
from display_helper import *

def recommend(user_id):
    user = User.objects.get(user_id=user_id)
    feed = [] # users could have a attribute feed in which we store the feed and refresh it daily or hourly.
    for story in Story.objects:
        score = user_scoring_function(user, story)
        if score:
            feed.append((score, story.title))
    feed.sort(reverse=True)
    display_feed(feed, user)
    return feed

def recommend_test(user_id):
    # used to perform a first test of the system
    user = User.objects.get(user_id=user_id)
    feed = []

    for story_title in user.stories:
        story = Story.objects.get(title=story_title)
        score = user_scoring_function(user, story)
        if score:
            real_score = user.stories[story_title] - user.avg_speed
            feed.append((score, story.title, real_score))

    feed.sort(reverse=True)
    display_feed_test(feed, user)
    return feed

if __name__ == '__main__':
    connect('pocketgems')
    recommend_test(12) # test on user 12
