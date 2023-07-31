from playwright.sync_api import expect, Page, sync_playwright
from interface.page_login_save_cookies import page_login_save_cookies, jump


def test_pw_test(page):
    page_login_save_cookies(page, "zihaoxujob@163.com", "Aa123456@")
    page.pause()
    jump(page, 'pjm/projects')
    page.wait_for_timeout(4000)
    # page_login_save_cookies(page,"17760272549","Aa123456@")
    # page.wait_for_timeout(3000)
