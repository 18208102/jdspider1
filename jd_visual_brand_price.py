#coding=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # ��ͼʱ��ʾ��������
mpl.rcParams['font.serif'] = ['KaiTi']

# df = pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig')
# df = pd.read_csv('jd_air_condition_3.csv',header=None,names=['title','price','comment_count','default_good_count','good_count','general_count','poor_count','after_count','good_rate','brand','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'])
# df.to_csv('jd_air_condition_3.csv',index=False,encoding='utf-8-sig')

lc=pd.DataFrame(pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig'))
# print(lc["brand"])
# lc.loc[lc["brand"] != "TCL"].head()
# a = lc.loc[lc['price'] > 5000].price.count()

a0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
a1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] < 1000)].price.count()
a2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
a3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] < 1000)].price.count()
a4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] < 1000)].price.count()
a5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
a6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
a7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] < 1000)].price.count()
a8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
a9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()
# a = lc.loc[(lc['brand'] == ' ����') & (lc['price'] < 1000)].price.count()

b0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()
b9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 1000) & (lc['price'] <= 2000) ].price.count()



c0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()
c9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 2000) & (lc['price'] <= 3000) ].price.count()


d0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()
d9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 3000) & (lc['price'] <= 4000) ].price.count()

e0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()
e9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 4000) & (lc['price'] <= 5000) ].price.count()

f0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()
f9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 5000) & (lc['price'] <= 6000) ].price.count()

g0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()
g9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 6000) & (lc['price'] <= 7000) ].price.count()

h0 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 7000)].price.count()
h1 = lc.loc[(lc['brand'] == ' �¿�˹') & (lc['price'] > 7000)].price.count()
h2 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 7000)].price.count()
h3 = lc.loc[(lc['brand'] == ' ־��') & (lc['price'] > 7000)].price.count()
h4 = lc.loc[(lc['brand'] == ' TCL') & (lc['price'] > 7000)].price.count()
h5 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 7000)].price.count()
h6 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 7000)].price.count()
h7 = lc.loc[(lc['brand'] == ' С��') & (lc['price'] > 7000)].price.count()
h8 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 7000)].price.count()
h9 = lc.loc[(lc['brand'] == ' ����') & (lc['price'] > 7000)].price.count()



#
# # ��������
# x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# y_data = [a0, a1, a2, a3, a4, a5, a6, a7 ,a8 ,a9 ]
# y_data2 = [b0, b1, b2, b3, b4, b5, b6, b7 ,b8 ,b9]
# bar_width = 0.3
# # ��X�����ݸ�Ϊʹ��range(len(x_data), ����0��1��2...
# plt.bar(x=range(len(x_data)), height=y_data, label='C���Ի���',
#         color='steelblue', alpha=0.8, width=bar_width)
# # ��X�����ݸ�Ϊʹ��np.arange(len(x_data))+bar_width,
# # ����bar_width��1+bar_width��2+bar_width...�����ͺ͵�һ����״ͼ������
# plt.bar(x=np.arange(len(x_data)) + bar_width, height=y_data2,
#         label='Java����', color='indianred', alpha=0.8, width=bar_width)
# # ����״ͼ����ʾ������ֵ, ha�������뷽��ˮƽ��ʽ, va���ƴ�ֱ���뷽ʽ
# for x, y in enumerate(y_data):
#     plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
# for x, y in enumerate(y_data2):
#     plt.text(x + bar_width, y + 100, '%s' % y, ha='center', va='top')
# # ���ñ���
# plt.title("C��Java�Ա�")
# # Ϊ������������������
# plt.xlabel("���")
# plt.ylabel("����")
# plt.savefig('Ʒ�Ƽ۸�.png')
# # ��ʾͼ��
# plt.legend()
# plt.show()

# # �����д����� plt ������ʾ������
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# ����ͳ������
waters = ('����', '�¿�˹', '����', '־��', 'TCL','����','����','С��','����','����')
y_number_1 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
y_number_2 = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]
y_number_3 = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
y_number_4 = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
y_number_5 = [e0, e1, e2, e3, e4, e5, e6, e7, e8, e9]
y_number_6 = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9]
y_number_7 = [g0, g1, g2, g3, g4, g5, g6, g7, g8, g9]
y_number_8 = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9]


bar_width = 0.1  # ���ο��
index_1 = np.arange(len(waters))  # 0~1000����ͼ�ĺ�����
index_2 = index_1 + bar_width  # 1000~2000����ͼ�ĺ�����
index_3 = index_1 + bar_width*2  # 2000~3000����ͼ�ĺ�����
index_4 = index_1 + bar_width*3  # 3000~4000����ͼ�ĺ�����
index_5 = index_1 + bar_width*4  # 4000~5000����ͼ�ĺ�����
index_6 = index_1 + bar_width*5  # 5000~6000����ͼ�ĺ�����
index_7 = index_1 + bar_width*6  # 6000~7000����ͼ�ĺ�����
index_8 = index_1 + bar_width*7  # 7000~~����ͼ�ĺ�����


# ʹ������ bar ����������������ͼsteelblue
plt.bar(index_1, height=y_number_1, width=bar_width, color='red', label='0~1000')
plt.bar(index_2, height=y_number_2, width=bar_width, color='orange', label='1000~2000')
plt.bar(index_3, height=y_number_3, width=bar_width, color='yellow', label='2000~3000')
plt.bar(index_4, height=y_number_4, width=bar_width, color='green', label='3000~4000')
plt.bar(index_5, height=y_number_5, width=bar_width, color='cyan', label='4000~5000')
plt.bar(index_6, height=y_number_6, width=bar_width, color='blue', label='5000~6000')
plt.bar(index_7, height=y_number_7, width=bar_width, color='violet', label='6000~7000')
plt.bar(index_8, height=y_number_8, width=bar_width, color='grey', label='6000~7000')

plt.legend()  # ��ʾͼ��
plt.xticks(index_1 + bar_width/2, waters)  # �ú�������̶���ʾ Ʒ�ƣ� index_male + bar_width/2 Ϊ��������̶ȵ�λ��
plt.ylabel('����')  # �����������
plt.title('��ͬƷ�ƶ�Ӧ��ͬ�۸�������г����')  # ͼ�α���
plt.savefig('Ʒ�Ƽ۸�.png')

# plt.show()
