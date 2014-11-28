import praw
import csv
from profanity import profanity
from collections import Counter
import string
import re
import os
import pylab as pl
import numpy as np

output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('all')
subreddit_comments = subreddit.get_comments(limit=20)
myList = []

for comment in subreddit_comments:
	myList.append(comment.body)
	output_file.writerow([comment.body.encode('utf-8')])

# Sentiment analysis word list
wordlist = []
with open('word_list.txt') as f:
  for line in f:
    wordlist.append(line.split('\t'))

# Googles profanity word list
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
wordFreq = 0
specificSwearWords = ["allah","god","fuck","homo","gay"]

for redcomment in myList:
    redcomment = redcomment.encode('utf-8')

    for word in redcomment.split():
        if word in specificSwearWords:
            wordFreq +=1
        if word in profanityList:
            profcount +=1
        if word in keywords:
            score += wordDict[word]
            words +=1

    i+=1

print "Total of specified swear words: " + str(wordFreq)
print "Total words: " + str(words)
print "Profanity count: " + str(profcount)
print "The average sentiment value is " + str(score/words)
