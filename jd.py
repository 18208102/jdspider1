import csv
import urllib
import json
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re




#选择页码进行爬取
def JDSpiderPage():
    for page in range(197,201):
        url = "https://search.jd.com/Search?keyword=%E7%A9%BA%E8%B0%83&stop=1&qrst=1&vt=1&click=2&page=" + str(
            page) + "&s=" + str(1 + (page - 1) * 30) + "&click=0&scrolling=y"
        print("正在爬取第 {} 页".format(page))
        load_page(url)


#读取查询页面
def load_page(url):
    #定义请求头
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    #添加请求头
    request = urllib.request.Request(url,headers=headers)
    #发送请求头获得响应
    html = urllib.request.urlopen(request).read()
    content=etree.HTML(html)#转化为etree
    #获取商品详情页链接
    content_list=content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
    #对页面前30个商品进行统一处理
    for i in range(1,31):
        try:
            result = re.split(r":",content_list[i-1])[1]
            content_list[i-1]=result
        except Exception as e :
            continue
    for j in content_list:
        new_url='http:'+j#完整url
        #获取商品id
        split_url = j.replace('//item.jd.com/', '')
        # 第一次替换后，返回的结果是 123456.html
        split_url = split_url.replace('.html', '')
        # 第二次替换后，返回结果就是123456了
        #print(split_url)
        comment=get_goods_comment(split_url, headers)
        print(comment)
        #print(new_url)
        sum=load_link_page(new_url,headers)
        #print(sum)

        price=get_price(new_url)
        print(price)
        mess=load_link_page_mess(new_url,headers)
        #print(mess)
        print("----------------------------")
        #get_comment(new_url,headers)
        with open("jd_air_condition.csv", "a", newline="",encoding='utf-8') as csvfile:
             rows = (sum,price,mess,comment)
             writer = csv.writer(csvfile)
             writer.writerow(rows)





#获取信息 爬取商品标题和店家名称
def load_link_page(url,headers):
    #添加请求
    request = urllib.request.Request(url,headers=headers)
    #发送请求头获得响应
    #html=response.read()
    html = urllib.request.urlopen(request).read()
    content=etree.HTML(html)#转化为etree
    #空调标题
    air_title=content.xpath('//div[@class="itemInfo-wrap"]/div[@class="sku-name"]/text()')
    #空调价格
    #air_price=content.xpath('//div[@class="dd"]/span[@class="p-price"]/span/text()')
    # 空调品牌
    brand = content.xpath('//div[@class="p-parameter"]/ul[@id="parameter-brand"]/li/@title')
    #店家名称
    shop_name=content.xpath('//div[@class="name"]/a/@title')
    sum = dict()
    sum['air_title'] = air_title
    sum['shop_name'] = shop_name
    return sum

#爬取商品参数
def load_link_page_mess(url,headers):
    # 添加请求
    request = urllib.request.Request(url, headers=headers)
    # 发送请求头获得响应
    # html=response.read()
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html, "html.parser")
    divSoup = soup.find("div", attrs={"class", "p-parameter"})  ##找到其配置信息的标签

    # data = DataFrame(columns=["参数", "值"])  # 定义一个二元的DataFrame
    uls = divSoup.find_all("ul")
    list = []
    for ul in uls:
        lis = ul.find_all("li")
        for i in range(len(lis)):
            f=lis[i].getText()
            # print(f)
            list.append(f)
    return list
            #print(f)
            #return list


# 根据商品id获取商品的评论数量统计信息
def get_goods_comment(goods_id,headers):
    COMMENTS_PATH='https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}'
    url = COMMENTS_PATH.format(goods_id)
    resp_text = requests.get(url=url, headers=headers).text
    comment_json = json.loads(resp_text)
    # print(comment_json)
    comments_count = comment_json['CommentsCount'][0]
    # 评论总数
    comment_count = comments_count['CommentCount']
    # 默认好评数
    default_good_count = comments_count['DefaultGoodCount']
    # 好评数
    good_count = comments_count['GoodCount']
    # 普通评价数
    general_count = comments_count['GeneralCount']
    # 差评数
    poor_count = comments_count['PoorCount']
    # 追评数
    after_count = comments_count['AfterCount']
    # 好评率
    good_rate = comments_count['GoodRate']

    #print(comment_count,default_good_count,good_count,general_count,poor_count,after_count,good_rate)

    comment_info = dict()
    comment_info['comment_count'] = comment_count
    comment_info['default_good_count'] = default_good_count
    comment_info['good_count'] = good_count
    comment_info['general_count'] = general_count
    comment_info['poor_count'] = poor_count
    comment_info['after_count'] = after_count
    comment_info['good_rate'] = good_rate

    return comment_info



#获得商品价格
def get_price(url):
    temp = url.split('/')[-1]
    sid = temp.split('.')[0]
    price_url = "https://p.3.cn/prices/mgets?skuIds=" + sid
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.100 Safari/537.36 '
    }
    response = requests.get(price_url, headers=headers, timeout=30)
    response.encoding = response.apparent_encoding
    jsons = json.loads(response.text[0:-1])
    price = jsons[0]['p']
    if price == "-1.00":
        return "商品已售完"
    else:
        return price




if __name__ == '__main__':
    JDSpiderPage()

