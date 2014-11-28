#Reddit Comments and Replies Analyzer 

A Python program that can take comments and replies from a chosen subreddit and count the occurences of specified swear words. The program can then automatically output a .csv file containing the counted words and display the information through a specified diagram/chart/plot.
Also has the ability to do sentiment analysis on the subreddits to determine the overall atmosphere.

##Usage

This program has several functions you can use to interact with Reddit.org. It all depends on your focus areas.

####Search a specific subreddit for comments and count the specified swear words.

		from swear_word_counter import swear_word_count

		swear_word_count(‘word1’, ‘word2’, ‘word3’, ‘word4’, ‘word5’, ‘word6’)

By default, the program takes the 200 recent comments from the subreddit ‘all’. You can change the subreddit by using the ‘subreddit’ parameter and you can change the amount of comments the program will fetch with the ‘comment_amount’ parameter.

		swear_word_count(‘word1’, ‘word2’, ‘word3’, ‘word4’, ‘word5’, ‘word6’,
						 subreddit=‘funny’, comment_amount=100)

This script will output a .csv file called ‘counted_swear_words.csv’ containing all the specified words and the amount of occurences. This file can then be used to graph your preferred plot with the datafile_plotting.py file.

####Graph the outputted .csv file

		from datafile_plotting import plotter

		plotter('barh', 'counted_swear_words.csv')

This function will graph the outputted .csv file with different types of plot, using pandas plot keywords.
