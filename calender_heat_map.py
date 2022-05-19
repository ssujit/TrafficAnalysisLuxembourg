import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calplot

# data1 = pd.read_csv('C:/Users/jyoti/Downloads/donneestrafic-2018.csv')
data1 = pd.read_csv('data/twoway_cars_traffic_2018_complete.csv')
data1['DATECOM'] = pd.to_datetime(data1['DATECOM'])
# data1 = data1[data1.DIRECTION == 3]
# data1 = data1[data1.VEHICULE == 'C']

# data2 = pd.read_csv('C:/Users/jyoti/Downloads/donneestrafic-2020.csv')
data2 = pd.read_csv('data/twoway_cars_traffic_2020_complete.csv')
data2['DATECOM'] = pd.to_datetime(data2['DATECOM'])
# data2 = data2[data2.DIRECTION == 3]
# data2 = data2[data2.VEHICULE == 'C']

data = pd.concat([data1, data2])
# data = data[(data.ROUTE == 'A1') | (data.ROUTE == 'A3') | (data.ROUTE == 'A7')]
mor_hrs = ['P07_08', 'P08_09', 'P09_10']
evn_hrs = ['P16_17', 'P17_18', 'P18_19']
data['MORNING_HOURS'] = data[mor_hrs].sum(axis=1)
data['EVENING_HOURS'] = data[evn_hrs].sum(axis=1)
data.set_index('DATECOM', inplace=True)

pil = calplot.calplot(data=data['SUM_TRAF'], cmap='GnBu', dropzero=True, figsize=(16, 6), suptitle="Total cars in everyday")
plt.savefig('result/heat_map_whole_day_aggregated.jpg')

pil = calplot.calplot(data=data['MORNING_HOURS'], cmap='GnBu', dropzero=True, figsize=(16, 6), suptitle="Total cars in everyday")
plt.savefig('result/heat_map_morning_aggregated.jpg')

pil = calplot.calplot(data=data['EVENING_HOURS'], cmap='GnBu', dropzero=True, figsize=(16, 6), suptitle="Total cars in everyday")
plt.savefig('result/heat_map_evening_aggregated.jpg')

