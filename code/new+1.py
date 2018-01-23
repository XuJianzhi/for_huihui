

#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd



#path_in='C:/Users/liangzhihui/Desktop/S500.xlsx' 
path_in='/home/m/桌面/for_huihui/S500.xlsx'
result=pd.read_excel(path_in)

buyers_id = result.customer_id.unique()		#从原来的文件复制过来的

data2=result.set_index('customer_id')	#从原来的文件复制过来的
data2=data2.sort_values(by='created_at',ascending=True)

data2['delta_price_2']=np.nan
for name in buyers_id:
	if type(data2.loc[name,'seller_price'])==np.int64 :		#改了
		data2.loc[name,'delta_price_2']=0
	else:
		array1=np.array(data2.loc[name,'seller_price'])
		data2.loc[name,'delta_price_2']=array1[0]-array1[-1]
         
         
data2=data2.reset_index()



#######################
data2=data2.sort_values(by='created_at',ascending=True)

def fun(ser):
	return ser-np.array(ser)[-1]

data2['delta_price_3']=data2['seller_price'].groupby(data2['customer_id']).apply(fun)
          
          
          
          
          
          
          
          
          
