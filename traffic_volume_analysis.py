#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Data analysis and visualization of traffic volume in Luxembourg
# This script is written to analyze and generate final  graph for dataset in 2018
# Declaring methods for different plots
# def line_chart(T, title, limit=40000, step=5000, route="A"):
#     if T == "M":
#         T = 'MORNING_HOURS'
#     elif T == "E":
#         T = 'EVENING_HOURS'
#     if route == "A":
#         Saturday = test[T][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(),
#                                                                              sort=False).sum().tolist()
#         Sunday = test[T][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(),
#                                                                          sort=False).sum().tolist()
#         w_d = test[T][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(
#             test.DATECOM.dt.month_name(), sort=False).sum()
#     else:
#         Saturday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(
#             test.DATECOM.dt.month_name(), sort=False).sum().tolist()
#         Sunday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(
#             test.DATECOM.dt.month_name(), sort=False).sum().tolist()
#
#         w_d = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][
#             test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort=False).sum()
#
#     Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
#              "November", "December"]
#     Weekdays = []
#     for number in w_d:
#         Weekdays.append(number / 5)
#     plt.figure(dpi=150)
#     plt.plot(Month, Saturday, marker='o', linewidth=2, label="Saturday")
#     plt.plot(Month, Sunday, marker='o', linewidth=2, label="Sunday")
#     plt.plot(Month, Weekdays, marker='o', linewidth=2, label="Weekdays")
#     plt.xticks(Month, rotation=90)
#     plt.yticks(np.arange(0, limit, step=step))
#     plt.xlabel("Timestamp")
#     plt.ylabel('Total Number of Cars')
#     plt.title(title)
#     plt.legend()
#     plt.savefig("result/line_chart_traffic_analysis_"+T+"_"+route+"_2018.jpg")
#     plt.show()
#
#
# def bar_chart(T, title, route="A"):
#     if T == "M":
#         T = 'MORNING_HOURS'
#     elif T == "E":
#         T = 'EVENING_HOURS'
#     if route == "A":
#         Saturday = test[T][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(),
#                                                                              sort=False).sum().tolist()
#         Sunday = test[T][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(),
#                                                                          sort=False).sum().tolist()
#         w_d = test[T][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(
#             test.DATECOM.dt.month_name(), sort=False).sum()
#     else:
#         Saturday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(
#             test.DATECOM.dt.month_name(), sort=False).sum().tolist()
#         Sunday = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(
#             test.DATECOM.dt.month_name(), sort=False).sum().tolist()
#
#         w_d = test['EVENING_HOURS'][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][
#             test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort=False).sum()
#
#     Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
#              "November",
#              "December"]
#     Weekdays = []
#     for number in w_d:
#         Weekdays.append(number / 5)
#     N = 12
#     ind = np.arange(N)
#     width = 0.25
#     plt.figure(dpi=150)
#     bar1 = plt.bar(ind, Saturday, width, color='g')
#     bar2 = plt.bar(ind + width, Sunday, width, color='r')
#     bar3 = plt.bar(ind + width * 2, Weekdays, width, color='b')
#     plt.xlabel("Timestamp")
#     plt.ylabel('Total Number of Cars')
#     plt.title("Traffic Analysis: Morning Hours")
#     plt.xticks(ind + width, Month, rotation=90)
#     plt.legend((bar1, bar2, bar3), ('Saturday', 'Sunday', 'Weekdays'))
#     plt.show()
#     plt.savefig("result/bar_chart_traffic_analysis_"+T+"_"+route+"_2018.jpg", dpi=600)


