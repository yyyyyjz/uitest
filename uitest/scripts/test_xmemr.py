import time

from until.until_webdrivers import Getdriver


class Test_asthmaControl:
    def setup(self):
        self.driver = Getdriver.getdriver()
        self.driver.get("http://103.90.155.19:33309/")
        self.driver.implicitly_wait(10)
        # self.jbp = Judge_Base_Page(self.driver)
        Getdriver.Url = True

    def teardown(self):
        Getdriver.time_sleep(3)
        Getdriver.quit_driver()

    def test_login(self):
        self.driver.find_element_by_class_name("el-input__inner").send_keys("xiaoman001")
        self.driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/div/input").send_keys("654321")
        self.driver.find_element_by_xpath("//*[@id='app']/div/form/button").click()
        self.driver.find_element_by_class_name("is-hover-shadow").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[1]/div[4]/div[1]/div/input").send_keys("颜家智009")
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[1]/div[3]/button[2]/span").click()
        # time.sleep(30)
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div/button[1]/span").click()