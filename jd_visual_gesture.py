#coding=utf-8-sig
# �������������wordcloud�����ķִʿ�jieba
import jieba
import wordcloud
import pandas as pd



# ���ƿ��ӻ�
# ��ȡnews_data.csv�����浽�½���news_data.txt��
data = pd.read_csv('jd_air_condition_3_2.csv', encoding='utf-8-sig')
with open('news_data_6.txt', 'a+', encoding='utf-8-sig') as f:
    for line in data.values:
        # str(line[0])��csv�е�0�У�+','+��csv����֮�䱣�浽txt�ö��ţ�����������'\n'����ȡcsvÿ�к���txt�л���
        f.write((str(line[10])  + '\n'))

# ���������ô��ƶ���w
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# �������ⲿ�ļ����ı��������ķִʣ��õ�string
f = open('news_data_6.txt',encoding='utf-8-sig')
txt = f.read()
txtlist = jieba.cut(txt)
string = " ".join(txtlist)

# ��string��������w��generate()��������������������
w.generate(string)

# ������ͼƬ��������ǰ�ļ���
w.to_file('output-gesture_1.png')