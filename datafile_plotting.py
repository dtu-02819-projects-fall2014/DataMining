"""
This file is part of the Subreddit Comments Analysis bot program.

Copyright 2014 Jeppe de Lange and Niclas Bach Nielsen

It is intended to be used in conjunction with analysis.py and
grab_comments.py.
This script will take the data which is outputted from analysis.py and
grab_comments.py and plot four graphs and saving them to '/plot_output_files/'

License:

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

The Reddit Subreddit Comments Analysis is distributed in the hope
that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the Reddit Subreddit Comments Analysis library.
If not, see <http://www.gnu.org/licenses/>.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

PLOT_FOLDER = 'plot_output_files'

if not os.path.exists(PLOT_FOLDER):
    os.makedirs(PLOT_FOLDER)


def plotter(plot_file, chosen_words):
    """
    Generates four bar plots of an inputted .csv file.
    Inputs a .csv file and some specified Words generated from
    grab_comments.py

    Example usage:

    >>> plotter(plot_file = 'reddit_sentiment.csv', chosen_words =
                [money, cats, dogs, love, hate, kiss])

    The reddit_sentiment.csv file and the chosen words have to correspond.
    """
    df = pd.read_csv(plot_file, encoding="utf-8", index_col='Subreddit')
    ax = df[chosen_words].plot(kind='barh',
                               stacked=True, alpha=0.7, figsize=(12, 9))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.title('Word Frequency (1000 comments)', fontsize=18)
    plt.xlabel('Percentage', fontsize=16)
    plt.ylabel('Subreddit', fontsize=16)
    plt.savefig('plot_output_files/wordfreq_barh.png', bbox_inches="tight")
    plt.show()

    df = pd.read_csv(plot_file, encoding="utf-8", index_col='Subreddit')
    ax2 = df[chosen_words].plot(kind='bar', alpha=0.7, figsize=(12, 9))
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.get_xaxis().tick_bottom()
    ax2.get_yaxis().tick_left()
    ax2.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.title('Word Frequency (1000 comments)', fontsize=18)
    plt.xlabel('Subreddit', fontsize=16)
    plt.ylabel('Percentage', fontsize=16)
    plt.savefig('plot_output_files/wordfreq_bar.png', bbox_inches="tight")
    plt.show()

    ax3 = df['Sentiment Value'].plot(kind='bar', alpha=0.7, figsize=(12, 9))
    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)
    ax3.get_xaxis().tick_bottom()
    ax3.get_yaxis().tick_left()
    ax3.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.title('Sentiment Score (1000 comments)', fontsize=18)
    plt.xlabel('Subreddit', fontsize=16)
    plt.ylabel('Average Sentiment Value', fontsize=16)
    plt.savefig('plot_output_files/sentiment_bar.png', bbox_inches="tight")
    plt.show()

    ax4 = df['Profanity Score'].plot(kind='bar', alpha=0.7, figsize=(12, 9))
    ax4.spines["top"].set_visible(False)
    ax4.spines["right"].set_visible(False)
    ax4.get_xaxis().tick_bottom()
    ax4.get_yaxis().tick_left()
    ax4.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.xticks(rotation='0')
    plt.title('Profane Words Frequency (1000 comments)', fontsize=18)
    plt.xlabel('Subreddit', fontsize=16)
    plt.ylabel('Percentage', fontsize=16)
    plt.savefig('plot_output_files/profanity_bar.png', bbox_inches="tight")
    plt.show()
