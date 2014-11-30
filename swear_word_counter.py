import praw
import csv
import string
import re
import os
import time
# Define the desired name and destination for your .csv file
SWEAR_WORDS = "counted_swear_words.csv"
SEMANTIC_RED = "reddit_semantic.csv"

timeout = time.time() + 60*2

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

output_file = csv.writer(open("comments.csv", "ab",0), dialect='excel')
output_file.writerow(["comment"])

# The function defines the words you want to search for,
# the subreddit and the amount of comments.
def swear_word_count(word1, word2, word3, word4, word5, word6,
                     subreddit='all', comment_amount=10000):

    chosen_subreddit = r.get_subreddit(subreddit)
    amount = chosen_subreddit.get_comments(limit=comment_amount)
    inCsvBool = True
    subredInCsv = True

    # Appends the subreddit comments 'myList'
    myList = []
    #flat_comments = praw.helpers.flatten_tree(amount)
    already_done = set()
    #print 'before'
    #print already_done
    while True:
        for comment in amount:
            if comment.id not in already_done:
                myList.append(comment.body)
                output_file.writerow([comment.body.encode('utf-8')])
                already_done.add(comment.id)
            if time.time() > timeout:
                break
        time.sleep(5)
    #print 'after'
    #print already_done


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
            
                # make sure the "semantics" file exists
                if not os.path.isfile(SEMANTIC_RED):
                    with open(SEMANTIC_RED, "wb") as out_file:
                        fieldnames = ['Subreddit', 'Semantic Value']
                        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
                        writer.writeheader()
            
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
            
                # Converting our comments list to a string, lowercasing the string and
                # removing all punctuation so we can count occurences.
                stringMyList = ''.join(myList).encode('utf-8').lower()
                regex = re.compile('[%s]' % re.escape(string.punctuation))
                finalList = regex.sub(' ', stringMyList)
                del myList, stringMyList
            
                words = [word1, word2, word3, word4, word5, word6]
                comments = finalList
                prof_wordcount = dict((x, 0) for x in words)
                for w in re.findall(r"\w+", comments):
                    if w in prof_wordcount:
                        prof_wordcount[w] += 1
                print "Profanity word count: " + str(prof_wordcount)
                prof_wordcount.keys().insert(0, subreddit)
            
                # Make sure the "swear words" file exists. 
                # If not, we will make it here and assign the necessary headers.
                if not os.path.isfile(SWEAR_WORDS):
                    with open(SWEAR_WORDS, "wb") as out_file:
                        w = csv.DictWriter(out_file, fieldnames = prof_wordcount.keys())
                        out_file.write('Subreddit' + ',')
                        w.writeheader()
            
                # Outputs a .csv file with the profanity words as headers
                with open(SWEAR_WORDS, 'ab') as sw, open (SWEAR_WORDS, 'rt') as f:
                    reader = csv.reader(f, delimiter=',')
                    w = csv.DictWriter(sw, fieldnames = prof_wordcount.keys())
                    for row in reader:
                        if subreddit not in row[0]:
                            inCsvBool = False
                        else:
                            inCsvBool = True
                    if inCsvBool is False:
                        sw.write(subreddit + ",")
                        w.writerow(prof_wordcount)
                        print "Outputted " + "'" + SWEAR_WORDS + "'" + " to the folder."
                    else:
                        print "You have already fetched results from that subreddit." 
                        print "Please save the current file and make a new."

# Example usage:
swear_word_count('homo', 'faggot', 'gay', 'fag', 'queer', 'homosexual',
                  subreddit='Buddhism', comment_amount= 5000)
