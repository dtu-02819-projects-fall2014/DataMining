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


# def sentiment_reddit(comment_amount=200, word1='gay', word2='homo', word3='love', word4='sex', word5='prayer', word6='meditation'):
def sentiment_reddit(comment_amount, words_of_interest):
    word1 = words_of_interest[0]
    word2 = words_of_interest[1]
    word3 = words_of_interest[2]
    word4 = words_of_interest[3]
    word5 = words_of_interest[4]
    word6 = words_of_interest[5]

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


words_of_interest = []
for x in range (0,6):
	x = raw_input('Enter word of interest (' + str(x + 1) +'/6): ')
	words_of_interest.append(x)

comment_amount = 200
# print words_of_interest

subreddit_name_list =[]
for x in range (0, 3):
    subreddit_input = raw_input("Enter subreddit: ")

    if subreddit_input == 'exit':
        exit('You have exited')

    subreddit_name_list.append(subreddit_input)
    while True:
        try:
            subreddit_name = r.get_subreddit(subreddit_input, fetch=True)
        except:
            print "That is not a valid subreddit. Please try again"
            new_subreddit = raw_input("Please enter new subreddit ")
            subreddit_input = new_subreddit
            continue
        break


print subreddit_name_list

for x in range (0, 3):
    new_subreddit = subreddit_name_list[x]
    subreddit = new_subreddit
    
    subreddit_name = r.get_subreddit(subreddit, fetch=True)
    subreddit_comments = subreddit_name.get_comments(limit=comment_amount)

    sentiment_reddit(comment_amount, words_of_interest)

plotter(REDDIT_SENTIMENT_FILE, words_of_interest)
# , word1 = word1, word2 = word2, word3 =word3, word4=word4, word5 = word5, word6 = word6)


