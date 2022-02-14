import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calplot
import july

def cal_heat_map(year):
    data = pd.read_csv('C:/Users/jyoti/Downloads/donneestrafic-'+str(year)+'.csv')
    data['DATECOM'] = pd.to_datetime(data['DATECOM'])
    data.set_index('DATECOM', inplace=True)
    data = data[data.DIRECTION == 3]
    data = data[data.VEHICULE == 'C']
    # data = data.ROUTE = ['A1', 'A3', 'A7']
    # print(data)
    pil = calplot.calplot(data=data['SUM_TRAF'], cmap='GnBu', dropzero=True, figsize=(16, 4), suptitle="Total cars in in everyday")
    plt.savefig('result/heat_map_'+str(year)+'.jpg')


cal_heat_map(2018)
cal_heat_map(2020)

