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
data = pd.read_csv('jd_air_condition_3.csv', encoding='utf-8-sig')

 # 商品价格分析
# 描述性统计分析
print(data['price'].describe())
# 价格分布直方图
plt.xlim(0, 20000) #x轴范围
plt.figure(figsize=(20, 9))
plt.hist(data['price'], bins=30, alpha=0.6, color='red')
plt.title('价格频数分布直方图')
plt.xlabel('价格')
plt.ylabel('频数')
plt.savefig('价格分布直方图.png')