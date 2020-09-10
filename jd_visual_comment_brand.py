#coding=gbk
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # ��ͼʱ��ʾ��������
mpl.rcParams['font.serif'] = ['KaiTi']

lc=pd.DataFrame(pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig'))
# print(lc["brand"])
# lc.loc[lc["brand"] != "TCL"].head()
# a = lc.loc[lc['price'] > 5000].price.count()
a0 = lc.loc[lc["brand"] == " ����"].good_count.sum()
a1 = lc.loc[lc["brand"] == " ����"].default_good_count.sum()
a2 = lc.loc[lc["brand"] == " ����"].general_count.sum()
a3 = lc.loc[lc["brand"] == " ����"].poor_count.sum()
a4 = lc.loc[lc["brand"] == " ����"].after_count.sum()

b0 = lc.loc[lc["brand"] == " �¿�˹"].good_count.sum()
b1 = lc.loc[lc["brand"] == " �¿�˹"].default_good_count.sum()
b2 = lc.loc[lc["brand"] == " �¿�˹"].general_count.sum()
b3 = lc.loc[lc["brand"] == " �¿�˹"].poor_count.sum()
b4 = lc.loc[lc["brand"] == " �¿�˹"].after_count.sum()

c0 = lc.loc[lc["brand"] == " ����"].good_count.sum()
c1 = lc.loc[lc["brand"] == " ����"].default_good_count.sum()
c2 = lc.loc[lc["brand"] == " ����"].general_count.sum()
c3 = lc.loc[lc["brand"] == " ����"].poor_count.sum()
c4 = lc.loc[lc["brand"] == " ����"].after_count.sum()

d0 = lc.loc[lc["brand"] == " ־��"].good_count.sum()
d1 = lc.loc[lc["brand"] == " ־��"].default_good_count.sum()
d2 = lc.loc[lc["brand"] == " ־��"].general_count.sum()
d3 = lc.loc[lc["brand"] == " ־��"].poor_count.sum()
d4 = lc.loc[lc["brand"] == " ־��"].after_count.sum()

e0 = lc.loc[lc["brand"] == " ����"].good_count.sum()
e1 = lc.loc[lc["brand"] == " ����"].default_good_count.sum()
e2 = lc.loc[lc["brand"] == " ����"].general_count.sum()
e3 = lc.loc[lc["brand"] == " ����"].poor_count.sum()
e4 = lc.loc[lc["brand"] == " ����"].after_count.sum()

a = lc['comment_count'].sum()


# # a0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
# waters = ('����', '�¿�˹', '����', '־��', 'TCL','����','����','С��','����','����')
# buy_number = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
# for x, y in enumerate(buy_number):
#     plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
# plt.bar(waters, buy_number)
# plt.ylabel('������')  # �����������
# plt.title('��ͬƷ���г��������')
# plt.savefig('Ʒ����������.png')
# plt.show()



# # ��������������Ḻ�Ŵ���
# matplotlib.rc('font', family='SimHei', weight='bold')
# plt.rcParams['axes.unicode_minus'] = False

# �������趨Ϊ�����Ρ���Բ��
plt.figure(figsize=(8, 8))

label = ['����', 'Ĭ�Ϻ���', '����', '����', '׷��']

# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0.05, 0.01, 0, 0.1]

values = [a2, a1, a3, a0, a4]

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

plt.title('���Ŀյ��г��ͻ���ӳ')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('���Ŀյ��г��ͻ���ӳ.png')
plt.show()


plt.figure(figsize=(8, 8))

label = ['����', 'Ĭ�Ϻ���', '����', '����', '׷��']

# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0.05, 0.01, 0, 0.1]

values = [b2, b1, b3, b0, b4]

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

plt.title('�¿�˹�յ��г��ͻ���ӳ')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('�¿�˹�յ��г��ͻ���ӳ.png')
plt.show()

# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0.05, 0.01, 0, 0.1]

values = [c2, c1, c3, c0, c4]

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

plt.title('�����յ��г��ͻ���ӳ')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('�����յ��г��ͻ���ӳ.png')
plt.show()


# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
plt.figure(figsize=(8, 8))

label = ['����', 'Ĭ�Ϻ���', '����', '����', '׷��']

# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0.05, 0.01, 0, 0.1]

values = [d2, d1, d3, d0, d4]

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

plt.title('־�߿յ��г��ͻ���ӳ')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('־�߿յ��г��ͻ���ӳ.png')
plt.show()


# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0.05, 0.01, 0, 0.1]

values = [e2, e1, e3, e0, e4]

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

plt.title('�����յ��г��ͻ���ӳ')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('�����յ��г��ͻ���ӳ.png')
plt.show()

