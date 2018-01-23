


#!/user/bin/python
#coding:utf-8

import numpy as np
import pandas as pd
from tqdm import tqdm

path_in='/home/m/桌面/for_huihui/原始数据.csv' 
source=pd.read_csv(path_in)

tempt1	= source [source.source_type == 5]
tempt2	= source [source.source_type == 13]
tempt	= tempt1.append(tempt2)

have_bought = tempt	[tempt.dealer_category.isnull()]	\
					[tempt.appoint_status	== 2]
#检测第一步对不对
print(have_bought.loc[:,['appoint_status','source_type','dealer_categoty']])



#第二步
buyers_id = have_bought.customer_id.unique()

source_2 = source.set_index('customer_id')
result = source_2.loc[buyers_id,:]
result = result.reset_index()

#写入
path_out='/home/m/桌面/for_huihui/新数据.csv' 
result.to_csv(path_out,index=False)

###########################
###########################

data = result.set_index('customer_id')
#data = result.copy()
#out = pd.DataFrame(columns=['how_many_brands','minor_category_name','tag_name'])
data['how_many_brands'] = np.nan
data['delta_price'] = np.nan

for name in tqdm(buyers_id):
	if type(data.loc[name,'minor_category_name']) == str :
		data.loc[name,'how_many_brands'] = 1
	else :
		data.loc[name,'how_many_brands'] = data.loc[name,'minor_category_name'].unique().shape[0]	
	
	series = data.loc[name,'seller_price']
	data.loc[name,'delta_price'] = series.max() - series.min()
	
data = data.reset_index()
	
out = data[['customer_id','how_many_brands','minor_category_name','tag_name','delta_price']]

print(out.head())

#######################

tempt = data[['customer_id','how_many_brands']].drop_duplicates()
average_brands = tempt['how_many_brands'].sum() / len(buyers_id)

print(average_brands)








