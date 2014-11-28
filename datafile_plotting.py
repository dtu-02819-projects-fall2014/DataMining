import pandas as pd
import matplotlib.pyplot as plt


def plotter(plot_kind, file):
    df = pd.read_csv(file)

    df.plot(kind=plot_kind, alpha=0.5, stacked=True)
    plt.show()

    print df

# Example usage:
# plotter('barh', 'counted_swear_words.csv')
