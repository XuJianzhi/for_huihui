
#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd
from datetime import datetime
from collections import Counter


########################
# 功能5： “once_dealer”里的人在“全部”里source_type第一行是5或13的，共几人？
path_in = '/home/m/桌面/for_huihui/data/'
once_dealer = pd.read_excel(path_in + 'once_dealer.xlsx')
once_dealer = np.array(once_dealer.iloc[:,0])

#下同
all_data = pd.read_excel(path_in + 'all.xlsx')

all_data_2 = all_data.copy()
for i in all_data_2.index :
	if all_data_2.loc[i, 'customer_id'] not in once_dealer :
		all_data_2.drop(i, inplace = True)
		
all_data_2 = all_data_2.sort_values(by='created_at',ascending=True)

temp = all_data_2['source_type'].groupby(all_data_2['customer_id']).first()
# 把等号前面换成你想要的名字
meiqiming_6 = len(temp[temp == 5]) + len(temp[temp == 13])	

print('meiqiming_6 =', meiqiming_6)	# 3274

########################
# 功能6： 在“more_than_once”里source_type是5或13的人，在“全部”里source_type第一行是5或13的，共几人？
path_in = '/home/m/桌面/for_huihui/data/'
data = pd.read_excel(path_in + 'more_than_once.xlsx')
temp = data['source_type'].groupby(data['customer_id']).first()
chosen = list(temp[temp==5].index) + list(temp[temp==13].index) 


#下同
all_data = pd.read_excel(path_in + 'all.xlsx')

all_data_2 = all_data.copy()
for i in all_data_2.index :
	if all_data_2.loc[i, 'customer_id'] not in chosen :
		all_data_2.drop(i, inplace = True)
		
all_data_2 = all_data_2.sort_values(by='created_at',ascending=True)

temp = all_data_2['source_type'].groupby(all_data_2['customer_id']).first()
# 把等号前面换成你想要的名字
meiqiming_7 = len(temp[temp == 5]) + len(temp[temp == 13])	

print('meiqiming_7 =', meiqiming_7)		# 

############################################
# 功能7： 功能5和6的人加在一起，在20180127.xlsx中出，在列is_consigned的第一行等于1的客户数, 列 label_value的第一行等于1,2,3各自的客户数
path_in = '/home/m/桌面/for_huihui/data/'
once_dealer = pd.read_excel(path_in + 'once_dealer.xlsx')
once_dealer = list(once_dealer.iloc[:,0])

data = pd.read_excel(path_in + 'more_than_once.xlsx')
temp = data['source_type'].groupby(data['customer_id']).first()
chosen = list(temp[temp==5].index) + list(temp[temp==13].index) 

persons = once_dealer + chosen

##

data = pd.read_excel(path_in + '20180127.xlsx')
data2 = data.set_index('customer_id')
data3 = data2.loc[persons, :]

##

data3 = data3.reset_index()
data3 = data3.sort_values(by='created_at',ascending=True)

##

data4 = data3['is_consigned'].groupby(data3['customer_id']).first()

number_1 = len(data4[data4 == 1])
print('列is_consigned等于1的客户数: ')
print(number_1)
print


data5 = data3['label_value'].groupby(data3['customer_id']).first()

number_2 = len(data5[data5 == 1])
number_3 = len(data5[data5 == 2])
number_4 = len(data5[data5 == 3])

print
print('列label_value等于1的客户数: ')
print(number_2)
print
print('列label_value等于2的客户数: ')
print(number_3)
print
print('列label_value等于3的客户数: ')
print(number_4)
print

###########################################
#功能8： 一次看了就买的人的记录（行们）
path_in = '/home/m/桌面/for_huihui/data/'
data = pd.read_excel(path_in + '20180129.xlsx')

data2 = data.copy()

lines_number = data2['appoint_status'].groupby(data2['customer_id']).count()	# 已确定该列无nan
one_line = lines_number[lines_number == 1]
many_lines = lines_number[lines_number != 1]
data3 = data2.set_index('customer_id')
data4 = data3.loc[one_line.index, :]

data4.reset_index(inplace=True)

data5 = data4[data4['appoint_status'] == 2]

print('len(data2)==' + str(len(data2)))
print('len(one_line)==' + str(len(one_line)))
print('len(data3.loc[many_lines,:])==' + str(len(data3.loc[many_lines.index,:])))
print('len(data3)==' + str(len(data3)))
print('len(data4)==' + str(len(data4)))
print('len(data5)==' + str(len(data5)))

data5.to_excel(path_in + '20180129_output.xlsx')

# 上述算法缺陷是无法考虑一人买多车的情况，故结果可能比实际情况偏少
# 下为改良版
path_in = '/home/m/桌面/for_huihui/data/'
data = pd.read_excel(path_in + '20180129.xlsx')

data2 = data.copy()
'''
def fun(s):	# 一个人买了几次
	return s - s + len(s[s==2])
aa = data2['appoint_status'].groupby(data2['customer_id']).apply(fun)	#证明有人买了两次
'''

data2 = data2.sort_values(by='created_at',ascending=True)
first_appoint_status = data2['appoint_status'].groupby(data2['customer_id']).first()	# 已确定该列无nan
first_success = first_appoint_status[first_appoint_status==2].index

data3 = data2.set_index('customer_id')
data4 = data3.loc[first_success, :]

data4.reset_index(inplace=True)
data4.to_excel(path_in + '20180129_output_20:00.xlsx')

# 进一步研究
lines_number = data4['appoint_status'].groupby(data4['customer_id']).count()	# 已确定该列无nan
times = pd.Series(Counter(lines_number))
print(times)








     
