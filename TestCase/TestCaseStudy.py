# -*-coding: utf-8 -*-

import unittest


# 关于setup  和setUpClass的学习

class Test(unittest.TestCase):
    # def setUp(self):
    #     print "执行setup"
    #
    # def tearDown(self):
    #     print "执行teardown"

    def test02(self):
        print "test  case 02"

    def test01(self):
        print "test case 01"

    @classmethod
    def setUpClass(cls):
        print "据说只执行一次启动"

    @classmethod
    def tearDownClass(cls):
        print "据说只执行一次结束"

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test("test02"))
    suite.addTest(Test("test01"))
    unittest.TextTestRunner().run(suite)
