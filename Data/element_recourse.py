# -*- coding:UTF-8 -*-

from selenium.webdriver.common.by import By


class ElementRecourse:

    # 底部导航栏
    homepage = (By.ID, 'ch999.app.UI:id/ll_tab_1')
    classify = (By.ID, 'ch999.app.UI:id/ll_tab_2')
    personal = (By.ID, 'ch999.app.UI:id/ll_tab_5')
    # 个人中心
    loginpage = (By.ID, 'ch999.app.UI:id/tv_user_name')
    setting = (By.ID,'ch999.app.UI:id/tv_user_name')
    # 登录页面
    username = (By.ID,'ch999.app.UI:id/et_username')   # 用户名
    password = (By.ID,'ch999.app.UI:id/et_password')   # 密码
    login = (By.ID,'ch999.app.UI:id/btn_user_login')

    # 首页
    home_page_search = (By.ID,'ch999.app.UI:id/tv_search')  # 首页搜索框
    home_bar_xianshigou = (By.XPATH, "//android.widget.TextView[contains(@text,'限时购')]") #

    # 搜索
    search_text = (By.ID,'ch999.app.UI:id/center_search_edit')  # 输入搜索内容的搜索框
    search_result_product_name = (By.ID, 'ch999.app.UI:id/product_name')#搜索结果的商品名称
    search_result_pic = (By.ID,'ch999.app.UI:id/product_image')  # 搜索结果的商品图标
    search_input_tip = (By.ID,'ch999.app.UI:id/content')  # 根据输入内容智能提示出来的商品
    search_result_back = (By.ID,'ch999.app.UI:id/back')  # 搜索结果列表页返回按钮
    search_back = (By.ID, 'ch999.app.UI:id/back')  # 搜索页返回

    # 分类
    product_pic = (By.ID,'ch999.app.UI:id/pic')  # 分类上的图标

    # 商品详情页
    buy_now = (By.ID,'ch999.app.UI:id/buy_now') # 立即购买

    # 参数详情页
    buy = (By.ID,'ch999.app.UI:id/deal') # 规格里的立即购买

    # 确认订单
    confirm_order = (By.ID, 'ch999.app.UI:id/confirm_order_bottom_buy')  # 确认订单

    # 订单提交成功页
    order_success_tip = (By.ID, 'ch999.app.UI:id/tv_text')   # 提交订单成功后 页面上的获得积分提示的文字
    order_center = (By.ID,'ch999.app.UI:id/close')  # 订单中心按钮

    # 抢购
    qiang_gou_product_list = (By.ID, 'ch999.app.UI:id/tv_title') # 抢购商品的名称
    qiang_gou_btn = (By.ID, 'qiangBtn') # 抢购按钮





    # 输入的参数：
    username_value = '19'  # 用户名
    password_value = 'qweasd'  # 密码





