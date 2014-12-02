import praw
import csv
import os
import sys
from datafile_plotting import plotter
from analysis import reddit_anal

reload(sys)
sys.setdefaultencoding('utf-8')

REDDIT_SENTIMENT_FILE = 'csv_files/reddit_sentiment.csv'
AFINN_FILE = 'word_lists/AFINN-111.txt'
PROFANITY_LIST_FILE = 'word_lists/profanity-list-google.txt'
CSV_FOLDER = 'csv_files'

if os.path.isfile(REDDIT_SENTIMENT_FILE):
    os.remove(REDDIT_SENTIMENT_FILE)

if not os.path.exists(CSV_FOLDER):
    os.makedirs(CSV_FOLDER)

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
subredInCsv = True


def sentiment_reddit(comment_amount=200,
                     word1='gay', word2='homo', word3='love',
                     word4='sex', word5='prayer', word6='meditation'):

    new_subreddit = raw_input("Please enter new subreddit\n"
                              "(videos, nfl, dogs, christianity, etc.).\n"
                              "Or you can type 'exit' to quit the program: ")
    subreddit = new_subreddit
    if subreddit == 'exit':
        exit('You have exited')

    # Check if input is a valid subreddit.
    while True:
        try:
            subreddit_name = r.get_subreddit(subreddit, fetch=True)
            subreddit_comments = subreddit_name.get_comments(
                limit=comment_amount)
        except:
            print "That is not a valid subreddit. Please try again"
            new_subreddit = raw_input("Please enter new subreddit ")
            subreddit = new_subreddit
            continue
        break

    words = [word1, word2, word3, word4, word5, word6]
    subreddit_comments_list, word_count, sentiment_score, \
        prof_score_list, profanity_count, prof_score, prof_wordcount = \
        reddit_anal(subreddit_comments, word1, word2, word3,
                    word4, word5, word6)

    # Make sure the correct subreddit name is inserted after the values
    prof_wordcount.keys().insert(0, subreddit)

    # Make sure the "REDDIT_SENTIMENT_FILE" file exists.
    if not os.path.isfile(REDDIT_SENTIMENT_FILE):
        with open(REDDIT_SENTIMENT_FILE, "wb") as out_file:
            fieldnames = ['Subreddit', 'Sentiment Value'] + \
                prof_wordcount.keys() + ['Profanity Score']
            writer = csv.DictWriter(out_file, fieldnames=fieldnames)
            writer.writeheader()

    # Write all the values to the REDDIT_SENTIMENT_FILE file for plotting.
    with open(REDDIT_SENTIMENT_FILE, 'ab') as sm,   \
            open(REDDIT_SENTIMENT_FILE, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(sm)
        for row in reader:
            if subreddit not in row[0]:
                subredInCsv = False
            else:
                subredInCsv = True
        if subredInCsv is False:
            writer.writerow([subreddit, sentiment_score] +
                            prof_wordcount.values() + prof_score_list)
        else:
            print "You have already fetched this subreddit."
            print "Try a different."
    return words

for x in range(0, 3):
    sentiment_reddit(comment_amount=200)

plotter(REDDIT_SENTIMENT_FILE, chosen_words=sentiment_reddit())
