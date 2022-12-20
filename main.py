import os
from utils.logger_util import log
import pytest

import yaml

if __name__ == '__main__':
    log.info("=====测试开始=====")
    pytest.main(['--reruns', '3', 'test_cases', '-sv', '--alluredir', './report/report-data', '--clean-alluredir'])
    os.system('allure generate ./report/report-data -o ./report/report-allure --clean')
    log.info("=====测试结束=====")
