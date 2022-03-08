#coding=utf-8
import ddt
import unittest

@ddt.ddt
class DataTest(unittest.TestCase):
    

    def setUp(self):
        print("这是个setUp")

    def tearDown(self):
        print("这是个tearDown")

    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )
    # unpack 代表将元素一组【1，2】分解，传入2个参数a,b,否则就都传入a
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)
    

if __name__ == '__main__':
    unittest.main()
    
