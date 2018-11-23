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




def call_pages(url):
    driver = webdriver.Chrome()
    driver.set_window_size(38, 12)  # 设置窗口大小
    driver.get(url)
    # time.sleep(1)
    html = driver.page_source
    return html
    # driver = webdriver.Chrome()
    # driver.set_window_size(38, 12)  # 设置窗口大小
    # driver.get(url)
    # # time.sleep(1)
    # html = driver.page_source
    # return html

<a href="http://www.sge.com.cn/upload/file/201704/11/n3be3mHdoesFI0uO.pdf'

def parse_pages(html):
    patt = re.compile('<a href="(.*?)" class="title fs14 clear" target="_blank">',re.S)
    items = re.findall(patt,html)
    for item in items:
        patt1 = re.compile('<a href="(.*?).pdf'',re.S)
    # for item in items:
    #     return item
    # link_list = []
    # selector = etree.HTML(html)
    # title = selector.xpath('//*[@id="coursecontent"]/div[1]/ul//div[2]/a/text()')
    # # patt = re.compile('onclick="javascript:window.open'+'.*?http://(.*?).pdf',re.S)
    # # items = re.findall(patt,html)
    # links = selector.xpath('//*[@id="coursecontent"]/div[1]/ul//div[1]/a/@href')
    # for item in links:
    #     links_f = 'http://www.sge.com.cn' + item
    #     link_list.append(links_f)

    # for item in items:
    #     full_link = 'http://' + item + '.pdf'
    #     link_list.append(full_link)
    # for i1,i2 in zip(title,link_list):
    #
    #     response = requests.get(i2)
    #     if response.status_code == 200:
    #         with open("/home/karson/SH_Gold_Ex_Spider/%s .pdf" % i1[:-4],"wb") as f:
    #             f.write(response.content)
    #             f.close()
    #     else:
    #         pass

# if __name__ == '__main__':
#     connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='SS_G_E',
#                                  charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#     cursor = connection.cursor()
#     for num in range(1,100):
#         sql = 'select link from down_links where id = %s'% num
#         cursor.fetchone(sql)
#         data = cursor.fetchall()
#




url = 'http://www.sge.com.cn/guize/rule/5141368'
html = call_pages(url)
content = parse_pages(html)
print(content)


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



