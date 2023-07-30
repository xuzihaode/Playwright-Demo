from playwright.sync_api import expect,Page
import json, os, time
from utils.tools import get_path

def page_login_save_cookies(page:Page, username:str, password:str):
    """
    拿到网站cookies进行登陆，并判断网站cookies是否过期，如未过期则读取cookies文数据进行登陆，如已过期则执行ui登陆并重新写入新的cookies
    :param page: page对象
    :param username:
    :param password:
    :return:
    """
    if os.path.exists(get_path(f"/.auth/{username}.json")) and int(time.time() - os.path.getctime(get_path(f"/.auth/{username}.json"))) < 86400:
        page.context.clear_cookies()
        with open(get_path(f"/.auth/{username}.json")) as f:
            cookies = f.read()
        cookies = json.loads(cookies)
        page.context.add_cookies(cookies)
        page.goto("https://0123456789.pingcode.com")
        expect(page.locator('.avatar-default').first).to_be_visible()
    else:
        page.context.clear_cookies()
        page.goto("https://0123456789.pingcode.com")
        page.get_by_placeholder("请输入手机号/邮箱").type(username, delay=30)
        page.get_by_placeholder("请输入登录密码").fill(password)
        page.get_by_role("button", name="登录").click()
        expect(page.locator('.avatar-default').first).to_be_visible()
        cookies = page.context.cookies()
        with open(get_path(f"/.auth/{username}.json"),'w') as f:
            # 用于将 Python 对象（如字典、列表等）序列化为 JSON 格式，并将序列化后的 JSON 数据写入到文件中
            json.dump(cookies, f)

# def jump(page:Page, path:str):
#     if path[0] != '/':
#         path = f'/{path}'
#     page.goto(f"{page.url.split('./com')[0]}.com{path}")

def jump(page:Page, path:str):
    """
    跳转到指定页面
    :param page: page对象
    :param path: 跳转路径
    :return:
    """
    if path[0] != '/':
        path = f'/{path}'
    old_url= f"{page.url.split('./com')[0]}.com{path}"
    start_index = old_url.find("com")
    end_index = old_url.rfind("com")
    if start_index != -1 and end_index != -1:
        filtered_url = old_url[:start_index + 3] + old_url[end_index + 3:]
        page.goto(filtered_url)
    else:
        page.goto(old_url)



