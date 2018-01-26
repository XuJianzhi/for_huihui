
#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd
from datetime import datetime


#path_in='C:/Users/liangzhihui/Desktop/S500.xlsx' 
path_in='/home/m/桌面/for_huihui/data/11.xlsx'
data2=pd.read_excel(path_in)

#############
'''
data2=data2.sort_values(by='created_at',ascending=True)

def fun(ser):
	ser_2=np.array(ser)
	ser_3=ser-ser+ser_2[0]-ser_2[-1]
	return ser_3

data2['delta_price_2']=data2['seller_price'].groupby(data2['customer_id']).apply(fun)


#######################

data2=data2.sort_values(by='created_at',ascending=True)

def fun(ser):
	return ser-np.array(ser)[-1]

data2['delta_price_3']=data2['seller_price'].groupby(data2['customer_id']).apply(fun)
          
          
#######################

data2=data2.sort_values(by='created_at',ascending=True)

def fun(ser):
	#print(ser)
	ser2 = np.array(ser)
	end_time = datetime.strptime(ser2[-1][:-2], '%Y-%m-%d %H:%M:%S')
	start_time = datetime.strptime(ser2[0][:-2], '%Y-%m-%d %H:%M:%S')

	delta_time = end_time - start_time
	delta_time_str = str(delta_time)
	
	return pd.Series([delta_time_str] * len(ser), index=ser.index)

data2['delta_time']=data2['_col4'].groupby(data2['customer_id']).apply(fun)
'''
########################

#去掉看了一次就买的
from collections import Counter

times = data2['customer_id'].groupby(data2['customer_id']).count()
single = np.array(times[times == 1].index)

data3 = data2.copy()
for i in data3.index :
	if data3.loc[i, 'customer_id'] in single :
		data3.drop(i, inplace = True)



########################


#新加的功能1
data3=data3.sort_values(by='created_at',ascending=True)

def fun(ser):
	if len(ser) == 1 :	##
		ser_2 = pd.Series([np.nan],index=ser.index)
		return ser_2
		
	ser_2 = pd.Series(index=ser.index)
	for i in ser.index[:-1] :
		if ser[i] == ser[i+1] :
			ser_2[i] = np.nan
		else :
			ser_2[i] = data3.loc[i, 'appoint_fail_reason']
	
	return ser_2
	
# 把等号前面换成你想要的名字		
data3['meiqiming_1']=data3['appoint_person'].groupby(data3['customer_id']).apply(fun)

path_out='/home/m/桌面/for_huihui/data/11_out.xlsx'
data3.to_excel(path_out)

########################
#新加的功能2
data3=data3.sort_values(by='created_at',ascending=True)

temp = data3['source_type'].groupby(data3['customer_id']).first()
# 把等号前面换成你想要的名字
meiqiming_2 = len(temp[temp == 11]) + len(temp[temp == 14])		# 8948

del temp
print('meiqiming_2 =', meiqiming_2)	
########################
#新加的功能3
data3=data3.sort_values(by='created_at',ascending=True)

def fun(ser):
	if len(ser) == 1 :
		temp = np.array(ser)
	else: 
		temp = np.array(ser)[:-1]
	temp_2 = len(temp[temp == 11]) + len(temp[temp == 14])
	return temp_2

temp = data3['source_type'].groupby(data3['customer_id']).apply(fun)

# 把等号前面换成你想要的名字
meiqiming_3 = sum(temp)		#  23608

del temp
print('meiqiming_3 =', meiqiming_3)
















     
