import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
import Image
import os

PLOT_FOLDER = 'plot_output_files'

if not os.path.exists(PLOT_FOLDER):
    os.makedirs(PLOT_FOLDER)


def plotter(plot_file, chosen_words): 
    df = pd.read_csv(plot_file, encoding="utf-8",index_col='Subreddit')
    ax = df[chosen_words].plot(kind='barh',stacked=True, alpha=0.7, figsize=(12,9))
    ax.spines["top"].set_visible(False)   
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()
    ax.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.title('Word Frequency', fontsize = 18)
    plt.xlabel('Percentage', fontsize=16)
    plt.ylabel('Subreddit', fontsize=16)
    plt.savefig('plot_output_files/wordfreq_barh.png', bbox_inches="tight")
    plt.show()

    df = pd.read_csv(plot_file, encoding="utf-8",index_col='Subreddit')
    ax2 = df[chosen_words].plot(kind='bar',stacked=False, alpha=0.7, figsize=(12,9))
    ax2.spines["top"].set_visible(False)   
    ax2.spines["right"].set_visible(False)
    ax2.get_xaxis().tick_bottom()  
    ax2.get_yaxis().tick_left()
    ax2.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.title('Word Frequency', fontsize = 18)
    plt.xlabel('Subreddit', fontsize=16)
    plt.ylabel('Percentage', fontsize=16)
    plt.savefig('plot_output_files/wordfreq_bar.png', bbox_inches="tight")
    plt.show()

    ax3 = df['Sentiment Value'].plot(kind='bar', alpha=0.7, figsize=(12,9))
    ax3.spines["top"].set_visible(False)   
    ax3.spines["right"].set_visible(False)
    ax3.get_xaxis().tick_bottom()  
    ax3.get_yaxis().tick_left()
    ax3.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.title('Sentiment Score', fontsize = 18)
    plt.xlabel('Subreddit', fontsize=16)
    plt.ylabel('Average Sentiment Value', fontsize = 16)
    plt.savefig('plot_output_files/sentiment_bar.png', bbox_inches="tight")
    plt.show()

    ax4 = df['Profanity Score'].plot(kind='bar',alpha=0.7, figsize=(12,9))
    ax4.spines["top"].set_visible(False)   
    ax4.spines["right"].set_visible(False)
    ax4.get_xaxis().tick_bottom()  
    ax4.get_yaxis().tick_left()
    ax4.grid(False)
    plt.xticks(rotation='0', fontsize=14)
    plt.yticks(rotation='0', fontsize=14)
    plt.xticks(rotation='0')
    plt.title('Profane Words Frequency', fontsize = 18)
    plt.xlabel('Subreddit', fontsize=16)
    plt.ylabel('Percentage', fontsize=16)
    plt.savefig('plot_output_files/profanity_bar.png', bbox_inches="tight")
    plt.show()


# Example usage:




