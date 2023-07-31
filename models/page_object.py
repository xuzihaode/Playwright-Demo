import json
import os
import time

from playwright.sync_api import expect, Page

from utils.tools import get_path


class Page_Object:
    def __init__(self, page: Page):
        self.page = page
        timeout = 10000
        self.page.set_default_timeout(timeout)
        self.page.set_default_navigation_timeout(timeout)
        self.url = 'https://0123456789.pingcode.com'

    def 跳转(self):
        self.jump()

    def jump(self, path: str = None):
        """
        跳转到指定页面
        :param path: 跳转路径
        :return:
        """
        if path[0] != '/':
            path = f'/{path}'
        old_url = f"{self.page.url.split('./com')[0]}.com{path}"
        start_index = old_url.find("com")
        end_index = old_url.rfind("com")
        if start_index != -1 and end_index != -1:
            filtered_url = old_url[:start_index + 3] + old_url[end_index + 3:]
            self.page.goto(filtered_url)
        else:
            self.page.goto(old_url)

    def 获取cookies(self, username: str, password: str):
        """
        拿到网站cookies进行登陆，并判断网站cookies是否过期，如未过期则读取cookies文数据进行登陆，如已过期则执行ui登陆并重新写入新的cookies
        :param username:
        :param password:
        :return:
        """
        if os.path.exists(get_path(f"/.auth/{username}.json")) and int(
                time.time() - os.path.getctime(get_path(f"/.auth/{username}.json"))) < 86400:
            self.page.context.clear_cookies()
            with open(get_path(f"/.auth/{username}.json")) as f:
                cookies = f.read()
            cookies = json.loads(cookies)
            self.page.context.add_cookies(cookies)
            self.page.goto(self.url)
            expect(self.page.locator('.avatar-default').first).to_be_visible()
        else:
            self.page.context.clear_cookies()
            self.page.goto(self.url)
            self.page.get_by_placeholder("请输入手机号/邮箱").type(username, delay=30)
            self.page.get_by_placeholder("请输入登录密码").fill(password)
            self.page.get_by_role("button", name="登录").click()
            expect(self.page.locator('.avatar-default').first).to_be_visible()
            cookies = self.page.context.cookies()
            with open(get_path(f"/.auth/{username}.json"), 'w') as f:
                # 用于将 Python 对象（如字典、列表等）序列化为 JSON 格式，并将序列化后的 JSON 数据写入到文件中
                json.dump(cookies, f)

    @classmethod
    def 获取项目绝对路径(cls, path: str) -> str:
        """
        获取项目绝对路径
        :param path: 拼接路径
        :return: 返回拼接路径文件的绝对路径
        """
        if path[0] != '/':
            path = f'/{path}'
        return f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}{path}"


