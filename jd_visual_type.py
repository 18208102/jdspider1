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
a0 = lc.loc[lc["type"] == "�ڹ�ʽ"].type.count()
a1 = lc.loc[lc["type"] == "����ʽ"].type.count()


# �������趨Ϊ�����Ρ���Բ��
plt.figure(figsize=(8, 8))

label = ['�ڹ�ʽ', '����ʽ']

# ͻ����ʾĳһ���Ρ�����Բ��n���뾶��
explode = [0, 0]

values = [a0, a1]

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

plt.title('�յ������г�ռ��')  # ���Ʊ���

# ͼ����λ�á�
# bbox_to_anchorǰһ��������ʾ���ҡ��ڶ������������¡�
# ncolͼ��һ����ʾ��
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('�յ������г�ռ��.png')
plt.show()