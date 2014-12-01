import praw
import csv
import os
import re
import sys
from datetime import date
from datafile_plotting import plotter
import string

reload(sys)
sys.setdefaultencoding('utf-8')

SENTIMENT_RED = "reddit_sentiment.csv"
AFINN_FILE = 'AFINN-111.txt'

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
subredInCsv = True

if os.path.isfile(SENTIMENT_RED):
    os.remove(SENTIMENT_RED)

# Write the comments from the given subreddit to a file 
# and nameit after the name of the subreddit and date.

def write_comments(filename, comments):
    now = date.today()
    dateToday = "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)

    with open(filename + dateToday + '.csv', 'ab') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(comments)

def sentiment_reddit(comment_amount=200, word1='gay', word2='homo', word3='love', word4='sex', word5='prayer', word6='meditation'):
    words = []
    new_subreddit = raw_input("Please enter new subreddit (videos, nfl, nhl, dogs, christianity, etc.): ")
    subreddit = new_subreddit
    if subreddit == 'exit':
        sys.exit('You have exited')

    # Run the function for each of the given subreddit.
    while True:
        try:
            subreddit_name = r.get_subreddit(subreddit, fetch=True)
            subreddit_comments = subreddit_name.get_comments(limit=comment_amount)
        except:
            print "That is not a valid subreddit. Please try again"
            new_subreddit = raw_input("Please enter new subreddit ")
            subreddit = new_subreddit
            continue
        break

    # Run through all comments and store them in a list.
    subreddit_comments_list = []
    for comment in subreddit_comments:
        subreddit_comments_list.append(comment.body)
        write_comments(subreddit, [comment.body])

    # Clears the list for special characters, for later analysis.
    subreddit_comments_list = map(lambda foo: foo.replace(".", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace(",", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("!", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("?", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("*", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("'", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("/", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace("(", ""), subreddit_comments_list)
    subreddit_comments_list = map(lambda foo: foo.replace(")", ""), subreddit_comments_list)

    # Run through the list of profanity and store them in a list.
    profanity_list = []
    with open('profanity-list-google.txt') as swearword:
        for someword in swearword:
            someword = someword.strip()
            profanity_list.append(someword)

    # Run through the commentlist and count profanity.
    word_count = 0.0
    profanity_count = 0.0

    for redcomment in subreddit_comments_list:
        redcomment = redcomment.encode('utf-8')
        for word in redcomment.lower().split():
            word_count += 1
            if word in profanity_list:
                profanity_count += 1

    prof_score = (float(profanity_count)/word_count)*100
    prof_score_list = [prof_score]

    # Use AFINN-111.txt and make a dict with words and their coresponding sentiment values. 
    afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(AFINN_FILE)]))

    # Convert the list of comments to a string, get sentiment value for each word 
    # and calculate an estimated sentimen average. 
    afinn_score = 0
    string_comments = ''.join(subreddit_comments_list)
    afinn_score = map(lambda word: afinn.get(word, 0), string_comments.lower().split()) 

    if afinn_score:
        # sentiment_score = float(sum(afinn_score))/math.sqrt(len(afinn_score))
        sentiment_score = float(sum(afinn_score))/len(afinn_score)
    else:
        sentiment_score = 0

    print "profanity count: " + str(profanity_count)
    print "total words: " + str(word_count)
    print "profscore: " + str(prof_score)
    print "Afinn sentiment avg: " + str(sentiment_score)

    # Convert list to string in order to count the frequency of selected words.
    stringMyList = ''.join(subreddit_comments_list).encode('utf-8').lower()
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    finalList = regex.sub(' ', stringMyList)
    # del myList, stringMyList
    words = [word1, word2, word3, word4, word5, word6]
    comments = finalList
    prof_wordcount = dict((x, 0) for x in words)
    for w in re.findall(r"\w+", comments):
        if w in prof_wordcount:
            prof_wordcount[w] += 1
    # print "Profanity word count: " + str(prof_wordcount)

    prof_wordcount.keys().insert(0, subreddit)

    for key,value in prof_wordcount.items():
        prof_wordcount[key] = (float(value)/word_count)*100

    # Make sure the "SENTIMENT_RED" file exists.
    if not os.path.isfile(SENTIMENT_RED):
        with open(SENTIMENT_RED, "wb") as out_file:
            fieldnames = ['Subreddit', 'Sentiment Value'] + prof_wordcount.keys() + ['Profanity Score']
            writer = csv.DictWriter(out_file, fieldnames=fieldnames)
            writer.writeheader()

    # Write all the values to the SENTIMENT_RED file for plotting.
    with open(SENTIMENT_RED, 'ab') as sm, open(SENTIMENT_RED, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(sm)
        w = csv.DictWriter(sm, fieldnames=prof_wordcount.keys())
        for row in reader:
            if subreddit not in row[0]:
                subredInCsv = False
            else:
                subredInCsv = True
        if subredInCsv is False:
            writer.writerow([subreddit, sentiment_score] + prof_wordcount.values() + prof_score_list)
        else:
            print "You have already fetched this subreddit."
            print "Try a different."
    return words

for x in range(0, 3):
    sentiment_reddit(comment_amount=200)
    # , word1 = word1, word2 = word2, word3 =word3, word4=word4, word5 = word5, word6 = word6)

plotter(SENTIMENT_RED, chosen_words=sentiment_reddit())
