import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common import exceptions as ex

num = 0
while num < 3 :
    driver = webdriver.Chrome()  # 实例化浏览器驱动
    # driver.maximize_window()  # 浏览器最大化
    driver.implicitly_wait(10)  # 隐式等待
    driver.get('https://www.baidu.com/')  # 访问url
    time.sleep(60)
    # 输入
    driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys('123')

    print('顺利完成')
    time.sleep(3)
    driver.quit()
    num += 1