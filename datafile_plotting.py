import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


df = pd.read_csv('counted_swear_words.csv')

df.plot(kind='hist', alpha=0.5)
plt.show()

print df