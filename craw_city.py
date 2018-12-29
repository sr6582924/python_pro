# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     craw_city
   Description :
   Author :       ming
   date：          2018/12/24
-------------------------------------------------
   Change Activity:
                   2018/12/24:
-------------------------------------------------
"""

import requests as req
from lxml import etree
from easydb import OpenDB
import uuid


from requests import HTTPError

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8;',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Host':'xingzhengquhua.51240.com',
    'Proxy-Connection':'keep-alive',
    'Referer':'https://xingzhengquhua.51240.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

host = 'https://xingzhengquhua.51240.com'

def parse_html(url, parent=''):
    print(url)
    rep = req.get(url, headers=headers)
    selector = etree.HTML(rep.text)
    region_list = selector.xpath('//tr')
    for i in range(3, len(region_list)):
        ii = region_list[i]
        print(ii)
        text = ii.xpath("td/a/text()")
        href = ii.xpath("td/a/@href")
        print("text:" + str(text))
        print("href:" + str(href))
        if href:
            insertRegion(regionName=text[0], regionCode=text[1], parentCode=parent)
            parse_html(host+href[0], text[1])

def insertRegion(**kwargs):
    with OpenDB() as db:
        id = str(uuid.uuid1())
        regionName = kwargs['regionName']
        regionCode = kwargs['regionCode']
        parentCode = kwargs['parentCode']
        sql = "insert into regiondata(id, regionName, regionCode, parentCode)values('%s','%s','%s','%s');"%(id, regionName, regionCode, parentCode)
        print(sql)
        db.execute(sql)

if __name__ == '__main__':
    parse_html(host)