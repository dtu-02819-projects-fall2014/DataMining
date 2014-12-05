#Subreddit Comments Analysis 

A Python program that can take comments from a chosen subreddit, analyse the subreddits sentiment value as well as count the occurences of specified swear words. The program can then automatically output a .csv file containing the counted words and display the information through bar plots.

##Usage

This program has several functions you can use to interact with reddit.com. It all depends on your focus areas.

####Search a specific subreddit for comments and specified words count the specified swear words.

		from grab_comments import sentiment_reddit

		sentiment_reddit(comment_amount = 500,
                     words_of_interest = [money, cats, dogs,
                                          love, hate, kiss])

By default, the program asks for a user input to determine the amount of comments to fetch and the words. It also uses user input to determine what subreddits it should search in.

This script will output a .csv file called ‘reddit_sentiment.csv’ containing all the specified words and the amount of occurences as well as the sentiment values and percentage of swearing. This file can then be used to graph bar plots with the datafile_plotting.py file.

####Analyse the comments.

		from analysis import reddit_anal

		reddit_anal(subreddit_com = 'comments.csv',
                'money', 'cats', 'dogs', 'love', 'hate', 'kiss')

the analysis.py file will input the subreddit comments (working together with grab_comments.py) and analyse the comments. The output will then be the average subreddits sentiment values, the percentage of swearing and the occurrences of the specified words.

####Graph the outputted .csv file.

		from datafile_plotting import plotter

		plotter(plot_file = 'reddit_sentiment.csv', chosen_words =
            [money, cats, dogs, love, hate, kiss])

This function will graph the outputted reddit_sentiment.csv file with four bar plots.
