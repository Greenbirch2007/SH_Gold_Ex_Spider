# ! -*- coding:utf-8 -*-

import time
import re
import pymysql
import requests
from selenium import webdriver
# 还是要用PhantomJS
import datetime
import string
from lxml import etree




def call_pages():

    driver = webdriver.Chrome()
    url = 'http://www.sge.com.cn/cpfw/byjq'
    driver.set_window_size(38, 12)  # 设置窗口大小
    driver.get(url)
    # time.sleep(1)
    html = driver.page_source
    return html


def parse_pages(html):
    big_list = []
    selector = etree.HTML(html)
    title = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul/li/div[1]/div[1]/h2/text()')
    title_f = title[:-1]
    means = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[1]/div[2]/ul/li[1]/p[1]/span/text()')
    ratio = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[1]/div[2]/ul/li[2]/p[1]/span/text()')

    patt1 = re.compile('交易时间\u3000上午:9:00 至 11:30，下午:13:30 至 15:30，夜间:19:50 至次日 02:30',re.S)
    _time = re.findall(patt1,html)
    time_f = _time[:1] * len(ratio)  # a[0] 是一个元素 a[:1]是第一个元素组成的列表，　a[:0]是一个空列表
    links = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[2]/a/@href')
    links_list = []
    for item in links:
        ll = "{}{}".format('http://www.sge.com.cn',item) # 尝试使用新的字符串拼接
        links_list.append(ll)
    for i1,i2,i3,i4,i5 in zip(title_f,means,ratio,time_f,links_list):
        big_list.append((i1,i2,i3,i4,i5))
    return title_f




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SS_G_E',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into s2 (title,means,raito,time,link) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except Exception :
        print('出列啦')



if __name__ == '__main__':

    html = call_pages()
    content = parse_pages(html)
    print(content)
    # insertDB(content)


# create table s2 (
# id int not null primary key auto_increment,
# title varchar(10),
# means varchar(10),
# raito varchar(10),
# time varchar(100),
# link varchar(150)
# ) engine =InnoDB charset=utf8;
#
# drop table s1;