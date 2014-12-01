import praw
import csv
import string
import re
import os
import time

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
if not os.path.isfile("comments.csv"):
    with open("comments.csv", 'wb') as open_file:
        open_file.write("comment")

def write_comments(comments):
    with open('comments.csv','ab') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(comments)

# The function defines the words you want to search for,
# the subreddit and the amount of comments.
def grab(subreddit='all', comment_amount=10000):

    chosen_subreddit = r.get_subreddit(subreddit)
    submissions = r.get_subreddit(subreddit).get_comments(limit=comment_amount)
    keep_on = True

    # Appends the subreddit comments 'myList'
    myList = []
    already_done = set()
    for comment in submissions:
        if comment.id not in already_done:
            myList.append(comment.body)
            write_comments([comment.body.encode('utf-8')])
            already_done.add(comment.id)

grab(subreddit='Islam', comment_amount=5000)
