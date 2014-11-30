import praw
import csv
import os
import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SEMANTIC_RED = "reddit_semantic.csv"
AFINN_FILE = 'AFINN-111.txt'

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
subredInCsv = True

# make sure the "semantics" file exists
if not os.path.isfile(SEMANTIC_RED):
    with open(SEMANTIC_RED, "wb") as out_file:
        fieldnames = ['Subreddit', 'Semantic Value']
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()

output_file = csv.writer(open("comments.csv", "w", 0), dialect='excel')
output_file.writerow(["comment"])


def semantic_reddit(subreddit='all', comment_amount=200):

    subreddit_name = r.get_subreddit(subreddit)
    subreddit_comments = subreddit_name.get_comments(limit=comment_amount)
    
    subreddit_comments_list = []
    for comment in subreddit_comments:
        subreddit_comments_list.append(comment.body)

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

    with open(SEMANTIC_RED, 'ab') as sm, open(SEMANTIC_RED, 'rt') as f:
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

semantic_reddit('christianity', 200)
