import praw
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')


subreddit = r.get_subreddit('videos')
#subreddit_comments = subreddit.get_comments()
for comment in subreddit.get_comments(limit=100):
	print (comment.body)
