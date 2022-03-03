# coding=utf-8
from PIL import Image
import time
import base64
import json
import requests


# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别

class GetCode(object):
    def __init__(self, driver):
        self.driver = driver

    # 获取验证码图片
    def get_code_image(self, file_name,code):
        # code = 1, 华为云验证码定位
        if code == '1':
            driver.save_screenshot(file_name)  # 保存整个页面为图片格式
            code_element = driver.find_element_by_id("s-canvas")  # 定位到验证码图片
            left = code_element.location['x'] + 5
            top = code_element.location['y'] - 3
            right = code_element.size['width'] + left + 5
            height = code_element.size['height'] + top + 5

            im = Image.open(file_name)  # 使用pillow中的Image方法打开之前保存的图片
            img = im.crop((left, top, right, height))  # 使用crop方法进行裁剪，取出图片中的验证码图片
            img.save(file_name)  # 保存裁剪出的验证码图片

            '''
            code == 0,测试网址定位
            '''
        if code == '0':
            self.driver.save_screenshot(file_name)  # 保存整个页面为图片格式
            code_element = self.driver.find_element_by_id("getcode_num")  # 定位到验证码图片
            left = code_element.location['x'] + 170
            top = code_element.location['y'] + 110
            right = code_element.size['width'] + left + 55
            height = code_element.size['height'] + top + 70

            im = Image.open(file_name)  # 使用pillow中的Image方法打开之前保存的图片
            img = im.crop((left, top, right, height))  # 使用crop方法进行裁剪，取出图片中的验证码图片
            img.save(file_name)  # 保存裁剪出的验证码图片
            time.sleep(1)  # 加上时间延迟，使得在解析之前能够有足够的时间保存图片

    def base64_api(self,uname, pwd, img, typeid):
        with open(img, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            b64 = base64_data.decode()
        data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        return ""

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name,'0')
        result = self.base64_api(uname='dagongren', pwd='chen184550', img=file_name, typeid=3)
        return result
