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
    url = 'http://www.sge.com.cn/cpfw/jypzlb'
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
    unit = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[1]/div[1]/p/span/text()')
    trade_style = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[1]/div[2]/ul/li[1]/p[1]/span/text()')
    settle_style = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[1]/div[2]/ul/li[2]/p[1]/span/text()')
    time = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[2]/ul//div[1]/div[3]/text()[2]')
    time_f = []
    for i in time:
        i = i.strip()  # strip去除空格
        time_f.append(i)

    for i1,i2,i3,i4,i5 in zip(title_f,unit,trade_style,settle_style,time_f):
        big_list.append((i1,i2,i3,i4,i5))

    return title_f





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SS_G_E',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into s4 (title,unit,trade_style,settle_style,time) values (%s,%s,%s,%s,%s)', content)
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


# create table s4 (
# id int not null primary key auto_increment,
# title varchar(10),
# unit varchar(10),
# trade_style varchar(10),
# settle_style varchar(10),
# time varchar(30)
# ) engine =InnoDB charset=utf8;

# drop table s4;