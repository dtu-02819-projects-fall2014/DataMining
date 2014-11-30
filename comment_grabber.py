import praw
import csv
import string
import re
import os
import time

timeout = time.time() + 60*1440 #24 hours 60*180
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
if not os.path.isfile("comments.csv"):
    with open("comments.csv", 'wb') as open_file:
        open_file.write("comment")

if not os.path.isfile("comment_ids.csv"):
    with open("comment_ids.csv", 'wb') as id_file:
        id_file.write("ids")

def write_comments(comments):
    with open('comments.csv','ab') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(comments)

def write_ids(ids):
    with open('comment_ids.csv', 'wb') as id_append:
        id_writer = csv.writer(id_append)
        id_writer.writerow(ids)

# The function defines the words you want to search for,
# the subreddit and the amount of comments.
def grab(subreddit='all', comment_amount=10000):

    keep_on = False
    if keep_on is False:
        chosen_subreddit = r.get_subreddit(subreddit)
        submissions = r.get_subreddit(subreddit).get_comments(limit=comment_amount)
        keep_on = True

    # Appends the subreddit comments 'myList'
    myList = []
    already_done = open('comment_ids')
    #print 'before'
    #print already_done
    while keep_on is True:
        for comment in submissions:
            if comment.id not in already_done:
                myList.append(comment.body)
                write_comments([comment.body.encode('utf-8')])
                already_done.add(comment.id)
                write_ids(list(already_done))
            else:
        		keep_on = False
        if time.time() > timeout:
           print 'Done'
           break

grab(subreddit='Islam', comment_amount=5000)
