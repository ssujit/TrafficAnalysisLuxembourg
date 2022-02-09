#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Data analysis and visualization of traffic volume in Luxembourg
# This script is written to analyze and generate final  graph for dataset in 2018
# Declaring methods for different plots
def line_chart(T, title, limit=40000, step=5000, route="A"):
    if T == "M":
        T = 'MORNING_HOURS'
    elif T == "E":
        T = 'EVENING_HOURS'
    if route == "A":
        Saturday = test[T][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday = test[T][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d = test[T][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][
            test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort=False).sum()

    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    Weekdays = []
    for number in w_d:
        Weekdays.append(number / 5)
    plt.figure(dpi=150)
    plt.plot(Month, Saturday, marker='o', linewidth=2, label="Saturday")
    plt.plot(Month, Sunday, marker='o', linewidth=2, label="Sunday")
    plt.plot(Month, Weekdays, marker='o', linewidth=2, label="Weekdays")
    plt.xticks(Month, rotation=90)
    plt.yticks(np.arange(0, limit, step=step))
    plt.xlabel("Timestamp")
    plt.ylabel('Total Number of Cars')
    plt.title(title)
    plt.legend()
    plt.savefig("result/line_chart_traffic_analysis_"+T+"_"+route+"_2018.jpg")
    plt.show()


def bar_chart(T, title, route="A"):
    if T == "M":
        T = 'MORNING_HOURS'
    elif T == "E":
        T = 'EVENING_HOURS'
    if route == "A":
        Saturday = test[T][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday = test[T][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d = test[T][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][
            test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort=False).sum()

    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November",
             "December"]
    Weekdays = []
    for number in w_d:
        Weekdays.append(number / 5)
    N = 12
    ind = np.arange(N)
    width = 0.25
    plt.figure(dpi=150)
    bar1 = plt.bar(ind, Saturday, width, color='g')
    bar2 = plt.bar(ind + width, Sunday, width, color='r')
    bar3 = plt.bar(ind + width * 2, Weekdays, width, color='b')
    plt.xlabel("Timestamp")
    plt.ylabel('Total Number of Cars')
    plt.title("Traffic Analysis: Morning Hours")
    plt.xticks(ind + width, Month, rotation=90)
    plt.legend((bar1, bar2, bar3), ('Saturday', 'Sunday', 'Weekdays'))
    plt.show()
    plt.savefig("result/bar_chart_traffic_analysis_"+T+"_"+route+"_2018.jpg", dpi=600)


def stack_area_chart(T, title, limit=40000, step=5000, route="A"):
    if T == "M":
        T = 'MORNING_HOURS'
    elif T == "E":
        T = 'EVENING_HOURS'
    if route == "A":
        Saturday = test[T][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday = test[T][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d = test[T][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][
            test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort=False).sum()

    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    Weekdays = []
    for number in w_d:
        Weekdays.append(number / 5)

    palette = sns.color_palette("rocket_r", 9).as_hex()
    colors = ','.join(palette)
    labels = ("Saturday", "Sunday", "Weekdays")
    plt.figure(dpi=150)
    plt.stackplot(Month, Saturday, Sunday, Weekdays, colors=colors, labels=labels)
    # plt.legend(loc='upper center', bbox_to_anchor=(1.1, 0.8), shadow=True, ncol=1)
    plt.xticks(Month, rotation=30)
    plt.yticks(np.arange(0, limit, step=step))
    plt.xlabel("Time")
    plt.ylabel('Total Number of Cars')
    plt.legend()
    plt.title(title)
    plt.savefig("result/stacked_chart_traffic_analysis_"+T+"_"+route+"_2018.jpg")
    plt.show()


# Read and prepare dataframe
test = pd.read_csv('data/twoway_cars_traffic_2018_complete.csv')
mor_hrs = ['P07_08', 'P08_09', 'P09_10']
evn_hrs = ['P16_17', 'P17_18', 'P18_19']
test['MORNING_HOURS'] = test[mor_hrs].sum(axis=1)
test['EVENING_HOURS'] = test[evn_hrs].sum(axis=1)
test.to_csv('data/twoway_cars_traffic_2018_complete_with_mor_evn.csv')
test['DATECOM'] = pd.to_datetime(test['DATECOM'])


# To analyze and generate plot we need to pass certain arguments
#     1. T:(timeframe)
#         M = Morning Hours
#         E - evening Hours
#     2. title: title of graph and filename to save the image
#     3. route:
#         A = for national  scale or leave empty
#         A1 = for traffic between Germany
#         A3 = for traffic between France
#         A7 = for traffic between Belgium
#     4. limit: set the y axis upper scale for graph (default is 50000)
#     5. step: set the step size


# line_chart(T="M", title=title, route="A1", limit=5000, step=500)
# line_chart(T="M", title=title)
stack_area_chart(T="M", title="Luxembourg Traffic Volume in Morning Rush Hours 2018", limit=55000, step=5000)
stack_area_chart(T="E", title="Luxembourg Traffic Volume in Evening Rush Hours 2018", limit=50000, step=5000)
stack_area_chart(T="M", title="Luxembourg Traffic Volume in Morning Rush Hours between Germany 2018", route="A1", limit=8000, step=1000)
stack_area_chart(T="E", title="Luxembourg Traffic Volume in Evening Rush Hours between Germany 2018", route="A1", limit=6000, step=1000)
# bar_chart(Saturday, Sunday, Weekdays, title)
