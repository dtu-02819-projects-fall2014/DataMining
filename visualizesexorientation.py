import praw
import csv
from profanity import profanity
from collections import Counter
import string
import re
import os
import pylab as pl
import numpy as np
    
SWEAR_WORDS = "counted_swear_words.csv"
# make sure the "swear words" file exists
if not os.path.isfile(SWEAR_WORDS):
  with open(SWEAR_WORDS, "w") as out_file:
    out_file.write("")

output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

#subreddit = r.get_subreddit('Christianity')
subreddit = r.get_subreddit('islam')
#subreddit = r.get_subreddit('askscience')
subreddit_comments = subreddit.get_comments(limit=2000)
myList = []

for comment in subreddit_comments:
	myList.append(comment.body)
	output_file.writerow([comment.body.encode('utf-8')])

wordlist = []
with open('word_list.txt') as f:
  for line in f:
    wordlist.append(line.split('\t'))

profanityList = []
with open('profanity-list-google.txt') as swearword:
  for someword in swearword:
    someword = someword.strip()
    profanityList.append(someword)

#print profanityList    

dict = {}
for i in range(0,len(wordlist)):
  dict[wordlist[i][0]] = float(wordlist[i][1])
keywords = dict.viewkeys()

L = len(myList)

words=0
i=0
profcount =0
score=0

specificSwearWords = ["gay","god","fuck","homo"]


wordfreq = 0


while i< L:
  redcomment= myList[i]
  
  redcomment = redcomment.encode('utf-8')
  #print redcomment



  for word in redcomment.split():
     
    if word in specificSwearWords:
      wordfreq +=1
    if word in profanityList:
      profcount +=1
    if word in keywords:
      score += dict[word]
      words +=1

  i+=1

#wordcount_swear = dict((x,0) for x in specificSwearWords)
#for w in re.findall(r"\w+", myList):
#    if w in wordcount_swear:
#        wordcount_swear[w] += 1

#Converting our comments list to a string so we can count occurences

stringMyList = ''.join(myList).encode('utf-8').lower()
#lowerList = stringMyList.lower()
regex = re.compile('[%s]' % re.escape(string.punctuation))
finalList = regex.sub(' ', stringMyList)

def count_many(needles, haystack):
    count = Counter(haystack.split())
    print {key: count[key] for key in count if key in needles}
    counted_words = {key: count[key] for key in count if key in needles}
    with open(SWEAR_WORDS, 'wb') as sw:
      sw.write("\n" + str(counted_words))
      #sw.write("\n".join(str(x) for x in key))
    
    X = np.arange(len(counted_words))
    pl.bar(X, counted_words.values(), align='center', width=0.5)
    pl.xticks(X, counted_words.keys())
    ymax = max(counted_words.values()) + 1
    pl.ylim(0, ymax)
    pl.show()
    


#print finalList
count_many(specificSwearWords, finalList)


#print "wordsadd: " + str(wordfreq)
#print "Total words: " + str(words)
#print "Profanity count: " + str(profcount)
#print "The average sentiment value is " + str(score/words)



