#coding=utf-8-sig
# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
import pandas as pd



# 词云可视化
# 读取news_data.csv，保存到新建的news_data.txt中
data = pd.read_csv('jd_air_condition_3_2.csv', encoding='utf-8-sig')
with open('news_data_6.txt', 'a+', encoding='utf-8-sig') as f:
    for line in data.values:
        # str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        f.write((str(line[10])  + '\n'))

# 构建并配置词云对象w
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 对来自外部文件的文本进行中文分词，得到string
f = open('news_data_6.txt',encoding='utf-8-sig')
txt = f.read()
txtlist = jieba.cut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('output-gesture_1.png')