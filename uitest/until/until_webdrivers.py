import logging
import time

from selenium import webdriver


class Getdriver:

    driver = None
    # option = webdriver.ChromeOptions()
    # 谷歌浏览器设置项啊，一些弹窗提示什么的，给他关了
    # def chrome_set(self):
    #     prefs = {}
    #     self.option.add_experimental_option("prefs", prefs)
    #     prefs["credentials_enable_service"] = False
    #     prefs["profile.password_manager_enabled"] = False
    #     self.option.add_experimental_option('useAutomationExtension', False)
    #     self.option.add_experimental_option("excludeSwitches", ['enable-automation'])

    @classmethod
    def getdriver(cls):
        if cls.driver is None:
            # # 打开控制台
            option = webdriver.ChromeOptions()
            # option.add_argument("--auto-open-devtools-for-tabs")
            # option.add_argument("--disable-extensions")

            #防止打印一些无用的日志
            option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            cls.driver = webdriver.Chrome(chrome_options=option)

            # cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            logging.info("测试完成，关闭driver")
            # logging.info("okok，睿智抽爆胡桃")
            cls.driver = None

    @classmethod
    def time_sleep(cls, times):
        time.sleep(times)




