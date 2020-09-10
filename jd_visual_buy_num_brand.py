#coding=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # ��ͼʱ��ʾ��������
mpl.rcParams['font.serif'] = ['KaiTi']

lc=pd.DataFrame(pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig'))
# print(lc["brand"])
# lc.loc[lc["brand"] != "TCL"].head()
# a = lc.loc[lc['price'] > 5000].price.count()
a0 = lc.loc[lc["brand"] == " ����"].comment_count.sum()
a1 = lc.loc[lc["brand"] == " �¿�˹"].comment_count.sum()
a2 = lc.loc[lc["brand"] == " ����"].comment_count.sum()
a3 = lc.loc[lc["brand"] == " ־��"].comment_count.sum()
a4 = lc.loc[lc["brand"] == " TCL"].comment_count.sum()
a5 = lc.loc[lc["brand"] == " ����"].comment_count.sum()
a6 = lc.loc[lc["brand"] == " ����"].comment_count.sum()
a7 = lc.loc[lc["brand"] == " С��"].comment_count.sum()
a8 = lc.loc[lc["brand"] == " ����"].comment_count.sum()
a9 = lc.loc[lc["brand"] == " ����"].comment_count.sum()
a = lc['comment_count'].sum()



# a0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
waters = ('����', '�¿�˹', '����', '־��', 'TCL','����','����','С��','����','����')
buy_number = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
for x, y in enumerate(buy_number):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
plt.bar(waters, buy_number)
plt.ylabel('������')  # �����������
plt.title('��ͬƷ���г��������')
plt.savefig('Ʒ����������.png')
plt.show()



# �������趨Ϊ�����Ρ���Բ��
plt.figure(figsize=(8, 8))

label = ['����', '�¿�˹', '����', '־��', 'TCL', '����', '����', 'С��', '����', '����']

# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0, 0, 0, 0.05, 0, 0, 0.05, 0.1, 0.15,]

values = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]

plt.pie(values,
        explode=explode,
        labels=label,
        autopct='%1.1f%%',
        startangle=90,
        radius=0.9,
        counterclock=False,  # ������˳ʱ�룿��ʱ�룿
        wedgeprops={'linewidth': 0.4, 'edgecolor': 'red'},  # ���ñ�ͼ����߿����ԡ�
        textprops={'fontsize': 18, 'color': 'k'},  # �����ı�������ֵ��kΪ��ɫ��
        center=(0, 0),  # ��ͼ��ԭ�㡣
        pctdistance=0.7,  # �ٷֱ����ݱ�ǩ��Բ�ĵľ��롣
        labeldistance=1.2,  # �������'����'��ǩ��Բ�ĵľ��롣
        )

plt.title('��ͬƷ�ƿյ��г�����ռ��')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('��ͬƷ�ƿյ��г�����ռ��.png')
plt.show()