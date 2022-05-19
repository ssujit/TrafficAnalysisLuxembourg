# load packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('data/both_direction_2020_with_mor_evn.csv')
data2 = pd.read_csv('data/both_direction_2018_with_mor_evn.csv')
print(data1.groupby(data2.POSTE_ID).count())
