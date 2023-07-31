from playwright.sync_api import Page
from repository import loginObject


class LoginPage:
    def __init__(self, page: Page):
        self.organization_input = page.locator(loginObject.username)


if __name__ == '__main__':
    page: Page
    loginPage = LoginPage(page)
    loginPage.organization_input.fill()
