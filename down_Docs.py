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
from requests.exceptions import RequestException




def call_pages_link(url):
    try:
        driver = webdriver.Chrome()
        driver.set_window_size(38, 12)  # 设置窗口大小
        driver.get(url)
        html = driver.page_source
        return html
        driver.quit()
    except Exception :
        pass

# def call_pages_pdf(url):
#
#     response = requests.get(url)
#     return response.text

  

# 正则解析不理想啊
def parse_pages(html):
    selector = etree.HTML(html)
    TL = selector.xpath('/html/body/div[6]/div/div[2]/div[2]/div[3]/ul/li/a/@href')# 这个解析表达式有多少，就可以解析多少
    return TL



if __name__ == '__main__':
    i_num = 0

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SS_G_E',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    for num in range(1,100):
        sql ='select title,link from down_links where id = %s'% num
        # #执行sql语句
        cursor.execute(sql)
        # #获取所有记录列表
        data = cursor.fetchone()

        url = data['link']
        TI = data['title']
        html = call_pages_link(url)
        content = parse_pages(html)
        for item in content:
            response = requests.get(item)
            if response.status_code == 200:
                with open("/home/karson/SH_Gold_Ex_Spider/%s .pdf" % TI,"wb") as f:
                    f.write(response.content)
                    f.close()

        i_num += 1
        print(i_num)












#批量创建文件夹
# import os
# themes = ['PAu99.99', 'PAu99.95', 'iPAu9999', 'iPAu99.5', 'iPAu100g', 'LAu9999 ', 'LAu9995', 'iLAu9999 ', 'iLAu995 ', 'iLAu100g ', 'OAu99.99 ', 'OAu99.95 ']
# base = "/home/karson/SH_Gold_Ex_Spider/询价/"
# for i in themes:
#     file_name = base + str(i)
#     os.mkdir(file_name)
#
#
#



