import praw
import csv
from profanity import profanity
    


output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('cringepics')
#subreddit = r.get_subreddit('askscience')
subreddit_comments = subreddit.get_comments(limit=1)


myList[]
myList.append(subreddit_comments) 

print myList