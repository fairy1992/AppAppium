# # -*- coding:UTF-8 -*-
#
# import unittest
# from PO.home_search import HomeSearch
# from PO.login_page import Login
# from selenium import webdriver
# from Data.driver_desired_caps import *
#
# # 合并多个case为一个  连续的操作
#
#
# class TestCaseLoginSearch(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print '执行搜索setup'
#         cls.driver = Driver_Desired_Caps.driver
#
#     def test_b_home_page_search(self):
#         print '执行搜索test case'
#         homeSearch = HomeSearch(self.driver)
#         homeSearch.click_home_page()
#         homeSearch.click_home_page_search()
#         homeSearch.input_search_content()
#         homeSearch.click_search_tip()
#         homeSearch.search_success_judge()
#
#     def test_a_login(self):
#         print '执行登录test case'
#
#         login = Login(self.driver)
#         login.click_personal_icon()
#         login.click_login_page()
#         login.send_username()
#         login.send_password()
#         login.click_login_button()
#         login.find_setting()
#
#     @classmethod
#     def tearDownClass(cls):
#         print "'执行搜索teardown'"
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()
