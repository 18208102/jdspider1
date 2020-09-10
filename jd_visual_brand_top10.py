#coding=gbk
# 导入相关的库及读取数据
import pandas as pd
import operator
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # 画图时显示楷体中文
mpl.rcParams['font.serif'] = ['KaiTi']



# 获取爬取的数据
data = pd.read_csv('jd_air_condition_3_1.csv', encoding='utf-8-sig')
# df = pd.read_csv('jd_air_condition_3_1.csv',header=None,names=['brand','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'])
# df.to_csv('jd_air_condition_3_1.csv',index=False,encoding='utf-8-sig')
# 销售地分布
group_data = list(data.groupby('brand'))
loc_num = {}
for i in range(len(group_data)):
    loc_num[group_data[i][0]] = len(group_data[i][1])
print(loc_num)
plt.figure(figsize=(20, 10))
plt.title('品牌折线图')
plt.scatter(list(loc_num.keys()), list(loc_num.values()), color='r')
plt.plot(list(loc_num.keys()), list(loc_num.values()))
plt.xlabel('品牌')
plt.ylabel('个数')
plt.savefig('品牌.png')
sorted_loc_num = sorted(loc_num.items(), key=operator.itemgetter(1), reverse=True) #排序
loc_num_10 = sorted_loc_num[:10]  #取前10
loc_10 = []
num_10 = []
for i in range(10):
    loc_10.append(loc_num_10[i][0])
    num_10.append(loc_num_10[i][1])
plt.figure(figsize=(16, 9))
plt.title('品牌TOP10')
plt.xlabel('品牌')
plt.ylabel('个数')
plt.bar(loc_10, num_10, facecolor='lightskyblue', edgecolor='white')
plt.savefig('品牌TOP10.png')
plt.show()