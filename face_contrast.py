# -*- coding: utf-8 -*-
'''
    face_contrast.py
    ~~~~~~~~~
    
    演示调用百度AipFace第三方实现人脸对比案例.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入AipFace模块库
from aip import AipFace

# 配置项目的 APP_ID, API_KEY（AK）, SECRET_KEY（SK）
# 通过百度AI控制台创建项目后查看得到
APP_ID = '10594384'
API_KEY = 'AgpRImqLmuYC9yDrEc2wzTLR'
SECRET_KEY = 'eEdoMPVReij1nUbgVhRSfR5Y8Ilflv2u'

# 创建client客户端对象
# 语法：AipFace(APP_ID, API_KEY, SECRET_KEY)
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 定义读取人像图片函数
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义图片列表，存放两张对比图片
images = [
    get_file_content('image/photo05.jpg'),
    get_file_content('image/photo06.jpg'),
]

# 调用人脸比对
client.match(images)

# 设置可选参数
options = {}
options["ext_fields"] = "qualities"
options["image_liveness"] = ",faceliveness"
options["types"] = "7,13"

# 带参数调用人脸对比
result = client.match(images, options)

# 输出相似度
similarity_rate = result['result'][0]['score']
print('相似度得分：%.2f' % similarity_rate)