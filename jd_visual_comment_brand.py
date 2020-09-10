#coding=gbk
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # 画图时显示楷体中文
mpl.rcParams['font.serif'] = ['KaiTi']

lc=pd.DataFrame(pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig'))
# print(lc["brand"])
# lc.loc[lc["brand"] != "TCL"].head()
# a = lc.loc[lc['price'] > 5000].price.count()
a0 = lc.loc[lc["brand"] == " 美的"].good_count.sum()
a1 = lc.loc[lc["brand"] == " 美的"].default_good_count.sum()
a2 = lc.loc[lc["brand"] == " 美的"].general_count.sum()
a3 = lc.loc[lc["brand"] == " 美的"].poor_count.sum()
a4 = lc.loc[lc["brand"] == " 美的"].after_count.sum()

b0 = lc.loc[lc["brand"] == " 奥克斯"].good_count.sum()
b1 = lc.loc[lc["brand"] == " 奥克斯"].default_good_count.sum()
b2 = lc.loc[lc["brand"] == " 奥克斯"].general_count.sum()
b3 = lc.loc[lc["brand"] == " 奥克斯"].poor_count.sum()
b4 = lc.loc[lc["brand"] == " 奥克斯"].after_count.sum()

c0 = lc.loc[lc["brand"] == " 海尔"].good_count.sum()
c1 = lc.loc[lc["brand"] == " 海尔"].default_good_count.sum()
c2 = lc.loc[lc["brand"] == " 海尔"].general_count.sum()
c3 = lc.loc[lc["brand"] == " 海尔"].poor_count.sum()
c4 = lc.loc[lc["brand"] == " 海尔"].after_count.sum()

d0 = lc.loc[lc["brand"] == " 志高"].good_count.sum()
d1 = lc.loc[lc["brand"] == " 志高"].default_good_count.sum()
d2 = lc.loc[lc["brand"] == " 志高"].general_count.sum()
d3 = lc.loc[lc["brand"] == " 志高"].poor_count.sum()
d4 = lc.loc[lc["brand"] == " 志高"].after_count.sum()

e0 = lc.loc[lc["brand"] == " 格力"].good_count.sum()
e1 = lc.loc[lc["brand"] == " 格力"].default_good_count.sum()
e2 = lc.loc[lc["brand"] == " 格力"].general_count.sum()
e3 = lc.loc[lc["brand"] == " 格力"].poor_count.sum()
e4 = lc.loc[lc["brand"] == " 格力"].after_count.sum()

a = lc['comment_count'].sum()


# # a0 = lc.loc[(lc['brand'] == ' 美的') & (lc['price'] < 1000)].price.count()
# waters = ('美的', '奥克斯', '海尔', '志高', 'TCL','海信','格力','小米','松下','科龙')
# buy_number = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
# for x, y in enumerate(buy_number):
#     plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
# plt.bar(waters, buy_number)
# plt.ylabel('销售量')  # 纵坐标轴标题
# plt.title('不同品牌市场销售情况')
# plt.savefig('品牌销售数量.png')
# plt.show()



# # 中文乱码和坐标轴负号处理。
# matplotlib.rc('font', family='SimHei', weight='bold')
# plt.rcParams['axes.unicode_minus'] = False

# 将画布设定为正方形。正圆。
plt.figure(figsize=(8, 8))

label = ['中评', '默认好评', '差评', '好评', '追评']

# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0.05, 0.01, 0, 0.1]

values = [a2, a1, a3, a0, a4]

plt.pie(values,
        explode=explode,
        labels=label,
        autopct='%1.1f%%',
        startangle=90,
        radius=0.9,
        counterclock=False,  # 数据是顺时针？逆时针？
        wedgeprops={'linewidth': 0.4, 'edgecolor': 'red'},  # 设置饼图内外边框属性。
        textprops={'fontsize': 18, 'color': 'k'},  # 设置文本的属性值。k为黑色。
        center=(0, 0),  # 饼图的原点。
        pctdistance=0.7,  # 百分比数据标签与圆心的距离。
        labeldistance=1.2,  # 设置外层'城市'标签与圆心的距离。
        )

plt.title('美的空调市场客户反映')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('美的空调市场客户反映.png')
plt.show()


plt.figure(figsize=(8, 8))

label = ['中评', '默认好评', '差评', '好评', '追评']

# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0.05, 0.01, 0, 0.1]

values = [b2, b1, b3, b0, b4]

plt.pie(values,
        explode=explode,
        labels=label,
        autopct='%1.1f%%',
        startangle=90,
        radius=0.9,
        counterclock=False,  # 数据是顺时针？逆时针？
        wedgeprops={'linewidth': 0.4, 'edgecolor': 'red'},  # 设置饼图内外边框属性。
        textprops={'fontsize': 18, 'color': 'k'},  # 设置文本的属性值。k为黑色。
        center=(0, 0),  # 饼图的原点。
        pctdistance=0.7,  # 百分比数据标签与圆心的距离。
        labeldistance=1.2,  # 设置外层'城市'标签与圆心的距离。
        )

plt.title('奥克斯空调市场客户反映')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('奥克斯空调市场客户反映.png')
plt.show()

# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0.05, 0.01, 0, 0.1]

values = [c2, c1, c3, c0, c4]

plt.pie(values,
        explode=explode,
        labels=label,
        autopct='%1.1f%%',
        startangle=90,
        radius=0.9,
        counterclock=False,  # 数据是顺时针？逆时针？
        wedgeprops={'linewidth': 0.4, 'edgecolor': 'red'},  # 设置饼图内外边框属性。
        textprops={'fontsize': 18, 'color': 'k'},  # 设置文本的属性值。k为黑色。
        center=(0, 0),  # 饼图的原点。
        pctdistance=0.7,  # 百分比数据标签与圆心的距离。
        labeldistance=1.2,  # 设置外层'城市'标签与圆心的距离。
        )

plt.title('海尔空调市场客户反映')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('海尔空调市场客户反映.png')
plt.show()


# 突出显示某一扇形。距离圆心n个半径。
plt.figure(figsize=(8, 8))

label = ['中评', '默认好评', '差评', '好评', '追评']

# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0.05, 0.01, 0, 0.1]

values = [d2, d1, d3, d0, d4]

plt.pie(values,
        explode=explode,
        labels=label,
        autopct='%1.1f%%',
        startangle=90,
        radius=0.9,
        counterclock=False,  # 数据是顺时针？逆时针？
        wedgeprops={'linewidth': 0.4, 'edgecolor': 'red'},  # 设置饼图内外边框属性。
        textprops={'fontsize': 18, 'color': 'k'},  # 设置文本的属性值。k为黑色。
        center=(0, 0),  # 饼图的原点。
        pctdistance=0.7,  # 百分比数据标签与圆心的距离。
        labeldistance=1.2,  # 设置外层'城市'标签与圆心的距离。
        )

plt.title('志高空调市场客户反映')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('志高空调市场客户反映.png')
plt.show()


# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0.05, 0.01, 0, 0.1]

values = [e2, e1, e3, e0, e4]

plt.pie(values,
        explode=explode,
        labels=label,
        autopct='%1.1f%%',
        startangle=90,
        radius=0.9,
        counterclock=False,  # 数据是顺时针？逆时针？
        wedgeprops={'linewidth': 0.4, 'edgecolor': 'red'},  # 设置饼图内外边框属性。
        textprops={'fontsize': 18, 'color': 'k'},  # 设置文本的属性值。k为黑色。
        center=(0, 0),  # 饼图的原点。
        pctdistance=0.7,  # 百分比数据标签与圆心的距离。
        labeldistance=1.2,  # 设置外层'城市'标签与圆心的距离。
        )

plt.title('格力空调市场客户反映')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('格力空调市场客户反映.png')
plt.show()

