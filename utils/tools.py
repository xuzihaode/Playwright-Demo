from typing import Text, Dict
import yaml, os


# yaml文件转换为Dict字典 的方法
def load_yaml_file(yaml_file: Text) -> Dict:
    """
    yaml文件转换为Dict字典 的方法
    :param yaml_file: yaml文件路径
    :return: 返回Dict字典
    """
    with open(yaml_file, mode='rb') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_content


def get_path(path: Text) -> Text:
    """
    获取项目绝对路径
    :param path: 拼接路径
    :return: 返回拼接路径文件的绝对路径
    """
    if path[0] != '/':
        path = f'/{path}'
    return f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{path}"