import praw
import csv
from profanity import profanity
    
output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('videos')
#subreddit = r.get_subreddit('askscience')
subreddit_comments = subreddit.get_comments(limit=50)
myList = []

for comment in subreddit_comments:
	myList.append(comment.body)
	output_file.writerow([comment.body.encode('utf-8')])

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
profanityList = []
profanity_count =set()
with open('profanity-list.txt') as swearword:
  for someword in swearword:
    someword = someword.strip()
    profanityList.append(someword)

profanity_count.update(set(profanityList))
del profanityList

while i<L:
  redcomment= myList[i]
  if redcomment in profanity_count:
    profcount +=1

#print profanityList  
#print profanity_count  
#print profcount
print myList





#while i< L:
#  redcomment= myList[i]
#  if(profanity.contains_profanity(myList[i])==True):
#  	profcount +=1