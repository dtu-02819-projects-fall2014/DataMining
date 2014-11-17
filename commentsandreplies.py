import praw
import csv
from profanity import profanity
    


output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('cringepics')
#subreddit = r.get_subreddit('askscience')
subreddit_comments = subreddit.get_comments(limit=1)
subreddit_replies = subreddit.get_comments.replies(limit=2)
myList = []
repList = []

for comment in subreddit_comments:
	myList.append(comment.body)
	output_file.writerow([comment.body.encode('utf-8')])

for comment in subreddit_replies:
	repList.append(comment.replies)
	#output_file.writerow([comment.replies.encode('utf-8')])

wordlist = []
with open('word_list.txt') as f:
  for line in f:
    wordlist.append(line.split('\t'))

dict = {}
for i in range(0,len(wordlist)):
  dict[wordlist[i][0]] = float(wordlist[i][1])
keywords = dict.viewkeys()

L = len(myList)

words=0
i=0
profcount =0
score=0
while i< L:
  redcomment= myList[i]
  if(profanity.contains_profanity(myList[i])==True):
  	profcount +=1
    
  for word in redcomment.split():
     word = word.lower()
     if word in keywords:
       score += dict[word]
       words +=1

  i+=1

print profcount
print "The average sentiment value is " + str(score/words)
print repList


#for c in myList:
#	print c

