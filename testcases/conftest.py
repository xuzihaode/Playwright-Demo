# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import shutil
import os
import sys
import warnings
import time
from typing import Any, Callable, Dict, Generator, List, Optional

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    BrowserType,
    Error,
    Page,
    Playwright,
    sync_playwright,
    expect,
    Request,
    Response,
    Route,
)
from slugify import slugify
import tempfile

from models.page_object import Page_Object
from models.产品首页模块 import 产品首页

# 这里导入models目录下所有的模块中的所有类

if sys.platform == 'linux':  # 如果在linux系统下运行时，将日志输出到终端
    sys.stdout = sys.stderr  # 用于解决在linux系统下运行时，日志输出到终端的问题
artifacts_folder = tempfile.TemporaryDirectory(prefix="playwright-pytest-")
# 用于将项目根目录添加到 sys.path 中，这样就可以在测试用例中导入项目中的模块了
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
expect.set_default_timeout(30000)  # 设定断言默认超时时间为30秒，之前默认时间为5秒


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "record_video_size": {
            "width": 1920,
            "height": 1080,
        }
    }


# 定义一个 pytest fixture，用于在测试用例中自动打开浏览器
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        # 在 fixture 中使用 chromium.launch() 来打开浏览器
        browser = pw.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        # 在 fixture 结束时关闭浏览器
        browser.close()


# 定义一个 pytest fixture，用于在测试用例中创建浏览器上下文
@pytest.fixture(scope="function")
def context(browser):
    # 在 fixture 中使用 browser.new_context() 来创建浏览器上下文
    context = browser.new_context()
    yield context
    # 在 fixture 结束时关闭浏览器上下文
    context.close()


class 页面实例化:
    # 类属性
    产品首页: 产品首页 = 产品首页

    def __init__(self, page: Page, log_dir, test_name):
        self.page = page
        self.log_dir = log_dir
        self.test_name = test_name

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if isinstance(attr, type) and issubclass(attr, Page_Object):
            instance = attr(self.page)
            setattr(self, item, instance)
            return instance
        return attr

    def page_instance(self, page: Page):
        return 页面实例化(page, self.log_dir, self.test_name)


@pytest.fixture
def log_dir():
    # 在 fixture 中使用 browser.new_context() 来创建浏览器上下文
    log_dir = os.path.join(artifacts_folder.name, slugify(pytest.item.name, separator="_"))
    os.makedirs(log_dir)
    yield log_dir
    # 在 fixture 结束时关闭浏览器上下文
    shutil.rmtree(log_dir)


@pytest.fixture
def test_name(request):
    return request.node.test_name


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    pw = sync_playwright().start()
    session_start_time = time.time()
    yield pw
    print(f"本轮测试耗时: {int(time.time() - session_start_time)}秒")
    pw.stop()


@pytest.fixture()
def pw_page(context):
    page = context.new_page()
    yield 页面实例化(page, log_dir, test_name)
