from basic import base
from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.by import By
from data.test_ele import create_wallet_ele
from utils.logger_util import log


class CreateWalletPage(base.Base):
    """
    创建钱包page层
    """

    # 定位器
    create_wallet_btn = (AppiumBy.XPATH, create_wallet_ele.create_wallet_btn)  # 创建钱包createWallet
    wallet_name = (AppiumBy.XPATH, create_wallet_ele.wallet_name)  # 钱包名称walletName
    wallet_password = (AppiumBy.XPATH, create_wallet_ele.wallet_password)  # 钱包密码walletPassword
    wallet_password_repeat = (AppiumBy.XPATH, create_wallet_ele.wallet_password_repeat)  # 确认钱包密码walletPasswordRepeat
    wallet_password_hint = (AppiumBy.XPATH, create_wallet_ele.wallet_password_hint)  # 钱包密码提示walletPasswordHint
    user_agreement = (AppiumBy.CLASS_NAME, create_wallet_ele.user_agreement)  # 用户协议walletAgreement
    create_wallet_confirm = (AppiumBy.XPATH, create_wallet_ele.create_wallet_confirm)  # 创建钱包表单确认createWalletConfirm

    def create_btn_click(self):
        """
        点击创建钱包按钮
        """
        self.click(self.create_wallet_btn)
        log.info("点击创建钱包按钮")

    def wallet_name_input(self, value: str):
        """
        输入钱包名称
        :param value: walletName
        """
        self.input(loc=self.wallet_name, value=value)
        log.info(f"输入钱包名称:{value}")

    def wallet_password_input(self, value: str):
        """
        输入钱包密码
        :param value: walletPassword
        """
        self.input(loc=self.wallet_password, value=value)
        log.info(f"输入钱包密码:{value}")

    def wallet_password_repeat_input(self, value: str):
        """
        重复输入钱包密码
        :param value: walletPasswordRepeat
        """
        self.input(loc=self.wallet_password_repeat, value=value)
        log.info(f"重复输入钱包密码:{value}")

    def wallet_password_hint_input(self, value: str):
        """
        输入钱包密码提示
        :param value: walletPasswordHint
        """
        self.input(loc=self.wallet_password_hint, value=value)
        log.info(f"输入钱包密码提示:{value}")

    def user_agreement_click(self):
        """
        点击用户协议
        """
        self.click(loc=self.user_agreement)
        log.info("点击用户协议")

    def create_wallet_confirm_click(self):
        """
        点击创建钱包按钮
        """
        self.click(loc=self.create_wallet_confirm)
        log.info("点击创建钱包按钮")
