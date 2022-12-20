from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from appium import webdriver
from utils.logger_util import log


class Base(object):
    # 初始化options
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = '8BN0217715005842'
    options.platformVersion = '9'
    options.app_package = 'com.bnqkl.cot'
    options.app_activity = 'com.bnqkl.cot.MainActivity'
    options.no_reset = False
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    log.info("初始化options完成！")

    # driver.implicitly_wait(10)  # 隐式等待

    def locator(self, loc: tuple):
        """
        重写定位方式，添加显示等待定位元素。
        :param loc: 定位器，元组的形式
        :return: element
        """
        try:
            return WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*loc))
        except Exception as e:
            log.error(e)

    def click(self, loc: tuple):
        """
        点击元素
        :param loc: 定位器
        """
        self.locator(loc=loc).click()

    def input(self, loc: tuple, value: str):
        """
        输入文本
        :param loc: 定位器
        :param value: 输入value
        """
        self.locator(loc=loc).send_keys(value)
