import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


df = pd.read_csv('counted_swear_words.csv')

df.plot(kind='barh', alpha=0.5, stacked=True)
plt.show()

print df
