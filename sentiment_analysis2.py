import praw
import csv
import os

SEMANTIC_RED = "reddit_semantic.csv"
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
    myList = []
    for comment in subreddit_comments:
        myList.append(comment.body)

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
    for i in range(0, len(wordlist)):
        wordDict[wordlist[i][0]] = float(wordlist[i][1])
    keywords = wordDict.viewkeys()

    words = 0
    profcount = 0
    score = 0

    for redcomment in myList:
        redcomment = redcomment.encode('utf-8')

    for word in redcomment.split():
        if word in profanityList:
            profcount += 1
        if word in keywords:
            score += wordDict[word]
            words += 1
    i += 1

    average_sentiment = str(score/words)

    with open(SEMANTIC_RED, 'ab') as sm, open(SEMANTIC_RED, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(sm)
        for row in reader:
            if subreddit not in row[0]:
                subredInCsv = False
            else:
                subredInCsv = True
            if subredInCsv is False:
                writer.writerow([subreddit, average_sentiment])
            else:
                print "You have already fetched this subreddit."
                print "Try a different."

semantic_reddit('videos', 200)
