import praw
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')


subreddit = r.get_subreddit('videos')
subreddit_comments = subreddit.get_comments(limit=10)
for comment in subreddit_comments:
	print (comment.body)
