import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv


def daily_traffic_Lu_De(text, route):
    path = "data/Hour_Twoway_Car_" + text + "_"+route+".csv"
    h_data = pd.read_csv(path)
    g = sns.FacetGrid(h_data, col="Month", palette="viridis", col_wrap=4, hue="Date")
    g = g.map(sns.lineplot, 'Hour', 'Car', alpha=1).set_titles("{col_name}")
    g = g.set_titles("{col_name}")
    g = g.add_legend(title=False)
    g = g.set_axis_labels(y_var="Number of Cars", x_var="Time")
    plt.subplots_adjust(top=0.92)
    g = g.fig.suptitle("result/Daily Traffic Volume Analysis between Germany and Luxembourg in " + text)
    plt.savefig("result/Daily Traffic Volume Analysis between Germany and Luxembourg in "+text+".png")
    plt.show()


daily_traffic_Lu_De("2018", "A1")
