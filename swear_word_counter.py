import praw
import csv
import string
import re
import os

# Define the desired name and destination for your .csv file
SWEAR_WORDS = "counted_swear_words.csv"

# Make sure the "swear words" file exists. If not, we will make it here.
if not os.path.isfile(SWEAR_WORDS):
    with open(SWEAR_WORDS, "w") as out_file:
        out_file.write("")

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')


# The function defines the words you want to search for,
# the subreddit and the amount of comments.
def swear_word_count(word1, word2, word3, word4, word5, word6,
                     subreddit='all', comment_amount=200):

    chosen_subreddit = r.get_subreddit(subreddit)
    amount = chosen_subreddit.get_comments(limit=comment_amount)

    # Appends the subreddit comments 'myList'
    myList = []
    for comment in amount:
        myList.append(comment.body)

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

    # Outputs a .csv file with the profanity words as headers
    with open(SWEAR_WORDS, 'wb') as sw:
        w = csv.DictWriter(sw, prof_wordcount.keys())
        w.writeheader()
        w.writerow(prof_wordcount)
    print "Outputted " + "'" + SWEAR_WORDS + "'" + " to the folder."

# Example usage:
# swear_word_count('fuck', 'in', 'shit', 'the', 'bitch', 'gay',
#                  'cringepics', 20)
