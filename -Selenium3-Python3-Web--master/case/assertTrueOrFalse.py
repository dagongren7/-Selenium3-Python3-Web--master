from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest

class BlogHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        url = "https://www.cnblogs.com/EncoreLiu/"
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_01(self):
        '''
        比较元素内容是否相等
        :return:
        assertFalse  返回结果为 False
        '''
        locator = ("id","blog_nav_sitehome")
        text = "博客1园"
        result = EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertIs(result,True)

    def test_02(self):
        '''
        比较元素内容是否相等
        :return:
        assertTrue  结果为true
        '''
        locator = ("id","blog_nav_myhome")
        text = "首页"
        result = EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()