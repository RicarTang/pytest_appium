import allure
import basic.base
import os
import pytest
from pages.create_wallet_page import CreateWalletPage
from utils.load_file_util import LoadFile
from utils.logger_util import log


@allure.feature("创建钱包")
class TestCreateWallet(CreateWalletPage):
    """
    创建钱包测试用例层
    """

    def setup(self):
        """
        前置操作，每条测试用例执行之前重置app
        """
        self.driver.reset()

    @allure.story("创建钱包表单测试用例")
    @pytest.mark.parametrize('data',
                             LoadFile(file=os.path.join(os.path.dirname(__file__),
                                                        '../data/test_data/create_wallet.yaml'),
                                      mode='r'))
    def test_create_case(self, data: dict):
        """
        创建钱包成功测试用例
        """
        allure.dynamic.title(data['title'])
        log.info(f"执行测试用例:{data['title']}")
        with allure.step("step1:点击创建钱包按钮"):
            self.create_btn_click()
        with allure.step(f"step2:输入钱包名称:{data['walletName']}"):
            self.wallet_name_input(data["walletName"])
        with allure.step(f"step3:输入钱包密码:{data['walletPassword']}"):
            self.wallet_password_input(data["walletPassword"])
        with allure.step(f"step4:重复输入钱包密码:{data['walletPasswordRepeat']}"):
            self.wallet_password_repeat_input(data["walletPasswordRepeat"])
        with allure.step(f"step5:输入钱包密码提示:{data['walletPasswordHint']}"):
            self.wallet_password_hint_input(data["walletPasswordHint"])
        with allure.step("step6:点击用户协议"):
            self.user_agreement_click()
        with allure.step("step7:点击创建钱包按钮"):
            self.create_wallet_confirm_click()
        with allure.step("step8:断言"):
            pass
