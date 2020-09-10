#coding=utf-8-sig
import csv

import pandas as pd



df = pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig')
# df = pd.read_csv('jd_air_condition_3.csv',header=None,names=['title','price','comment_count','default_good_count','good_count','general_count','poor_count','after_count','good_rate','mess'])



# with open("jd_air_condition_2.csv", "a", newline="", encoding='utf-8-sig') as csvfile:
#     rows = ('title', 'price', 'mess', 'comment')
#     writer = csv.writer(csvfile)
#     writer.writerow(rows)

# 增加列头
# df = pd.read_csv('jd_air_condition_1.csv',header=None,names=['title','price','mess','comment'])
"""
tf.csv是你当前目录下的csv文件名
names后面是你想要设置的表头
切记:header值为None,不能是False,否则会报错
"""



# 切分，删除源数据列
# df[['title','shop_name']] = df['title'].str.split(',',expand=True)
# df.drop('title', axis=1, inplace=True)

# df[['a','b','c','d','e','f','g',]] = df['comment'].str.split(', ',expand=True)
# df.drop('comment', axis=1, inplace=True)



# 删除全空的行
df.dropna(how='all',inplace=True)
# df.drop([2])#删除第二行
# 删除重复数据行
df.drop_duplicates(['title','mess'],inplace=True)
# #删除多余列
# f=df.drop(columns='four')#或者写为：df.drop(columns='four',inplace=True)
# #或者del df['four']
# print(df)

df.to_csv('jd_air_condition_3.csv',index=False,encoding='utf-8-sig')





