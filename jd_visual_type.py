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
a0 = lc.loc[lc["type"] == "壁挂式"].type.count()
a1 = lc.loc[lc["type"] == "立柜式"].type.count()


# 将画布设定为正方形。正圆。
plt.figure(figsize=(8, 8))

label = ['壁挂式', '立柜式']

# 突出显示某一扇形。距离圆心n个半径。
explode = [0, 0]

values = [a0, a1]

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

plt.title('空调类型市场占比')  # 绘制标题

# 图例的位置。
# bbox_to_anchor前一个参数表示左右。第二个参数是上下。
# ncol图例一列显示。
plt.legend(loc='center right', bbox_to_anchor=(1.2, 0.5), ncol=1)
plt.savefig('空调类型市场占比.png')
plt.show()