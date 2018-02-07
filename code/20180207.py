
#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd
from datetime import datetime
from collections import Counter


#########################################
#20180205
#第一列“价格预期”：每个客户ID下的upper对应的价格减去lower对应的价格，再除以lower对应的价格。
#第二列“是否成交”：appoint_status=2代表成交，不等于2代表不成交，一个客户id下只要有等于2的就返回1，没有等于2的就返回0。
#前面还有一个清洗工作，就是黄色这列，一个客户只会有两个不同的价格数，比如这个客户是正常的，如果多于两个，这样的客户的所有信息你先删掉
path_in = '/home/m/桌面/for_huihui/data/20180207.xlsx'
data = pd.read_excel(path_in )

data2 = data.copy()
print(data2.shape)
print

#功能1：“几个车系”
def fun4(s):
	return pd.Series( [ len(s.unique()) ] * len(s), index = s.index)

data2['new_1'] = data2['tag_name'].groupby(data2['buyer_phone_encode']).apply(fun4)

#功能2：“是否成交”：appoint_status=2代表成交，不等于2代表不成交，一个客户id下只要有等于2的就返回1，没有等于2的就返回0。
def fun3(s):
	return s - s + ( 2 in s.values )

data2['new_3'] = data2['appoint_status'].groupby(data2['buyer_phone_encode']).apply(fun3)

#删列
#data2.drop_duplicates(data.columns.drop(['_col2']), inplace = True)
data2.drop(['appoint_status'], axis = 1, inplace = True)
print(data2.shape)
print
data2.drop_duplicates(inplace = True)
print(data2.shape)
print
'''
#删行1：一个客户如果有两个以上的value，就把这个客户的所有信息删了。 结论：都不大于二，不用删。
def fun1(s):
	return s - s + len(s.unique())
data2['value_kinds'] = data2['value'].groupby(data2['buyer_phone_encode']).apply(fun1)
aa=data2.value_numbers
print(aa[aa>2])
data2.drop(['value_kinds'], axis = 1, inplace = True)

#此时发现：每个人只有两行
print( float(data2.shape[0])/2 == len(data2.buyer_phone_encode.unique()) )
'''
#删行2：删去value等于0的客户的所有行。（经测试，value为零的行的name都是lower，没有upper。）
bad_customer = data2['buyer_phone_encode'] [ data2['price'] == 0 ]
data2.set_index('buyer_phone_encode', inplace = True)
data2.drop(bad_customer, inplace = True)
data2.reset_index(inplace = True)

#功能1：“价格预期”：每个客户ID下的upper对应的价格减去lower对应的价格，再除以lower对应的价格。
def fun2(s):
	upper = float( s.max() )
	lower = float( s.min() )
	rate = ( upper - lower ) / lower
	return s - s + rate

temp = data2['price'].groupby(data2['buyer_phone_encode']).apply(fun2)
temp2 = temp.copy()
#变成“66%”的格式
temp2 = (temp2 * 100).apply(int).apply(str) + '%'
data2['new_2'] = temp2

data3 = data2[ list(data2.columns[:-2]) + ['new_2'] + ['new_3'] ]

path_out = '/home/m/桌面/for_huihui/data/20180207_output.xlsx'
data3.to_excel( path_out )

















     
