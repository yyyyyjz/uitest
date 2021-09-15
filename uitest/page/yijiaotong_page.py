from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class YijiaotongPage(BaseAction):
    click_login_bot = By.XPATH, "//*[@id='app']/div/div[1]/div/div[1]/div/img"
    send_username = By.XPATH, "//*[@id='app']/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div[1]/input"
    send_password = By.XPATH, "//*[@id='app']/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/input"
    click_login = By.XPATH, "//*[@id='app']/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div[3]"
    get_text = By.XPATH,"//*[text()='操作成功']"

    # 1.点击登录，跳转到登录界面
    def click_bot(self):
        return self.click(self.click_login_bot)

    # 2.输入账号
    def input_username(self, username):
        return self.input(self.send_username, username)

    # 3.输入密码
    def input_password(self, password):
        return self.input(self.send_password, password)

    # 4.点击登录按钮
    def login_click(self):
        return self.click(self.click_login)

    # 5.获取断言信息
    def get_msg(self):
        return self.get_res_msg(self.get_text)



