

#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd
from datetime import datetime


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

def fun(ser):
	#print(ser)
	ser2 = np.array(ser)
	end_time = datetime.strptime(ser2[-1][:-2], '%Y-%m-%d %H:%M:%S')
	start_time = datetime.strptime(ser2[0][:-2], '%Y-%m-%d %H:%M:%S')

	delta_time = end_time - start_time
	delta_time_str = str(delta_time)
	
	return pd.Series([delta_time_str] * len(ser), index=ser.index)

data2['delta_time']=data2['_col4'].groupby(data2['customer_id']).apply(fun)












#ttt = data2.loc[data2['customer_id']==674879, ['customer_id', '_col4', 'delta_time']]




     
