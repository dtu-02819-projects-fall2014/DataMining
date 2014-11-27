import praw
import csv
from profanity import profanity
    
output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('cringepics')
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

print profanityList    

dict = {}
for i in range(0,len(wordlist)):
  dict[wordlist[i][0]] = float(wordlist[i][1])
keywords = dict.viewkeys()

L = len(myList)

words=0
i=0
profcount =0
score=0

specificSwearWords = ['the','in','gay','homo','homosexual','queer']


wordfreq = 0


while i< L:
  redcomment= myList[i]
  
  redcomment = redcomment.encode('utf-8')
  print redcomment



  for word in redcomment.split():
     
    if word in specificSwearWords:
      wordfreq +=1
    if word in profanityList:
      profcount +=1
    if word in keywords:
      score += dict[word]
      words +=1

  i+=1

print "wordsadd: " + str(wordfreq)
print "Total words: " + str(words)
print "Profanity count: " + str(profcount)
print "The average sentiment value is " + str(score/words)

