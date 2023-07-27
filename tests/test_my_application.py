import re
from playwright.sync_api import Page, expect


def test_homepage_has_playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # 期望标题“包含”子字符串。
    expect(page).to_have_title(re.compile("Playwright"))

    # 创建定位器
    get_started = page.locator("text=Get Started")

    # 期望属性“严格等于”值。
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # 单击链接。
    get_started.click()


    # 要求URL包含 intro.
    expect(page).to_have_url(re.compile(".*intro"))