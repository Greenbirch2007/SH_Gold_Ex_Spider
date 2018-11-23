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
    url = 'http://www.sge.com.cn/guize?cflag=1&p=1'
    driver.set_window_size(38, 12)  # 设置窗口大小
    driver.get(url)
    # time.sleep(1)
    html = driver.page_source
    return html

# http://www.sge.com.cn/tzzjy/kjxqinfo/792259664960901120
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

def download_pdf():

    cursor.execute('select title,link from down_links')



    # for i1,i2 in zip(title,link_list):
    #
    #     response = requests.get(i2)
    #     if response.status_code == 200:
    #         with open("/home/karson/SH_Gold_Ex_Spider/%s .pdf" % i1[:-4],"wb") as f:
    #             f.write(response.content)
    #             f.close()
    #     else:
    #         pass


if __name__ == '__main__':
    html = call_pages()
    content = parse_pages(html)
    insertDB(content)




# create table down_links (
# id int not null primary key auto_increment,
# title varchar(100),
# link varchar(150)
# ) engine =InnoDB charset=utf8;