def stack_area_chart(title1, title2, limit=40000, step=5000, route="A"):
    T = 'MORNING_HOURS'
    if route == "A":
        Saturday18 = test18[T][test18.DATECOM.dt.day_name() == 'Saturday'].groupby(test18.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday18 = test18[T][test18.DATECOM.dt.day_name() == 'Sunday'].groupby(test18.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d18 = test18[T][test18.DATECOM.dt.day_name() != 'Saturday'][test18.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test18.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday18 = test18[T][test18.ROUTE == route][test18.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test18.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday18 = test18[T][test18.ROUTE == route][test18.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test18.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d18 = test18[T][test18.ROUTE == route][test18.DATECOM.dt.day_name() != 'Saturday'][
            test18.DATECOM.dt.day_name() != 'Sunday'].groupby(test18.DATECOM.dt.month_name(), sort=False).sum()

    if route == "A":
        Saturday20 = test20[T][test20.DATECOM.dt.day_name() == 'Saturday'].groupby(test20.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday20 = test20[T][test20.DATECOM.dt.day_name() == 'Sunday'].groupby(test20.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d20 = test20[T][test20.DATECOM.dt.day_name() != 'Saturday'][test20.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test20.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday20 = test20[T][test20.ROUTE == route][test20.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test20.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday20 = test20[T][test20.ROUTE == route][test20.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test20.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d20 = test20[T][test20.ROUTE == route][test20.DATECOM.dt.day_name() != 'Saturday'][
            test20.DATECOM.dt.day_name() != 'Sunday'].groupby(test20.DATECOM.dt.month_name(), sort=False).sum()

    T = 'EVENING_HOURS'
    if route == "A":
        Saturday18e = test18[T][test18.DATECOM.dt.day_name() == 'Saturday'].groupby(test18.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday18e = test18[T][test18.DATECOM.dt.day_name() == 'Sunday'].groupby(test18.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d18e = test18[T][test18.DATECOM.dt.day_name() != 'Saturday'][test18.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test18.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday18e = test18[T][test18.ROUTE == route][test18.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test18.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday18e = test18[T][test18.ROUTE == route][test18.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test18.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d18e = test18[T][test18.ROUTE == route][test18.DATECOM.dt.day_name() != 'Saturday'][
            test18.DATECOM.dt.day_name() != 'Sunday'].groupby(test18.DATECOM.dt.month_name(), sort=False).sum()

    if route == "A":
        Saturday20e = test20[T][test20.DATECOM.dt.day_name() == 'Saturday'].groupby(test20.DATECOM.dt.month_name(),
                                                                             sort=False).sum().tolist()
        Sunday20e = test20[T][test20.DATECOM.dt.day_name() == 'Sunday'].groupby(test20.DATECOM.dt.month_name(),
                                                                         sort=False).sum().tolist()
        w_d20e = test20[T][test20.DATECOM.dt.day_name() != 'Saturday'][test20.DATECOM.dt.day_name() != 'Sunday'].groupby(
            test20.DATECOM.dt.month_name(), sort=False).sum()
    else:
        Saturday20e = test20[T][test20.ROUTE == route][test20.DATECOM.dt.day_name() == 'Saturday'].groupby(
            test20.DATECOM.dt.month_name(), sort=False).sum().tolist()
        Sunday20e = test20[T][test20.ROUTE == route][test20.DATECOM.dt.day_name() == 'Sunday'].groupby(
            test20.DATECOM.dt.month_name(), sort=False).sum().tolist()

        w_d20e = test20[T][test20.ROUTE == route][test20.DATECOM.dt.day_name() != 'Saturday'][
            test20.DATECOM.dt.day_name() != 'Sunday'].groupby(test20.DATECOM.dt.month_name(), sort=False).sum()

    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    Weekdays18 = []
    for number in w_d18:
        Weekdays18.append(number / 5)

    Weekdays20 = []
    for number in w_d20:
        Weekdays20.append(number / 5)

    Weekdays18e = []
    for number in w_d18e:
        Weekdays18e.append(number / 5)

    Weekdays20e = []
    for number in w_d20e:
        Weekdays20e.append(number / 5)

    palette = sns.color_palette("rocket_r", 9).as_hex()
    colors = ','.join(palette)
    labels = ("Saturday", "Sunday", "Weekdays")
    plt.rcParams.update({'figure.figsize':(10,6), 'figure.dpi':120})

    fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')
    fig.text(0.437,0.91,"Morning Rush Hours", size=10, backgroundcolor='yellow')
    fig.text(0.437,0.485,"Evening Rush Hours", size=10, backgroundcolor='yellow')
    # fig.suptitle("Luxembourg Daily Traffic Volume Analysis")
    ax[0][0].stackplot(Month, Saturday18, Sunday18, Weekdays18, colors=colors, labels=labels)
    ax[0][0].set_title("2018\n",)
    ax[0][1].stackplot(Month, Saturday20, Sunday20, Weekdays20, colors=colors, labels=labels)
    ax[0][1].set_title("2020\n")
    ax[1][0].stackplot(Month, Saturday18e, Sunday18e, Weekdays18e, colors=colors, labels=labels)
    ax[1][0].set_title("\n")
    plt.sca(ax[1, 0])
    plt.xticks(Month, rotation=45, fontsize=6)
    ax[1][1].stackplot(Month, Saturday20e, Sunday20e, Weekdays20e, colors=colors, labels=labels)
    ax[1][1].set_title("\n")
    plt.sca(ax[1, 1])
    plt.xticks(Month, rotation=45,fontsize=6)
    plt.legend(bbox_to_anchor=(0.98, 0.97), ncol=3, frameon=False, fontsize=8)
    plt.sca(ax[1, 0])
    plt.yticks(np.arange(0, limit, step=step), fontsize=6)
    plt.sca(ax[0, 0])
    plt.yticks(np.arange(0, limit, step=step), fontsize=6)

    plt.savefig("result/stacked_chart_traffic_volume_analysis_"+route+".jpg")
    plt.show()


# Read and prepare dataframe 2018
test18 = pd.read_csv('data/twoway_cars_traffic_2018_complete.csv')
mor_hrs18 = ['P07_08', 'P08_09', 'P09_10']
evn_hrs18 = ['P16_17', 'P17_18', 'P18_19']
test18['MORNING_HOURS'] = test18[mor_hrs18].sum(axis=1)
test18['EVENING_HOURS'] = test18[evn_hrs18].sum(axis=1)
test18.to_csv('data/twoway_cars_traffic_2018_complete_with_mor_evn.csv')
test18['DATECOM'] = pd.to_datetime(test18['DATECOM'])

# Read and prepare dataframe 2020
test20 = pd.read_csv('data/twoway_cars_traffic_2020_complete.csv')
mor_hrs20 = ['P07_08', 'P08_09', 'P09_10']
evn_hrs20 = ['P16_17', 'P17_18', 'P18_19']
test20['MORNING_HOURS'] = test20[mor_hrs20].sum(axis=1)
test20['EVENING_HOURS'] = test20[evn_hrs20].sum(axis=1)
test20.to_csv('data/twoway_cars_traffic_2020_complete_with_mor_evn.csv')
test20['DATECOM'] = pd.to_datetime(test20['DATECOM'])


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

stack_area_chart(title1="Luxembourg vs Germany 2018", title2="Luxembourg vs Germany 2020", route="A1", limit=11000, step=1000)

stack_area_chart(title1="Luxembourg vs Germany 2018", title2="Luxembourg vs Germany 2020", route="A3", limit=15000, step=1500)

stack_area_chart(title1="Luxembourg vs Germany 2018", title2="Luxembourg vs Germany 2020", route="A7", limit=5000, step=500)

stack_area_chart(title1="Luxembourg vs Germany 2018", title2="Luxembourg vs Germany 2020", route="A", limit=55000, step=5000)
