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
data = pd.read_csv('jd_air_condition_3.csv', encoding='utf-8-sig')

 # ��Ʒ�۸����
# ������ͳ�Ʒ���
print(data['price'].describe())
# �۸�ֲ�ֱ��ͼ
plt.xlim(0, 20000) #x�᷶Χ
plt.figure(figsize=(20, 9))
plt.hist(data['price'], bins=30, alpha=0.6, color='red')
plt.title('�۸�Ƶ���ֲ�ֱ��ͼ')
plt.xlabel('�۸�')
plt.ylabel('Ƶ��')
plt.savefig('�۸�ֲ�ֱ��ͼ.png')