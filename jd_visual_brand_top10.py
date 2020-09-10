#coding=gbk
# ������صĿ⼰��ȡ����
import pandas as pd
import operator
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # ��ͼʱ��ʾ��������
mpl.rcParams['font.serif'] = ['KaiTi']



# ��ȡ��ȡ������
data = pd.read_csv('jd_air_condition_3_1.csv', encoding='utf-8-sig')
# df = pd.read_csv('jd_air_condition_3_1.csv',header=None,names=['brand','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'])
# df.to_csv('jd_air_condition_3_1.csv',index=False,encoding='utf-8-sig')
# ���۵طֲ�
group_data = list(data.groupby('brand'))
loc_num = {}
for i in range(len(group_data)):
    loc_num[group_data[i][0]] = len(group_data[i][1])
print(loc_num)
plt.figure(figsize=(20, 10))
plt.title('Ʒ������ͼ')
plt.scatter(list(loc_num.keys()), list(loc_num.values()), color='r')
plt.plot(list(loc_num.keys()), list(loc_num.values()))
plt.xlabel('Ʒ��')
plt.ylabel('����')
plt.savefig('Ʒ��.png')
sorted_loc_num = sorted(loc_num.items(), key=operator.itemgetter(1), reverse=True) #����
loc_num_10 = sorted_loc_num[:10]  #ȡǰ10
loc_10 = []
num_10 = []
for i in range(10):
    loc_10.append(loc_num_10[i][0])
    num_10.append(loc_num_10[i][1])
plt.figure(figsize=(16, 9))
plt.title('Ʒ��TOP10')
plt.xlabel('Ʒ��')
plt.ylabel('����')
plt.bar(loc_10, num_10, facecolor='lightskyblue', edgecolor='white')
plt.savefig('Ʒ��TOP10.png')
plt.show()