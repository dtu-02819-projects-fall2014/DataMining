import praw
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

comments = r.get_content("http://www.reddit.com/r/%s/comments" % subreddit, limit = 100)


print(submission)