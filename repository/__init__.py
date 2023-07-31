from config.config_load import config
from models.models import LoginModel
from utils.tools import load_yaml_file

# 对象库


# yaml文件转换为Dict字典
__object_data = load_yaml_file(config.repository_path)
# 获取loginPage（data/ui_data.yml）下的所有子元素
loginObject = LoginModel.parse_obj(__object_data['loginPage '])
