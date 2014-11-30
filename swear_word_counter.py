import praw
import csv
import string
import re
import os

# Define the desired name and destination for your .csv file
SWEAR_WORDS = "counted_swear_words.csv"
r = praw.Reddit(user_agent='Sentiment analysis of subreddits by /u/langeniels')
inCsvBool = True

output_file = csv.writer(open("comments.csv", "ab", 0), dialect='excel')
output_file.writerow(["comment"])


# The function defines the words you want to search for,
# the subreddit and the amount of comments.
def swear_word_count(word1, word2, word3, word4, word5, word6,
                     subreddit='all', comment_amount=10000):

    chosen_subreddit = r.get_subreddit(subreddit)
    amount = chosen_subreddit.get_comments(limit=comment_amount)

    # Appends the subreddit comments 'myList'
    myList = []
    for comment in amount:
        myList.append(comment.body)
        output_file.writerow([comment.body.encode('utf-8')])

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
            w = csv.DictWriter(out_file, fieldnames=prof_wordcount.keys())
            out_file.write('Subreddit' + ',')
            w.writeheader()

    # Outputs a .csv file with the profanity words as headers
    with open(SWEAR_WORDS, 'ab') as sw, open(SWEAR_WORDS, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        w = csv.DictWriter(sw, fieldnames=prof_wordcount.keys())
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
                 subreddit='Buddhism', comment_amount=5000)
