def test_产品创建(pw_page):
    pw_page.产品首页.获取cookies()
    pw_page.产品首页.navigate('/path/path')
    pw_page.产品首页.新建产品.click()
    pw_page.产品首页.create_产品()
    pw_page.产品首页.page.wait_for_timeout(10000)
