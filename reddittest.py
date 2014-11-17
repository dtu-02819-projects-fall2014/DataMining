

import praw
r = praw.Reddit(user_agent='my_cool_application')

submissions = r.get_subreddit('videos').get_hot(limit=5)
print([str(x) for x in submissions])