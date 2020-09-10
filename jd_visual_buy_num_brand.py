#coding=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']  # 画图时显示楷体中文
mpl.rcParams['font.serif'] = ['KaiTi']

lc=pd.DataFrame(pd.read_csv('../jdspider/jd_air_condition_3.csv',encoding='utf-8-sig'))
# print(lc["brand"])
# lc.loc[lc["brand"] != "TCL"].head()
# a = lc.loc[lc['price'] > 5000].price.count()
a0 = lc.loc[lc["brand"] == " 美的"].comment_count.sum()
a1 = lc.loc[lc["brand"] == " 奥克斯"].comment_count.sum()
a2 = lc.loc[lc["brand"] == " 海尔"].comment_count.sum()
a3 = lc.loc[lc["brand"] == " 志高"].comment_count.sum()
a4 = lc.loc[lc["brand"] == " TCL"].comment_count.sum()
a5 = lc.loc[lc["brand"] == " 海信"].comment_count.sum()
a6 = lc.loc[lc["brand"] == " 格力"].comment_count.sum()
a7 = lc.loc[lc["brand"] == " 小米"].comment_count.sum()
a8 = lc.loc[lc["brand"] == " 松下"].comment_count.sum()
a9 = lc.loc[lc["brand"] == " 科龙"].comment_count.sum()
a = lc['comment_count'].sum()



# a0 = lc.loc[(lc['brand'] == ' 美的') & (lc['price'] < 1000)].price.count()
waters = ('美的', '奥克斯', '海尔', '志高', 'TCL','海信','格力','小米','松下','科龙')
buy_number = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
for x, y in enumerate(buy_number):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
plt.bar(waters, buy_number)
plt.ylabel('销售量')  # 纵坐标轴标题
plt.title('不同品牌市场销售情况')
plt.savefig('品牌销售数量.png')
plt.show()



# 将画布设定为正方形。正圆。
plt.figure(figsize=(8, 8))

label = ['美的', '奥克斯', '海尔', '志高', 'TCL', '海信', '格力', '小米', '松下', '科龙']

# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0, 0, 0, 0.05, 0, 0, 0.05, 0.1, 0.15,]

values = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]

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

plt.title('不同品牌空调市场销售占比')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('不同品牌空调市场销售占比.png')
plt.show()