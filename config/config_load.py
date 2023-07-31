import configparser


# 读取初始化配置信息

class CAO:
    __config_file = r'D:\PythonCode\Playwright\config\config.ini'

    def __init__(self):
        c = configparser.ConfigParser()
        c.read(CAO.__config_file)
        self.__repository_path = c.get('repository', 'repository_path')

    @property
    def repository_path(self):
        return self.__repository_path


# 初始化配置文件信息，只执行一次
config = CAO()
