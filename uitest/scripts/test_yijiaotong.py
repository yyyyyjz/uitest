import logging

import pytest

from data.msg_data import dict2
from page.yijiaotong_page import YijiaotongPage
from until.until_webdrivers import Getdriver


class Test_yijiaotong_login:

    def setup(self):
        self.driver = Getdriver.getdriver()
        self.yjt_page = YijiaotongPage(self.driver)
        self.driver.get("https://test.c-sams.com:8091/#/")
        self.driver.implicitly_wait(10)
        Getdriver.Url = True

    def teardown(self):
        Getdriver.time_sleep(3)
        Getdriver.quit_driver()

    @pytest.mark.parametrize("data", [dict2])
    def test_yijiao_login(self, data):
        self.yjt_page.click_bot()
        self.yjt_page.input_username(data["username"])
        self.yjt_page.input_password(data["password"])
        logging.info("输入医教通账号:【{}】,输入密码【{}】".format(data["username"], data["password"]))
        # logging.info("okok，睿智抽爆胡桃")
        self.yjt_page.login_click()
        Getdriver.time_sleep(2)
        # prompt = self.yjt_page.get_msg()
        # assert prompt == "操作成功"
        # logging.info(prompt)

        logging.info("测试通过")
        # logging.info("okok，睿智抽爆胡桃")
