import praw
import csv
from profanity import profanity


output_file = csv.writer(open("replies.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('videos')
hotSubmissions = subreddit.get_hot(limit=5)
replyList = []

def getReplies(comments):
  print ("Getting replies...")
  for comment in comments:
    #print comment.body
    output_file.writerow([comment.body.encode('utf-8')])
    replyList.append(comment.body)
    #getReplies(comment.replies)
    

for submission in hotSubmissions:
  print ("Processing...")
  submission.replace_more_comments(limit=None, threshold=0)
  getReplies(submission.comments)

print ("NOW TO SENTIMENT")

wordlist = []
with open('word_list.txt') as f:
  for line in f:
    wordlist.append(line.split('\t'))

dict = {}
for i in range(0,len(wordlist)):
  dict[wordlist[i][0]] = float(wordlist[i][1])
keywords = dict.viewkeys()

L = len(replyList)

words=0
i=0
profcount =0
score=0
while i< L:
  redcomment= replyList[i]
  if(profanity.contains_profanity(replyList[i])==True):
    profcount +=1
    
  for word in redcomment.split():
     word = word.lower()
     if word in keywords:
       score += dict[word]
       words +=1

  i+=1

print "Total words: " + str(words)
print "Profanity count: " + str(profcount) 
print "The average sentiment value is " + str(score/words)
