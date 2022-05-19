import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def cal_per(value1, value2):
    percentage1 = []
    percentage2 = []
    total = 0
    lim = len(value1)
    # print("Parcentage: ", lim)
    for i in range(lim):
        total = value1[i] + value2[i]
        pct1 = (value1[i] / total) * 100
        percentage1.append(round(pct1, 2))
        pct2 = (value2[i] / total) * 100
        percentage2.append(round(pct2, 2))
    return percentage1,percentage2

def difference(sat1, sat2, sun1, sun2, wday1, wday2):
    diff_std = []
    diff_sd = []
    diff_wd = []
    limit = len(sat1)
    # print("Differe: ",limit)
    for i in range(limit):
        d = sat2[i] - sat1[i]
        diff_std.append(d)

    for i in range(limit):
        e = sun2[i] - sun1[i]
        diff_sd.append(e)

    for i in range(limit):
        f = wday2[i] - wday1[i]
        diff_wd.append(f)

    return diff_wd, diff_sd, diff_wd

def data_collection(time, route, test):
    test['DATECOM'] = pd.to_datetime(test['DATECOM'])
    Saturday1 = test[time][test.DIRECTION==1][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(), sort = False).sum().tolist()
    Sunday1 = test[time][test.DIRECTION==1][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort = False).sum().tolist()

    w_day1 = test[time][test.DIRECTION==1][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort = False).sum()

    Saturday2 = test[time][test.DIRECTION==2][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Saturday'].groupby(test.DATECOM.dt.month_name(), sort = False).sum().tolist()
    Sunday2 = test[time][test.DIRECTION==2][test.ROUTE == route][test.DATECOM.dt.day_name() == 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort = False).sum().tolist()

    w_day2 = test[time][test.DIRECTION==2][test.ROUTE == route][test.DATECOM.dt.day_name() != 'Saturday'][test.DATECOM.dt.day_name() != 'Sunday'].groupby(test.DATECOM.dt.month_name(), sort = False).sum()

    # Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    w_d1 = []
    w_d2 = []
    # w_d1 = [2630, 3546, 5648, 5648, 2630, 3546, 5648, 5648, 2630, 3546, 5648, 5648]
    # w_d2 = [1630, 2546, 3648, 4688, 2630, 3546, 5648, 7648, 1630, 3546, 6648, 7648]
    for number in w_day1:
        w_d1.append(number/5)
    for number in w_day2:
        w_d2.append(number/5)

    # print("Saturday: ", len(Saturday2))
    week_d1,week_d2 = cal_per(w_d1,w_d2)
    Satur1,Satur2 = cal_per(Saturday1,Saturday2)
    Sun1,Sun2 = cal_per(Sunday1,Sunday2)

    diff_std, diff_sd, diff_wd = difference(Satur1, Satur2, Sun1, Sun2, week_d1, week_d2)

    return diff_std, diff_sd, diff_wd

def draw_plot_2(std18, sd18, wd18, std20, sd20, wd20, title, marking):
    labels = ("Saturday", "Sunday", "Weekdays")
    plt.rcParams.update({'figure.figsize':(10,4.5), 'figure.dpi':120})
    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
    fig.suptitle(title,  x=0.215, y=0.95, weight='bold', fontsize=11)
    fig.text(0.915,0.66,"2018", size=11, backgroundcolor='yellow', weight='bold', rotation=90)
    fig.text(0.915,0.26,"2020", size=11, backgroundcolor='yellow', weight='bold', rotation=90)

    ax[0][0].bar(Month, std18, color='blue', hatch="////")
    ax[0][1].bar(Month, sd18, color='red', hatch="////")
    ax[0][2].bar(Month, wd18, color='green', hatch="////")
    ax[1][0].bar(Month, std20, color='blue', hatch="////")
    ax[1][1].bar(Month, sd20, color='red', hatch="////")
    ax[1][2].bar(Month, wd20, color='green', hatch="////")

    plt.sca(ax[0, 0])
    plt.yticks(np.arange(-20, 80, step=20), fontsize=6)
    plt.sca(ax[1, 0])
    plt.yticks(np.arange(-20, 80, step=20), fontsize=6)

    plt.sca(ax[1, 0])
    plt.xticks(Month, rotation=45, fontsize=6)
    plt.sca(ax[1, 1])
    plt.xticks(Month, rotation=45, fontsize=6)
    plt.sca(ax[1, 2])
    plt.xticks(Month, rotation=45, fontsize=6)

    fig.legend(labels, ncol=3, bbox_to_anchor=[0.912, 0.96], frameon=False)
    plt.show()
    plt.savefig("loss_and_gain_graph_"+marking+".jpg")


def draw_plot(std18m, sd18m, wd18m, std18e, sd18e, wd18e, std20m, sd20m, wd20m, std20e, sd20e, wd20e):
    palette = sns.color_palette("rocket_r", 9).as_hex()
    colors = ','.join(palette)
    labels = ("Saturday", "Sunday", "Weekdays")
    plt.rcParams.update({'figure.figsize':(10,6), 'figure.dpi':120})
    Month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    fig, ax = plt.subplots(4, 3, sharex='col', sharey='row')
    fig.text(0.915,0.76,"Morning", size=10, backgroundcolor='yellow', rotation=90)
    fig.text(0.915,0.56,"Evening", size=10, backgroundcolor='yellow', rotation=90)
    fig.text(0.915,0.36,"Morning", size=10, backgroundcolor='yellow', rotation=90)
    fig.text(0.915,0.16,"Evening", size=10, backgroundcolor='yellow', rotation=90)
    # fig.text(0.437,0.485,"Evening Rush Hours", size=10, backgroundcolor='yellow')
    labels = ("Saturday", "Sunday", "Weekdays")
    ax[0][0].bar(Month, std18m, color='blue')
    ax[0][1].bar(Month, sd18m, color='red')
    ax[0][2].bar(Month, wd18m, color='green')
    ax[1][0].bar(Month, std18e, color='blue')
    ax[1][1].bar(Month, sd18e, color='red')
    ax[1][2].bar(Month, wd18e, color='green')
    ax[2][0].bar(Month, std20m, color='blue', hatch="////")
    ax[2][1].bar(Month, sd20m, color='red', hatch="////")
    ax[2][2].bar(Month, wd20m, color='green', hatch="////")
    ax[3][0].bar(Month, std20e, color='blue', hatch="////")
    plt.sca(ax[3, 0])
    plt.xticks(Month, rotation=45, fontsize=6)
    ax[3][1].bar(Month, sd20e, color='red', hatch="////")
    plt.sca(ax[3, 1])
    plt.xticks(Month, rotation=45, fontsize=6)
    ax[3][2].bar(Month, wd20e, color='green', hatch="////")
    plt.sca(ax[3, 2])
    plt.xticks(Month, rotation=45, fontsize=6)
    plt.sca(ax[0, 0])
    plt.yticks(np.arange(-20, 80, step=20), fontsize=6)
    plt.sca(ax[1, 0])
    plt.yticks(np.arange(-20, 80, step=20), fontsize=6)
    plt.sca(ax[2, 0])
    plt.yticks(np.arange(-20, 80, step=20), fontsize=6)
    plt.sca(ax[3, 0])
    plt.yticks(np.arange(-20, 80, step=20), fontsize=6)

    fig.legend(labels, ncol=3, bbox_to_anchor=[0.912, 0.94], frameon=False)
    # ax[0][1].set_title("2018\nMorning Rush Hours")
    # ax[1][1].set_title("2018\nEvening Rush Hours")
    # ax[2][1].set_title("2020\nMorning Rush Hours")
    # ax[3][1].set_title("2020\nEvening Rush Hours")

    plt.show()


data1 = pd.read_csv('data/both_direction_2020_with_mor_evn.csv')
data2 = pd.read_csv('data/both_direction_2018_with_mor_evn.csv')
M = 'MORNING_HOURS'
E = 'EVENING_HOURS'
Route = 'A1'

std18m, sd18m, wd18m = data_collection(M, Route, data1)
std18e, sd18e, wd18e = data_collection(E, Route, data1)
std20m, sd20m, wd20m = data_collection(M, Route, data2)
std20e, sd20e, wd20e = data_collection(E, Route, data2)


# draw_plot(std18m, sd18m, wd18m, std18e, sd18e, wd18e, std20m, sd20m, wd20m, std20e, sd20e, wd20e)

draw_plot_2(std18m, sd18m, wd18m, std20m, sd20m, wd20m, title="Morning rush hours: ", marking='morning')
draw_plot_2(std18e, sd18e, wd18e, std20e, sd20e, wd20e, title="Evening rush hours: ", marking='evening')
