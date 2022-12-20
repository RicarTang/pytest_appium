import json
from typing import Optional
import yaml


class LoadFile(object):
    """
    读取文件类
    """

    def __init__(self, file: str, mode: str, encoding: Optional[str] = 'utf-8'):
        self.file = file
        self.mode = mode
        self.encoding = encoding

    def __iter__(self):
        """
        生成器函数
        :return:
        """
        if self.file.endswith('.yaml') or self.file.endswith('.yml'):
            for item in self.load_yaml():
                yield item
        elif self.file.endswith('.json'):
            for item in self.load_json():
                yield item
        elif self.file.endswith('.xlsx'):
            for item in self.load_excel():
                yield item

    def load_yaml(self) -> list:
        """
        读取yaml文件
        :return: list
        """
        with open(file=self.file, mode=self.mode, encoding=self.encoding) as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def load_json(self) -> list:
        """
        读取json文件
        :return: list
        """
        with open(file=self.file, mode=self.mode, encoding=self.encoding) as f:
            return json.load(f)

    def load_excel(self):
        pass


if __name__ == '__main__':
    import os.path
    import collections
    filepath = os.path.join(os.path.dirname(__file__), '../data/test_data/create_wallet.yaml')
    for i in LoadFile(file=filepath, mode='r'):
        print(i)

