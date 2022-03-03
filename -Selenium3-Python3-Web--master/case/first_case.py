#coding=utf-8
import sys
sys.path.append(r"F:\dailyCode\pythonCode\-Selenium3-Python3-Web--master\-Selenium3-Python3-Web--master") #将工程路径加入到Python的搜索路径中
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import unittest
import HTMLTestRunner
import os
import time

'''
验证码识别网址
http://www.ttshitu.com/price.html?spm=null
'''
class FirstCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = r"C:\Users\ASUS\Pictures\test02.png"
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.5itest.cn/register")
        cls.driver.maximize_window()  

    def setUp(self):
        self.driver.refresh()
        self.logger.info("this is Chrome")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName #获取case的名字，用于后续的截图
                screenshot_name = case_name+'.png' #截图图片的名字
                dir_path = os.path.dirname(os.getcwd()) #获取上一级目录，即工程目录  
                file_path = os.path.join(dir_path,'report',screenshot_name) #截图保存路径
                self.driver.save_screenshot(file_path)
    
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        # cls.driver.close()


    def test_login_email_error(self):
        email_error = self.login.login_email_error('27','user221','111111',self.file_name)
        self.assertIs(email_error,True)
    
    def test_login_username_error(self):
        username_error = self.login.login_name_error('1234@126.com','1','111111',self.file_name)
        self.assertIs(username_error,True)
        # if username_error == True:
        #     print("注册成功了，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error('12345@126.com','11','11',self.file_name)
        # self.assertIs(password_error,True)
        if password_error == False:
            print("注册成功了，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error('34dsdf@qq.com','user111','111111',self.file_name)
        print('code_error----------------',code_error)
        # self.assertIs(code_error,True)
        if code_error == False:
            print("验证码执行失败")
            # return self.test_login_code_error()

    def test_login_success(self):
        success = self.login.register_succes("777@qq.com","ss779","111111",self.file_name)
        # self.assertIs(success,True)
        if self.login.register_succes("777@qq.com","ss779","111111",self.file_name) == False:
            print('重新输入')
            return self.test_login_success()

if __name__ == '__main__':
    # unittest.main()   
    dir_path = os.path.dirname(os.getcwd()) #获取上一级目录，即工程目录  
    print(dir_path)
    file_path = os.path.join(dir_path,'report','first_case.html') #获取report文件夹下first_case.html目录路径
    print(file_path)
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_email_error'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is firstcase report",description=u"这个是第一次测试报告",verbosity=2)
    runner.run(suite)


