

import pytest

from base.read_base import read
from data.msg_data import *
from judge.judge_BasePage import Judge_Base_Page
from judge.judge_statistical_file import J_Statistical_File
from page.bingli_login_page import *
from until.until_webdrivers import *


class Test_bingli_login:

    def setup(self):
        J_Statistical_File()
        self.driver = Getdriver.getdriver()
        self.bingli_page = BingliLoginPage(self.driver)
        self.driver.get(dict1["url"])
        self.driver.implicitly_wait(10)
        # self.jbp = Judge_Base_Page(self.driver)
        Getdriver.Url = True

    def teardown(self):
        Getdriver.time_sleep(3)
        Getdriver.quit_driver()

    @pytest.mark.parametrize("data", read("data_json"))
    def test_bingl_login(self, data):
        #
        # judgment = self.jbp.Judger_is_element_exist
        #

        # 1.输入账号
        start = time.time()
        self.bingli_page.input_send_username(data["username"])

        # 2.输入密码
        self.bingli_page.input_send_password(data["password"])
        logging.info("输入emr病历系统账号:【{}】，输入密码【{}】".format(data["username"], data["password"]))
        # logging.info("okok，睿智抽爆胡桃")

        # 点击登录

        self.bingli_page.click_login()
        end = time.time()
        print("{}".format(end - start))

        # 3.点击病历管理
        start = time.time()
        self.bingli_page.click_bingli()
        end = time.time()
        Getdriver.time_sleep(1)

        # 4.关闭添加患者弹窗
        self.bingli_page.icon_close()
        # 5.输入搜索姓
        self.bingli_page.lastname_send(data["lastname"])
        # 6.点击搜索按钮

        self.bingli_page.find_lastname()
        # 7.点击选择患者名字
        self.bingli_page.name_click()
        # 8.点击选择选中患者

        self.bingli_page.name_choise()
        # 9.点击保存查看患者信息

        # 点击添加处方
        self.bingli_page.prescription_button_click()
        # 10.输入诊断信息
        self.bingli_page.diagnosis_content_send(data["diagnosis"])
        # 11.选择处方有效时间
        self.bingli_page.date_click()
        # 12.点击药物名称输入框
        self.bingli_page.click_drug_name()
        # 13.输入药物名称
        self.bingli_page.drup_name_send(data["drup_name"])
        # Getdriver.time_sleep(60)
        # 14.点击选择药物
        self.bingli_page.choise_drug()
        # 15.等待药物规格加载
        Getdriver.time_sleep(3)
        # 16.输入发药总量
        self.bingli_page.input_drup_number(data["drup_num"])
        Getdriver.time_sleep(3)
        # 点击选择用法
        self.bingli_page.choise_use()
        Getdriver.time_sleep(3)
        # Getdriver.time_sleep(30)
        # 17.用法选择口服
        self.bingli_page.mouth_eat_click()
        # Getdriver.time_sleep(30)
        # 18.添加药物
        self.bingli_page.add_drug()
        # Getdriver.time_sleep(30)
        # 19.点击保存处方
        self.bingli_page.preservation_prescription_click()
        # 20.点击处方发送至患者
        self.bingli_page.send_out_click()
        Getdriver.time_sleep(3)
        self.bingli_page.submit_click()
        Getdriver.time_sleep(3)

        # 断言失败截图
        # prompt = self.bingli_page.get_msg()
        # try:
        #     assert prompt == "操作成功"
        #     logging.info("测试通过")
        # except(AssertionError):
        #     self.bingli_page.assert_error_screenshot()

        # logging.info("okok，睿智抽爆胡桃")

        # 治位计算每个功能的响应时间没用的方法
        # Getdriver.page.append(
        #     self.driver.execute_script("return performance.timing.responseStart") - self.driver.execute_script(
        #         "return performance.timing.requestStart"))
        # print("建立处方的时间为{}".format(Getdriver.page[0]))


