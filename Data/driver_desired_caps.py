# -*- coding:UTF-8 -*-

from selenium import webdriver


class DesiredCaps:
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': 'f68ca56',
        'noReset': True,
        'appPackage': 'ch999.app.UI',
        'appActivity': 'ch999.app.UI.View.MainActivity',
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

Driver_Desired_Caps = DesiredCaps()

