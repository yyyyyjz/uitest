import datetime
import time

from selenium.webdriver.common.keys import Keys

from Overall import img, fileim


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 定位一个元素
    def find_el(self, feature):
        return self.driver.find_element(*feature)

    # 定位多个元素
    def find_els(self, feature):
        return self.driver.find_elements(*feature)

    # 定位一个元素，输入内容
    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)

    # 定位一个元素，输入内容，并回车
    def input_enter(self, feature, content):
        return self.find_el(feature).send_keys(content, Keys.ENTER)

    # 定位一个元素，并点击
    def click(self, feature):
        return self.find_el(feature).click()

    # 定位一个元素，并获取文本信息
    def get_res_msg(self, feature):
        return self.find_el(feature).text

    # 截图
    def screenshot(self, joint):

        return self.driver.get_screenshot_as_file(img + joint+ fileim)

    def refresh(self):
        """
        刷新页面
        """
        return self.driver.refresh()

