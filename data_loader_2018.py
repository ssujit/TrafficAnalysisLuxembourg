import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import csv


data = pd.read_csv('C:/Users/jyoti/Downloads/donneestrafic-2018.csv')
d_3 =  data[data.DIRECTION == 3]
vt_c = d_3[d_3.VEHICULE == 'C']
# print(y.VEHICULE.count())
vt_c['DATECOM'] = pd.to_datetime(vt_c['DATECOM'])


# In[225]:


# Morning Working Pick Hour Calculation

header = ['Month', 'Date', 'Cars']
with open('twoway_car_traffic_2018.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

def write_csv(x, y, z):
    data = [x, y, z]
    with open('twoway_car_traffic_2018.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# Traffic Analysis for January
# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-01-20']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in January:", total_st_fw_jan)

write_csv('January','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-01-21']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in January:",total_s_fw_jan)

write_csv('January','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-01-15']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in January:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-01-16']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in January:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-01-17']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in January:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-01-18']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in January:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-01-19']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in January:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('January','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', index=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[227]:


# Traffic Analysis for February

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-02-03']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in February:", total_st_fw_jan)

write_csv('February','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-02-04']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in February:",total_s_fw_jan)

write_csv('February','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-02-05']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in February:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-02-06']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in February:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-02-07']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in February:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-02-08']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in February:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-02-09']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in February:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('February','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[228]:


# Traffic Analysis for March

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-03-03']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in March:", total_st_fw_jan)

write_csv('March','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-03-04']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in March:",total_s_fw_jan)

write_csv('March','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-03-05']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in March:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-03-06']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in March:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-03-07']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in March:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-03-08']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in March:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-03-09']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in March:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('March','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[229]:


# Traffic Analysis for April

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-04-07']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in April:", total_st_fw_jan)

write_csv('April','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-04-08']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in April:",total_s_fw_jan)

write_csv('April','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-04-09']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in April:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-04-10']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in April:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-04-11']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in April:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-04-12']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in April:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-04-13']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in April:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('April','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[230]:


# Traffic Analysis for May

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-05-05']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in May:", total_st_fw_jan)

write_csv('May','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-05-06']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in May:",total_s_fw_jan)

write_csv('May','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-05-07']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in May:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-05-08']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in May:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-05-09']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in May:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-05-10']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in May:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-05-11']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in May:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('May','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[231]:


# Traffic Analysis for June

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-06-02']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in June:", total_st_fw_jan)

write_csv('June','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-06-03']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in June:",total_s_fw_jan)

write_csv('June','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-06-04']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in June:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-06-05']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in June:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-06-06']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in June:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-06-07']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in June:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-06-08']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in June:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('June','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[232]:


# Traffic Analysis for July

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-07-07']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in July:", total_st_fw_jan)

write_csv('July','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-07-08']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in July:",total_s_fw_jan)

write_csv('July','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-07-09']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in July:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-07-10']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in July:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-07-11']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in July:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-07-12']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in July:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-07-13']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in July:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('July','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[233]:


# Traffic Analysis for August

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-08-04']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in August:", total_st_fw_jan)

write_csv('August','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-08-05']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in August:",total_s_fw_jan)

write_csv('August','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-08-06']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in August:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-08-07']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in August:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-08-08']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in August:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-08-09']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in August:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-08-10']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in August:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('August','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[234]:


# Traffic Analysis for September

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-09-08']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in September:", total_st_fw_jan)

write_csv('September','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-09-09']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in September:",total_s_fw_jan)

write_csv('September','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-09-10']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in September:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-09-11']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in September:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-09-12']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in September:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-09-13']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in September:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-09-14']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in September:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('September','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[235]:


# Traffic Analysis for October

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-10-20']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in October:", total_st_fw_jan)

write_csv('October','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-10-21']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in October:",total_s_fw_jan)

write_csv('October','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-10-22']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in October:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-10-23']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in October:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-10-24']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in October:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-10-25']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in October:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-10-26']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in October:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('October','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[236]:


# Traffic Analysis for November

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-11-10']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in November:", total_st_fw_jan)

write_csv('November','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-11-04']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in November:",total_s_fw_jan)

write_csv('November','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-11-05']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in November:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-11-06']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in November:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-11-07']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in November:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-11-08']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in November:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-11-09']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in November:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('November','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)


# In[237]:


# Traffic Analysis for December

# Saturday

st_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Saturday']

# total_st_all = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
# total_st_fw = st_d.P06_07.sum() + st_d.P07_08.sum() + st_d.P08_09.sum()
temp = st_d[st_d.DATECOM == '2018-12-08']
total_st_fw_jan = temp.P06_07.sum() + temp.P07_08.sum() + temp.P08_09.sum()
print("Total Cars on Saturday in December:", total_st_fw_jan)

write_csv('December','Saturday',total_st_fw_jan)

# Sunday

s_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Sunday']
temp1 = s_d[s_d.DATECOM == '2018-12-09']
total_s_fw_jan = temp1.P06_07.sum() + temp1.P07_08.sum() + temp1.P08_09.sum()
print("Total Cars on Sunday in December:",total_s_fw_jan)

write_csv('December','Sunday',total_s_fw_jan)

# Monday

m_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Monday']
temp3 = m_d[m_d.DATECOM == '2018-12-10']
total_m_fw_jan = temp3.P06_07.sum() + temp3.P07_08.sum() + temp3.P08_09.sum()
print("Total Cars on Monday in December:",total_m_fw_jan)

# Tuesday

tu_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Tuesday']
temp4 = tu_d[tu_d.DATECOM == '2018-12-11']
total_tu_fw_jan = temp4.P06_07.sum() + temp4.P07_08.sum() + temp4.P08_09.sum()
print("Total Cars on Monday in December:",total_tu_fw_jan)

# Wednesday

w_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Wednesday']
temp5 = w_d[w_d.DATECOM == '2018-12-12']
total_w_fw_jan = temp5.P06_07.sum() + temp5.P07_08.sum() + temp5.P08_09.sum()
print("Total Cars on Monday in December:",total_w_fw_jan)

# Thursday

th_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Thursday']
temp6 = th_d[th_d.DATECOM == '2018-12-13']
total_th_fw_jan = temp6.P06_07.sum() + temp6.P07_08.sum() + temp6.P08_09.sum()
print("Total Cars on Monday in December:",total_th_fw_jan)

# Friday

f_d = vt_c[vt_c.DATECOM.dt.day_name() == 'Friday']
temp7 = f_d[f_d.DATECOM == '2018-12-14']
total_f_fw_jan = temp7.P06_07.sum() + temp7.P07_08.sum() + temp7.P08_09.sum()
print("Total Cars on Monday in December:",total_f_fw_jan)

average_weekdays = (total_m_fw_jan + total_tu_fw_jan + total_w_fw_jan + total_th_fw_jan + total_f_fw_jan)/5
print("Total Cars on Weekday Average:", average_weekdays)

write_csv('December','Weekdays',average_weekdays)


temp.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp1.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp3.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp4.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp5.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp6.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)
temp7.to_csv('twoway_cars_traffic_2018_complete.csv', mode='a', index=False, header=False)

