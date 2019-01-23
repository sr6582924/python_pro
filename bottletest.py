# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bottletest
   Description :
   Author :       ming
   date：          2019/1/23
-------------------------------------------------
   Change Activity:
                   2019/1/23:
-------------------------------------------------
"""

import bottle
import json

#定义图片路径
images_path = './images'
@bottle.route('/images/<filename:re:.*\.*>')
def server_static(filename):
    return bottle.static_file(filename, root=images_path, download=True)

@bottle.route("/getJson", methods=['GET', 'POST'])
def getJson():
    formid = bottle.request.query.id
    pageid = bottle.request.query.page or '1'
    print(formid, pageid)
    list = ['fdsfds', 'fdsfdsfds']
    dict = {"response": list}
    return json.dumps(dict)

bottle.run(host='0.0.0.0', port=9999)
