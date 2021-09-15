from datetime import datetime

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
from until.until_webdrivers import Getdriver


class BingliLoginPage(BaseAction):

    username_send = By.CLASS_NAME, "el-input__inner"
    password_send = By.ID, "password"
    login_input = By.CLASS_NAME, "el-button"
    guanli_click = By.CLASS_NAME, "management"
    get_res_text = By.CLASS_NAME, "el-message"
    close_icon = By.XPATH, "/html/body/div[2]/div/div[1]/button/i"
    send_lastname = By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/span[2]/div[1]/input"
    find_name = By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/button/span"
    click_name = By.CLASS_NAME, "identifier"
    choice_name = By.XPATH, "/html/body/div[3]/div/div[3]/div/button[1]/span"
    click_prescription_button = By.XPATH, "/html/body/div/div[1]/div[1]/nav/ul/li[6]/a/div/i[2]"
    send_diagnosis_content = By.CLASS_NAME, "el-textarea__inner"
    click_date = By.CLASS_NAME, "el-input__inner"
    send_drug_name = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[4]/div/div[2]/div[1]/span[1]/div/div/input"
    # click_choise_drug = By.XPATH, "//*[@id='el-autocomplete-873-item-0']/div"
    click_choise_drug = By.CLASS_NAME, "drug-list-item"
    send_drug_num = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[4]/div/div[2]/div[1]/span[4]/div/input"
    click_choise_use = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[4]/div/div[2]/div[2]/span[3]/div/div/input"
    click_mouth_eat = By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    click_add_drug = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[4]/div/div[2]/div[2]/span[4]/button[1]/span"
    # 保存
    click_preservation_prescription = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[5]/div[2]/button[1]/span"
    # 发送给患者
    click_send_out = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[5]/div[2]/button[2]/span"
    click_Submit = By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[7]/div/div/div[3]/span/button[1]"


    # 1.输入账号
    def input_send_username(self, username):
        return self.input(self.username_send, username)

    # 2.输入密码
    def input_send_password(self, password):
        return self.input(self.password_send, password)

    # 3.点击登录
    def click_login(self):
        return self.click(self.login_input)

    # 4.点击打开病历系统
    def click_bingli(self):
        return self.click(self.guanli_click)

    # 5.获取断言信息
    def get_msg(self):
        return self.get_res_msg(self.get_res_text)

    def icon_close(self):
        return self.click(self.close_icon)

    def lastname_send(self, lastname):
        return self.input(self.send_lastname, lastname)

    def find_lastname(self):
        return self.click(self.find_name)

    def name_click(self):
        return self.click(self.click_name)

    def name_choise(self):
        return self.click(self.choice_name)

    def prescription_button_click(self):
        return self.click(self.click_prescription_button)

    def diagnosis_content_send(self, diagnosis):
        return self.input(self.send_diagnosis_content, diagnosis)

    def date_click(self):
        return self.click(self.click_date)

    def click_drug_name(self):
        return self.click(self.send_drug_name)

    def drup_name_send(self, name):
        return self.input(self.send_drug_name, name)

    def choise_drug(self):
        return self.click(self.click_choise_drug)

    def input_drup_number(self, num):
        self.input(self.send_drug_num, num)

    def choise_use(self):
        return self.click(self.click_choise_use)

    def mouth_eat_click(self):
        return self.click(self.click_mouth_eat)

    def add_drug(self):
        return self.click(self.click_add_drug)

    def preservation_prescription_click(self):
        return self.click(self.click_preservation_prescription)

    def send_out_click(self):
        return self.click(self.click_send_out)

    def submit_click(self):
        Getdriver.time_sleep(1)
        self.screenshot("button")
        Getdriver.time_sleep(1)
        return self.click(self.click_Submit)

    def assert_error_screenshot(self):
        return self.screenshot("arrerterror")
