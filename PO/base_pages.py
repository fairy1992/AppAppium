# coding= utf-8
__author__='fairy'
from selenium.webdriver.support.ui import WebDriverWait
import pytesseract
from PIL import Image


class Base:

    def __init__(self,se_driver):
        """
                            初始化driver
        """

        self.driver = se_driver

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except AttributeError:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)

    def find_elements(self, loc):
        try:
            WebDriverWait(self.driver, 20).until(lambda driver: driver.find_elements(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except AttributeError:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)

    # 重新封装输入方法
    def send_keys(self, loc, value):
        try:
            # if click_first:
            #     self.find_element(loc).click()
            # if clear_first:
            self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print "%s 页面未能找到 %s 元素" % (self, loc)

    # 重新封装按钮点击方法
    def click_button(self,*loc):
        try:
            # if find_first:
            #     self.find_element(loc)
            self.find_element(*loc).click()
        except AttributeError:
            print "%s 页面未能找到 %s 按钮" % (self, loc)

    # def isdispaly(self,*loc):
    #     try:
    #         WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element(*loc).is_displayed())
    #     except AttributeError:
    #         print u"%s 页面中未能找到 %s 元素" % (self, loc)
