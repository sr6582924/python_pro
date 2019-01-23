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

from bottle import request,run,route

import os

#定义图片路径
import os

images_path = './images'
@route('/images/<filename:re:.*\.*>')
def server_static(filename):
    return bottle.static_file(filename, root=images_path, download=True)

upload_path = './upload'
@route('/uploadfile/<filename:re:.*\.*>')
def uploadfile_static(filename):
    return bottle.static_file(filename, root=upload_path)

@route("/getJson", methods=['GET', 'POST'])
def getJson():
    formid = request.query.id
    pageid = request.query.page or '1'
    print(formid, pageid)
    list = os.listdir('./upload')
    dict = {"data": list, "code":0, "msg":'success'}
    return json.dumps(dict)

@route('/uploadDetail', method='GET')
def upload():
    return '''<form action="/upload" method="post" enctype="multipart/form-data">
                  filename:      <input type="text" name="fileName" />
                  Select a file: <input type="file" name="upload" />
                  <input type="submit" value="Start upload" />
             </form>'''

@route('/upload', method='POST')
def do_upload():
    file_name   = request.forms.get('fileName')
    print(file_name)
    upload     = request.files.get('upload')
    if upload:
        name, ext = os.path.splitext(upload.filename)
        print(name, ext)
        save_path = 'upload/'+ file_name
        print(save_path)
        upload.save(save_path) # appends upload.filename automatically
        return 'OK'
    else:
        return '请选择文件'

run(host='0.0.0.0', port=9999)
