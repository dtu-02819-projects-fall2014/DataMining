import praw
import csv
from profanity import profanity
from collections import Counter
import string
import re
import os
import pylab as pl
import numpy as np
import pandas as pd
from pandas import DataFrame
    
SEMANTIC_RED = "reddit_semantic.csv"
# make sure the "swear words" file exists
if not os.path.isfile(SEMANTIC_RED):
  with open(SEMANTIC_RED, "wb") as out_file:
    out_file.write("Subreddit" + ',' + 'Semantic Value')

output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

def semantic_reddit(subreddit='all', comment_amount=200):

  subreddit_name = r.get_subreddit(subreddit)
  subreddit_comments = subreddit_name.get_comments(limit=comment_amount)
  myList = []
  for comment in subreddit_comments:
    myList.append(comment.body)
    #output_file.writerow([comment.body.encode('utf-8')])

  wordlist = []
  with open('word_list.txt') as f:
    for line in f:
      wordlist.append(line.split('\t'))

  profanityList = []
  with open('profanity-list-google.txt') as swearword:
    for someword in swearword:
      someword = someword.strip()
      profanityList.append(someword)

  wordDict = {}
  for i in range(0,len(wordlist)):
    wordDict[wordlist[i][0]] = float(wordlist[i][1])
  keywords = wordDict.viewkeys()

  words=0
  profcount =0
  score=0
  wordfreq = 0

  for redcomment in myList:
    redcomment = redcomment.encode('utf-8')

    for word in redcomment.split():
      if word in profanityList:
        profcount +=1
      if word in keywords:
        score += wordDict[word]
        words +=1
    i+=1

  average_sentiment = str(score/words)
  print average_sentiment

    with open(SEMANTIC_RED, 'ab') as sm:
      writer = csv.writer(sm, delimiter=',')
      sm.write(subreddit + ",")
      #writer = csv.DictWriter(sm, fieldnames = ['Subreddit', 'Semantic Value'])
      #writer.writeheader()
      #writer.writerow(average_sentiment)
      writer.writerow(average_sentiment)

semantic_reddit('cringepics', 20)
