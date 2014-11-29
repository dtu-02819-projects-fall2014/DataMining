import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import csv
import math


def plotter(file):
    df = pd.read_csv(file, encoding="utf-8",index_col='Subreddit')
    df.plot(kind='bar',stacked=True)#,x=df.values, y=df.columns)
    plt.xticks(rotation='0')
    plt.show()

    plt.boxplot(x=df.values)
    plt.xticks([1, 2, 3, 4, 5, 6], df.columns)
    plt.show()

    df.boxplot()
    plt.show()
    area =[]
    #area.append(math.sqrt(df.values))
    plt.scatter(x=df['fuck'],y=df['shit'])
    plt.show()


# Example usage:
plotter('counted_swear_words.csv')



