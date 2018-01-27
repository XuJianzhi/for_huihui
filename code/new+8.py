
#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd
from datetime import datetime
from collections import Counter

#path_in='C:/Users/liangzhihui/Desktop/S500.xlsx' 
path_in='/home/m/桌面/for_huihui/data/20180126_1.xlsx'
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
#新加的功能2:	每个客户第一单的source_type是11或14的客户有多少个？
data3=data3.sort_values(by='created_at',ascending=True)

temp = data3['source_type'].groupby(data3['customer_id']).first()
# 把等号前面换成你想要的名字
meiqiming_2 = len(temp[temp == 11]) + len(temp[temp == 14])	

print('meiqiming_2 =', meiqiming_2)	# 4407
########################
#新加的功能2	（的另一种形式）： 每个客户第一单外的source_type是11或14的行数之和？
data3=data3.sort_values(by='created_at',ascending=True)

def fun(ser):
	temp = np.array(ser)[0:1]
	temp_2 = len(temp[temp == 11]) + len(temp[temp == 14])
	return temp_2

temp = data3['source_type'].groupby(data3['customer_id']).apply(fun)
# 把等号前面换成你想要的名字
meiqiming_2 = sum(temp)
print('meiqiming_2 =', meiqiming_2)			# 4407
########################
#新加的功能3： 每个客户第一单外的source_type是11或14的行数之和？
data3=data3.sort_values(by='created_at',ascending=True)

def fun(ser):
	temp = np.array(ser)[1:]
	temp_2 = len(temp[temp == 11]) + len(temp[temp == 14])
	return temp_2

temp = data3['source_type'].groupby(data3['customer_id']).apply(fun)

# 把等号前面换成你想要的名字
meiqiming_3 = sum(temp)

print('meiqiming_3 =', meiqiming_3)		#  1162

##################################
#新加功能2的检测1：	计算每个客户第一行的source_type的各个值分别对应多少客户？
data3=data3.sort_values(by='created_at',ascending=True)

temp = data3['source_type'].groupby(data3['customer_id']).first()

number_first = pd.Series(Counter(temp))

print number_first
#print number_first.sum()
##################################
#新加功能2的检测2：	计算source_type中11和14的行数
temp = data3['source_type']
temp = pd.Series(Counter(temp))
temp = temp[11] + temp[14]
print(temp)
#print(temp.sum())

########################
#新加的功能3的检测1： 每个客户所有单的source_type是11或14的行数之和？
data3=data3.sort_values(by='created_at',ascending=True)

def fun(ser):
	temp = np.array(ser)
	temp_2 = len(temp[temp == 11]) + len(temp[temp == 14])
	return temp_2

temp = data3['source_type'].groupby(data3['customer_id']).apply(fun)

# 把等号前面换成你想要的名字
meiqiming_4 = sum(temp)	

print('meiqiming_4 =', meiqiming_4)		# 5569

#########################
# 功能4： 一个客户的记录里，只要appoint_person有相同就计数，最后返回有多少个这样条件的客户
data2=data2.sort_values(by='created_at',ascending=True)

def fun(ser):
	temp = np.array(ser)
	temp_2 = pd.Series(Counter(temp))
	if len(temp_2[temp_2 > 1]) > 0 :
		return 1
	else : 
		return 0

temp_3 = data2['appoint_person'].groupby(data2['customer_id']).apply(fun)

# 把等号前面换成你想要的名字
meiqiming_5 = sum(temp_3)	

print('meiqiming_5 =', meiqiming_5)		# 6216 / 9663


















     
