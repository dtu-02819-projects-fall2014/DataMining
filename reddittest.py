

import praw
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

submissions = r.get_subreddit('videos').get_hot(limit=5)
print([str(x) for x in submissions])