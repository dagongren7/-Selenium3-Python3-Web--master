#coding=utf-8
from selenium import webdriver
from PIL import Image
import random
import base64
import json
import requests
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("http://sgs.pocyun.com:48003/#/") #打开页面
    driver.maximize_window() #窗口最大化
    driver.refresh()
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
    return user_info

#获取验证码图片
def get_code_image(file_name):
    '''
    思想：先保存整个网页，然后从中裁剪出验证码图片
    '''
    driver.save_screenshot(file_name) #保存整个页面为图片格式
    code_element = driver.find_element_by_id("s-canvas") #定位到验证码图片
    left = code_element.location['x'] + 5
    top = code_element.location['y'] - 3
    right = code_element.size['width']+left + 5
    height = code_element.size['height']+top + 5

    im = Image.open(file_name) #使用pillow中的Image方法打开之前保存的图片
    img = im.crop((left,top,right,height)) #使用crop方法进行裁剪，取出图片中的验证码图片
    img.save(file_name) #保存裁剪出的验证码图片

#解析图片获取验证码
def code_online(file_name):
    result = base64_api(uname='dagongren', pwd='chen184550', img=file_name, typeid=3)
    print(result)
    return result

def base64_api(uname, pwd, img, typeid):
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

#运行主程序
def run_main():
    # user_name_info = get_range_user()
    # user_email = user_name_info + '@126.com'
    file_name = r"C:\Users\admin\Pictures\test01.png"
    driver_init()
    driver.find_element_by_name("userName").send_keys('ckladmin')
    get_element("password").send_keys('123456')
    get_code_image(file_name)
    text = code_online(file_name)
    driver.find_element_by_name("vailDateCode").send_keys(text)
    driver.find_element_by_class_name("login_button").click()
    text = driver.find_element_by_class_name('error').text
    print('验证码错误',text)
    if len(text) == 0:
        print('重试')
    else:
        time.sleep(5)
        ActionChains(driver).send_keys(Keys.ENTER).perform()
    # driver.close() #关闭driver，一定要有，否则电脑速度会越来越慢

run_main()
