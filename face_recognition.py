# -*- coding: utf-8 -*-
'''
    helloflask.py
    ~~~~~~~~~
    
    演示快速创建Flask应用项目.

    :copyright: (c) 2017 by Chinasoft International·ETC.    
    :license: BSD, see LICENSE for more details.
    :author: CTO Officer (YanHe)
    :email: yanhe@chinasofti.com
'''

# 导入所需模块库及对象
from flask import Flask
from flask import render_template,request
import os,base64, json
# 导入AipFace模块库
from aip import AipFace

# 创建Flask类实例app
app = Flask(__name__)
# 设置当前运行模式为调试模式
app.config['DEBUG'] = True

# 配置项目的 APP_ID, API_KEY（AK）, SECRET_KEY（SK）
# 通过百度AI控制台创建项目后查看得到
APP_ID = '10594384'
API_KEY = 'AgpRImqLmuYC9yDrEc2wzTLR'
SECRET_KEY = 'eEdoMPVReij1nUbgVhRSfR5Y8Ilflv2u'

# 创建client客户端对象
# 语法：AipFace(APP_ID, API_KEY, SECRET_KEY)
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 通过装饰器设置函数URLs访问路径
@app.route('/')
# 定义设置网站首页的处理函数
def gotoIndex():
    # 浏览器输出
    return render_template('face_recognition.html')

'''
 接受客户端传入人脸数据并进行鉴定识别
'''
@app.route('/commitImageData',methods=['POST'])
def commitImageData():
    if request.method == 'POST':
        # 将获取的data数据转化成Json数据格式
        json_data = json.loads(request.form.get('data'))
        # 获取key：data的数据（即图片base64编码）
        img_base64 = json_data['data']
        # base64转码
        imgdata=base64.b64decode(img_base64)
        # 创建临时图片文件，以写入二进制形式打开
        file=open('temp/face_tmp.png','wb')
        # 将base64编码写入
        file.write(imgdata)
        # 关闭文件操作对象  
        file.close()
        # 调用人脸特征检测函数
        result = face_detection('temp/face_tmp.png')
        print(json.dumps(result))     
        return json.dumps(result)

'''
 定义读取人像图片函数
'''
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

'''
 实现人脸特征检测
'''
def face_detection(face_img_path):
    # 调用函数获取图像二进制数据
    face_image = get_file_content(face_img_path)
    # 设置关键参数选项
    options = {}
    options["max_face_num"] = 1  # 最多处理人脸数目，默认值1
    options["face_fields"] = "age,gender,expression,glasses,beauty"  # 年龄,性别

    # 带参数调用人脸检测
    result = client.detect(face_image, options)

    # ~~ 测试结果 ~~
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
    # ~~ 测试结束 ~~
    # 返回数据
    return result['result'][0]



# 设置main入口
if __name__ == '__main__':    
    app.run() # 启动应用
