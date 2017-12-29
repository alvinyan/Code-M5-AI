# -*- coding: utf-8 -*-
'''
    face_detction.py
    ~~~~~~~~~
    
    演示调用百度AipFace第三方实现人脸特征数据监测案例.

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

# 调用函数获取图像二进制数据
face_image = get_file_content('image/photo03.jpg')
# 设置关键参数选项
options = {}
options["max_face_num"] = 1  # 最多处理人脸数目，默认值1
options["face_fields"] = "age,gender"  # 年龄,性别

# 带参数调用人脸检测
result = client.detect(face_image, options)

# 输出检测结果
print('~~~~ 返回结果类型 ~~~~')
print(type(result))
print('~~~~ 返回结果数据 ~~~~')
print(result)
print('~~~~ 输出检测结果 ~~~~')
age = int(result['result'][0]['age'])
# 年龄
print('检测年龄:', age)
# 性别
gender = result['result'][0]['gender']
if gender == 'male':
    gender = '男'
else:
    gender = '女'
print('检测性别:', gender)
