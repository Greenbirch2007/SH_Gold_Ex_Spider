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




def call_pages(url):
    driver = webdriver.Chrome()
    driver.set_window_size(38, 12)  # 设置窗口大小
    driver.get(url)
    # time.sleep(1)
    html = driver.page_source
    driver.close()
    return html

def parse_pages(html):
    big_list = []
    link_list = []
    selector = etree.HTML(html)
    title = selector.xpath('/html/body/div[6]/div/div/div[2]/div[2]/ul//a/span[1]/text()')

    links = selector.xpath('/html/body/div[6]/div/div/div[2]/div[2]/ul//a/@href')
    for item in links:
        links_f = 'http://www.sge.com.cn' + item
        link_list.append(links_f)

    for i1,i2 in zip(title,link_list):
        big_list.append((i1,i2))

    return big_list



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SS_G_E',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into down_links (title,link) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except Exception :
        print('出列啦')





if __name__ == '__main__':
    links = ['http://www.sge.com.cn/guize?cflag=1&p=1', 'http://www.sge.com.cn/guize?cflag=1&p=2',
             'http://www.sge.com.cn/guize/ywgz?cflag=1&p=1', 'http://www.sge.com.cn/guize/ywgz?cflag=1&p=2',
             'http://www.sge.com.cn/guize/ywgz?cflag=1&p=3', 'http://www.sge.com.cn/guize/ywgz?cflag=1&p=4',
             'http://www.sge.com.cn/guize/ywgz?cflag=1&p=5', 'http://www.sge.com.cn/guize/ywgz?cflag=1&p=6',
             'http://www.sge.com.cn/guize/ywgz?cflag=1&p=7', 'http://www.sge.com.cn/guize/gjzxywgz',
             'http://www.sge.com.cn/guize/jj', 'http://www.sge.com.cn/guize/xhjqhy',
             'http://www.sge.com.cn/guize/xhyqhy', 'http://www.sge.com.cn/guize/rljysxj',
             'http://www.sge.com.cn/guize/rlyhjxj', 'http://www.sge.com.cn/guize/rlgjsgl',
             'http://www.sge.com.cn/guize/qs', 'http://www.sge.com.cn/guize/jg', 'http://www.sge.com.cn/guize/dj',
             'http://www.sge.com.cn/guize/fxqbg']

    for url in links:
        html = call_pages(url)
        content = parse_pages(html)
        insertDB(content)




# create table down_links (
# id int not null primary key auto_increment,
# title varchar(100),
# link varchar(150)
# ) engine =InnoDB charset=utf8;
# #
# drop table down_links;
#
#
# drop table down_links;
# select count(*) from down_links;
#





