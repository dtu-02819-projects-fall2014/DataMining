import praw
import csv
import string
import re
import os
import time

timeout = time.time() + 60*180
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
if not os.path.isfile("comments.csv"):
    with open("comments.csv", 'wb') as open_file:
        open_file.write("comment")

def write_comments(comments):
    with open('comments.csv','ab') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(comments)
        #output_file.write(comments)

# The function defines the words you want to search for,
# the subreddit and the amount of comments.
def grab(subreddit='all', comment_amount=10000):

    keep_on = False
    if keep_on is False:
        chosen_subreddit = r.get_subreddit(subreddit)
        amount = chosen_subreddit.get_comments(limit=comment_amount)
        keep_on = True

    # Appends the subreddit comments 'myList'
    myList = []
    already_done = set()
    #print 'before'
    #print already_done
    while keep_on is True:
        for comment in amount:
            #while comment.id not in already_done:
            if comment.id not in already_done:
                myList.append(comment.body)
                write_comments([comment.body.encode('utf-8')])
                #output_file.writerow([comment.body.encode('utf-8')])
                already_done.add(comment.id)
            else:
            	#chosen_subreddit = r.get_subreddit(subreddit)
        		#amount = chosen_subreddit.get_comments(limit=comment_amount)
        		keep_on = False

        if time.time() > timeout:
           print 'Done'
           break
        #time.sleep(120)
    #print 'after'
    #print already_done

grab(subreddit='Islam', comment_amount=5000)