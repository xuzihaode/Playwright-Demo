from models import *


class 产品首页(Page_Object):
    def __init__(self, page: Page):
        super().__init__(page)
        self.新建产品 = self.page.get_by_text("新建产品")

    def navigate(self):
        self.jump()

    def create_产品(self, 产品名称):
        self.page.get_by_text("")
        self.page.get_by_placeholder("")
        pass
