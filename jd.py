import urllib
from urllib import response
import json
import requests
from pandas import DataFrame;
from bs4 import BeautifulSoup
from lxml import etree
import re

#选择页码进行爬取
def JDSpiderPage(url):
    for page in range(1,3):
        fullurl=url+"&page="+str(page*2-1)
        print("正在爬取第 {} 页".format(page))
        load_page(fullurl)

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
        #print(new_url)
        load_link_page(new_url,headers)
        load_link_page_mess(new_url,headers)
        get_price(new_url)

#获取信息 爬取商品标题和商品空调品牌
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
    #空调名称
    #air_name=content.xpath('//div[@class="p-parameter"]/ul[@id="parameter2 p-parameter-list"]/li/@title/text()')
    #累计评价
    #buy_judge=content.xpath('//div[@class="comment-count item fl"]/a/text()')
    #选购指数
    #buy_index=content.xpath('//div[@class="buy-rate item fl hide"]/a/text()')

    #评价数
    buy_num=content.xpath('//div[@class="tab-main small"]/ul/li[1]/a/em')
    print(air_title, brand,buy_num)

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

    for ul in uls:
        lis = ul.find_all("li")
        for i in range(len(lis)):
            f = lis[i].getText()
            print(f)

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
        print(price)


if __name__ == '__main__':
    url='https://search.jd.com/Search?keyword=%E7%A9%BA%E8%B0%83&qrst=1&wq=%E7%A9%BA%E8%B0%83&stock=1'
    JDSpiderPage(url)