import time

from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions


class GetDriver1:
    driver = None
    URL = False
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            mobile_emulation = {"deviceName": "Moto G4"}
            option = webdriver.ChromeOptions()
            option.add_experimental_option('mobileEmulation', mobile_emulation)
            cls.driver = webdriver.Chrome(chrome_options=option)
            # cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def driver_quit(cls):
        if cls.driver and cls.URL is False:
            cls.driver.quit()
            print("quit")
            cls.driver = None

    @classmethod
    def sleep_sjian(cls, times):
        time.sleep(times)

    # @classmethod
    # def close_switch(cls):
    #     cls.switch = True

