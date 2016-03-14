import settings

def similarity_user(u, v):
    intersection = list(set(u.stories.keys()).intersection(set(v.stories.keys())))
    size = len(intersection)

    similarity_sum = 0
    denominator = 0

    if size>settings.MIN_SIZE_INTERSECTION:
        for story in intersection:
            r_u = u.stories[story] - u.avg_speed
            r_v = v.stories[story] - v.avg_speed
            similarity_sum += abs(r_u - r_v)
            denominator += 1

        result = 1 - similarity_sum/float(denominator*settings.MAX_DIFFERENCE)
        return result

def similarity_story(s1, s2):
    '''This function is equivalent to the jaccard index'''
    intersection = list(set(s1.users).intersection(set(s2.users)))
    size = len(intersection)
    union = len(s1.users) + len(s2.users) - size
    if size!=0:
        return size/float(union)
