from mongoengine import *
from models.user import User
from models.read import Read
from models.story import Story
from numpy import mean

connect("pocketgems")

def create_users():
    for user in User.objects:
        user_reads = Read.objects(user_id = user.user_id)
        user.reads = user_reads
        user.stories, user.avg_speed = create_user_stories(user_reads)
        user.save()

def create_user_stories(user_reads):
    dict_stories = {}
    user_stories = {}
    list_speed_of_progression = []

    for r in user_reads:
        try:
            dict_stories[r.story_title].append((r.chapter, r.timestamp))
        except KeyError:
            dict_stories[r.story_title] = [(r.chapter, r.timestamp)]

    for story in dict_stories:
        chapter_reads = dict_stories[story]
        try:
            story_object = Story.objects.get(title = story)
        except DoesNotExist:
            continue
        max_chapter = story_object.max_chapter

        if len(chapter_reads)>1:
            chapter_reads.sort()

            first_chapter_read = chapter_reads[0][0]
            last_chapter_read = chapter_reads[-1][0]
            number_chapters_read = last_chapter_read - first_chapter_read

            progression = number_chapters_read/float(max_chapter)

            first_chapter_date = chapter_reads[0][1]
            last_chapter_date = chapter_reads[-1][1]

            timedelta = (last_chapter_date - first_chapter_date)
            timedelta_chapters = timedelta.days*24*60 + timedelta.seconds/float(60) # in minutes

            if timedelta_chapters!=0:
                speed_of_progression = progression/timedelta_chapters
                user_stories[story] = speed_of_progression
            else:
                speed_of_progression = 0
                user_stories[story] = 0
            '''
            Note: we could store a data structure that saves the number_chapters,
            timedelta_chapters and last_chapter_date to update easily the speed of progression
            as the user reads more chapters
            '''
            list_speed_of_progression.append(speed_of_progression)

    average_speed_of_progression = mean(list_speed_of_progression)
    return user_stories, average_speed_of_progression

if __name__ == '__main__':
    create_users()
