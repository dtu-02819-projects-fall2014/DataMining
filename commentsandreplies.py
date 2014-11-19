import praw

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('videos')
hotSubmissions = subreddit.get_hot(limit=20)

def getReplies(comments):
  for comment in comments:
    print comment.body
    getReplies(comment.replies)

for submission in hotSubmissions:
  submission.replace_more_comments(limit=None, threshold=0)
  getReplies(submission.comments)
