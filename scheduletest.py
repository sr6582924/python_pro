# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     scheduletest
   Description :
   Author :       ming
   date：          2018/12/25
-------------------------------------------------
   Change Activity:
                   2018/12/25:
-------------------------------------------------
"""

import schedule
import time


def job():
    print("I'm working...")



schedule.every().day.at("10:06").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
