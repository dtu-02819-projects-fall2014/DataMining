import praw
import csv
import os
import math
import re
import sys
import time
from datetime import date
from datafile_plotting import plotter

reload(sys)
sys.setdefaultencoding('utf-8')

SENTIMENT_RED = "reddit_sentiment.csv"
AFINN_FILE = 'AFINN-111.txt'

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
subredInCsv = True

if os.path.isfile(SENTIMENT_RED):
    os.remove(SENTIMENT_RED)

# make sure the "semantics" file exists
if not os.path.isfile(SENTIMENT_RED):
    with open(SENTIMENT_RED, "wb") as out_file:
        fieldnames = ['Subreddit', 'Sentiment Value']
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()

def write_comments(filename, comments):
    now = date.today()
    dateToday = "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)
    with open(filename + dateToday + '.csv', 'ab') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(comments)



def sentiment_reddit(comment_amount=200):
    new_subreddit = raw_input("Please enter new subreddit (videos, nfl, nhl, dogs, christianity, etc.): ")
    subreddit = new_subreddit
    while True:
        try:
            subreddit_name = r.get_subreddit(subreddit,fetch=True)
            subreddit_comments = subreddit_name.get_comments(limit=comment_amount)
        except:
            print "That is not a valid subreddit. Please try again"
            new_subreddit = raw_input("Please enter new subreddit ")
            subreddit = new_subreddit
            continue
        break
    
    
    subreddit_comments_list = []
    for comment in subreddit_comments:
        subreddit_comments_list.append(comment.body)
        write_comments(subreddit, [comment.body])
    
    subreddit_comments_list = map(lambda foo: foo.replace(".", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace(",", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("!", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("?", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("*", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("'", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("/", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("(", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace(")", ""), subreddit_comments_list)
    
    profanity_list = []
    with open('profanity-list-google.txt') as swearword:
        for someword in swearword:
            someword = someword.strip()
            profanity_list.append(someword)

    word_count = 0
    profanity_count = 0

    for redcomment in subreddit_comments_list:
        redcomment = redcomment.encode('utf-8')
        for word in redcomment.lower().split():
            word_count += 1
            print word
            if word in profanity_list:
            	profanity_count += 1

    afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(AFINN_FILE) ]))

    afinn_score = 0

    string_comments = ''.join(subreddit_comments_list)

    afinn_score = map(lambda word: afinn.get(word, 0), string_comments.lower().split())
    
    if afinn_score:
        #sentiment_score = float(sum(afinn_score))/math.sqrt(len(afinn_score))
        sentiment_score = float(sum(afinn_score))/len(afinn_score)
    else:
        sentiment_score = 0

    print "profanity count: " + str(profanity_count)
    print "total words: " + str(word_count)
    print "Afinn sentiment avg: " + str(sentiment_score)

    with open(SENTIMENT_RED, 'ab') as sm, open(SENTIMENT_RED, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(sm)
        for row in reader:
            if subreddit not in row[0]:
                subredInCsv = False
            else:
                subredInCsv = True
        if subredInCsv is False:
            writer.writerow([subreddit, sentiment_score])
        else:
            print "You have already fetched this subreddit."
            print "Try a different."

for x in range(0, 3):
    sentiment_reddit(comment_amount=200)

plotter(SENTIMENT_RED)
