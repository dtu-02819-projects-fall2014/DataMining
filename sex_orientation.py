import praw
import csv
from collections import Counter
import string
import re
import os

# Define the desired name and destination for your .csv file
# that will contain the counted swear words
SWEAR_WORDS = "counted_swear_words.csv"

# Define the words you want to search for in a specific subreddit
specificSwearWords = ["the", "in", "fuck", "homo", "homosexual", "queer"]

# Make sure the "swear words" file exists. If not, we will make it here.
if not os.path.isfile(SWEAR_WORDS):
    with open(SWEAR_WORDS, "w") as out_file:
        out_file.write("")

r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')

subreddit = r.get_subreddit('cringepics')
subreddit_comments = subreddit.get_comments(limit=2000)

# Will append the subreddit comments 'myList'
myList = []
for comment in subreddit_comments:
    myList.append(comment.body)

# Converting our comments list to a string so we can count occurences.
# The string is then converted to lowercase
# so we don't have to search for a word twice. ex. "fuck" and "Fuck"
# The regex is replacing all punctuations in the comments string with spaces.
# We can then count swear words that ends or starts with a punctuation.

stringMyList = ''.join(myList).encode('utf-8').lower()
regex = re.compile('[%s]' % re.escape(string.punctuation))
finalList = regex.sub(' ', stringMyList)
del myList, stringMyList

prof_wordcount = dict((x, 0) for x in specificSwearWords)
for w in re.findall(r"\w+", finalList):
    if w in prof_wordcount:
        prof_wordcount[w] += 1
print "WORDCOUNT: " + str(prof_wordcount)

# Writes a .csv file with the profanity keys in the start of the rows
# and the profanity occurences to the right
writer = csv.writer(open('dict.csv', 'wb'))
for key, value in prof_wordcount.items():
    writer.writerow([key, value])

# Writes a .csv file with the profanity keys as headers
# and the amount of occurences beneath
with open(SWEAR_WORDS, 'wb') as sw:
    w = csv.DictWriter(sw, prof_wordcount.keys())
    w.writeheader()
    w.writerow(prof_wordcount)


def count_many(needles, haystack):
    count = Counter(haystack.split())
    print {key: count[key] for key in count if key in needles}

count_many(specificSwearWords, finalList)
