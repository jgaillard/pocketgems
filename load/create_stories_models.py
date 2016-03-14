from models.story import Story
from models.read import Read
from mongoengine import connect
from numpy import mean

connect("pocketgems")

def create_stories():
    for story in Story.objects:
        story_reads = Read.objects(story_title = story.title)
        story.reads = story_reads
        max_chapter = max([r.chapter for r in story_reads])
        story.users = [r.user_id for r in story_reads]
        story.max_chapter = max_chapter
        story.save()

if __name__ == '__main__':
    create_stories()
