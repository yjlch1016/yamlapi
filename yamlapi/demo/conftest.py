"""
全局钩子文件
"""

from datetime import datetime

import pytest
from py._xmlgen import html

from setting.project_config import *


def pytest_configure(config):
    """
    添加环境信息
    :param config:
    :return:
    """

    config._metadata["项目名称"] = project_name
    config._metadata["Swagger地址"] = swagger_address


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    """
    添加附加摘要信息
    :param prefix:
    :param summary:
    :param postfix:
    :return:
    """

    prefix.extend([html.p(test_department)])
    prefix.extend([html.p(tester)])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """
    添加带有测试函数docstring的description列，添加可排序的time列，并删除links列
    :param cells:
    :return:
    """

    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
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


def pytest_addoption(parser):
    """
    注册自定义的命令
    :param parser:
    :return:
    """

    parser.addoption(
        "--cmd", action="store", default="test", help="被测环境的缩写"
    )


@pytest.fixture(scope="session", autouse=True)
def cmd(request):
    """
    获取从命令行传入的值
    :param request:
    :return:
    """

    environment = request.config.getoption("--cmd")
