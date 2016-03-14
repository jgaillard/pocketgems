def display_feed(feed, user):
    print('Recommendations for user', user.user_id)
    for score, story in feed:
        print(score, '\t', story)

def display_feed_test(feed, user):
    print('Recommendations for user', user.user_id)
    for predicted_score, story, real_score in feed:
        print(predicted_score, '\t', real_score, '\t', story)
