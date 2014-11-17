import praw
import csv

output_file = csv.writer(open("comments.csv", "w",0), dialect='excel')
output_file.writerow(["comment"])

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('funny')
subreddit_comments = subreddit.get_comments(limit=1)
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
score=0
while i< L:
  redcomment= myList[i]
  for word in redcomment.split():
     word = word.lower()
     if word in keywords:
       score += dict[word]
       #print word
       words +=1

  i+=1

#print results
print "The average sentiment value is " + str(score/words)



#for c in myList:
#	print c

