# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     easydb
   Description :
   Author :       ming
   date：          2018/12/24
-------------------------------------------------
   Change Activity:
                   2018/12/24:
-------------------------------------------------
"""
import pymysql


class OpenDB(object):
    def __init__(self):
        self.connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='citydata',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

if __name__ == '__main__':
    pass