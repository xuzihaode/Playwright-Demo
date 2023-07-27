from typing import Text, Dict
import yaml


# yaml文件转换为Dict字典 的方法
def load_yaml_file(yaml_file: Text) -> Dict:
    with open(yaml_file, mode='rb') as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_content
