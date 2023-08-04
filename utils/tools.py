from typing import Text, Dict
import os


def get_path(path: Text) -> Text:
    """
    获取项目绝对路径
    :param path: 拼接路径
    :return: 返回拼接路径文件的绝对路径
    """
    if path[0] != '/':
        path = f'/{path}'
    return f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{path}"


def 日期控件填写():
    pass
