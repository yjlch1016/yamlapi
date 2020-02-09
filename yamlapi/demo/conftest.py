"""
全局钩子文件
"""

from datetime import datetime

import pytest
from py._xmlgen import html


def pytest_configure(config):
    # 添加环境信息

    config._metadata["项目名称"] = "XXX接口自动化测试"
    config._metadata["Swagger地址"] = "http://www.test.com/swagger-ui.html"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    # 添加附加摘要信息

    prefix.extend([html.p("测试部门：")])
    prefix.extend([html.p("测试人员：")])


def pytest_html_results_table_header(cells):
    # 添加带有测试函数docstring的description列，添加可排序的time列，并删除links列

    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
