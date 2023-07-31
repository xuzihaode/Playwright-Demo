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
)
from slugify import slugify
import tempfile

# 用于将项目根目录添加到 sys.path 中，这样就可以在测试用例中导入项目中的模块了
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

artifacts_folder = tempfile.TemporaryDirectory(prefix="playwright-pytest-")


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
