from similarity import similarity_story
from similarity import similarity_user
from models.story import Story
from models.read import Read
from models.user import User

def user_scoring_function(user, story):

    previous_users_id = [r.user_id for r in Read.objects(story_title=story.title)]
    score_sum = 0
    denominator = 0

    for j in previous_users_id:
        previous_user = User.objects.get(user_id=j)
        rating_j = previous_user.stories[story.title]
        similarity = similarity_user(user, previous_user)
        if similarity:
            score_sum += similarity * (rating_j - previous_user.avg_speed)
            denominator += abs(similarity)

    if denominator!=0:
        return score_sum/float(denominator)

def story_scoring_function(user, story_to_rank):
    score_sum = 0
    denominator = 0
    for title in user.stories:
        story = Story.objects.get(title=title)
        similarity = similarity_story(story, story_to_rank)
        if similarity:
            score_sum += user.stories[title] * similarity
            denominator += similarity

    if denominator!=0:
        return score_sum/float(denominator)
