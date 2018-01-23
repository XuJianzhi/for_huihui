

#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd



#path_in='C:/Users/liangzhihui/Desktop/S500.xlsx' 
path_in='/home/m/桌面/for_huihui/1.xlsx'
data2=pd.read_excel(path_in)



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

def time_change(time_str):
	#转换成时间数组
	timeArray = time.strptime(time_str[:-2], "%Y-%m-%d %H:%M:%S")
	#转换成时间戳
	timestamp = time.mktime(timeArray)
	#print(timestamp)
	return timestamp

def fun(ser):
	#print(ser)
	ser_2 = np.array(ser)
	delta_time = time_change(ser_2[-1]) - time_change(ser_2[0])
	#将时间戳变成localtime
	localtime = time.localtime(delta_time)
	#将localtime变成str
	delta_time_str = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
	#差值为零时 delta_time_str ='1970-01-01 08:00:00'，故需在各处减去

	return pd.Series([delta_time_str] * len(ser), index=ser.index)

data2['delta_time']=data2['_col4'].groupby(data2['customer_id']).apply(fun)







     
