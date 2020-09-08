#coding=utf-8-sig
import csv

import pandas as pd



df = pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig')
df = pd.read_csv('jd_air_condition_3.csv',header=None,names=['title','price','mess','comment'])



# with open("jd_air_condition_2.csv", "a", newline="", encoding='utf-8-sig') as csvfile:
#     rows = ('title', 'price', 'mess', 'comment')
#     writer = csv.writer(csvfile)
#     writer.writerow(rows)

# df = pd.read_csv('../jdspider/jd_air_condition_test.csv',encoding='utf-8-sig')
# df.head()

# 增加列头
# df = pd.read_csv('jd_air_condition_1.csv',header=None,names=['title','price','mess','comment'])
"""
tf.csv是你当前目录下的csv文件名
names后面是你想要设置的表头
切记:header值为None,不能是False,否则会报错
"""



# 切分，删除源数据列
df[['title','shop_name']] = df['title'].str.split(',',expand=True)
df.drop('title', axis=1, inplace=True)

# df[['a','b','c','d','e','f','g',]] = df['comment'].str.split(', ',expand=True)
# df.drop('comment', axis=1, inplace=True)
#
# df['mess'].str.split(', ',expand=True)
# df.drop('mess', axis=1, inplace=True)
#
#
# df.to_csv('jd_air_condition_1.csv',index=False,encoding='utf-8-sig')
# df = pd.read_csv('jd_air_condition_1.csv')
# df.drop([2])#删除第二行
# df.to_csv('jd_air_condition_1.csv',index=False,encoding='utf-8-sig')

# 删除重复数据行
# df.drop_duplicates(['first_name','last_name'],inplace=True)

#添加列名
# pd.read_csv('jd_air_condition.csv', header=None, names = ['title','price','mess','comment'] )

#
#
#
# 分割列

df = pd.read_csv('jd_air_condition_2.csv')
df['air_title'] = df['title'].map(lambda x:x.split[','][0])
df['shop_name'] = df['title'].map(lambda x:x.split[','][1])
df['title'].str.split(', ', expand=True)

# df.join(df['comment'].str.split(',',expand=True))
df.to_csv('jd_air_condition_test.csv',index=False,encoding='utf-8-sig')
# newline.to_csv('jd_air_condition_1.csv',index=False,encoding='utf-8-sig')

# data['mess'].str.split(',', expand=True)
# data['comment'].str.split(',', expand=True)
#
# pd.read_csv('jd_air_condition.csv', header=None, names = ['title','price','mess','comment'] )
# #
#
#
# # 删除全空的行
# df.dropna(how='all',inplace=True)

#
# #删除多余列
# f=df.drop(columns='four')#或者写为：df.drop(columns='four',inplace=True)
# #或者del df['four']
# print(df)







