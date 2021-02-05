"""
全局钩子文件
"""

from datetime import datetime

import pytest
from py._xmlgen import html

from setting.project_config import *
from tool.feishu_robot import send_feishu_alarm
from tool.dingtalk_robot import send_dingtalk_alarm


def pytest_html_report_title(report):
    """
    添加标题
    :param report:
    :return:
    """
    report.title = html_report_title


def pytest_configure(config):
    """
    添加环境信息
    :param config:
    :return:
    """

    config._metadata["项目名称"] = project_name
    config._metadata["Swagger地址"] = swagger_address


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


def pytest_html_results_table_header(cells):
    """
    添加带有测试函数docstring的description列，添加可排序的time列，并删除test与links列
    :param cells:
    :return:
    """

    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()
    cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.now().replace(microsecond=0), class_='col-time'))
    cells.pop()
    cells.pop(2)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

    if report.when == "call":
        print("用例名称：%s" % str(item.function.__doc__))
        print("运行结果：%s" % report.outcome)


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


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    统计测试结果
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    """

    logger.info("环境：{}", environment)
    total = terminalreporter._numcollected
    logger.info("总共：{}条", total)
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'setup' and i.when != 'teardown'])
    logger.info("通过：{}条", passed)
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'setup' and i.when != 'teardown'])
    logger.info("失败：{}条", failed)
    error = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'setup' and i.when != 'teardown'])
    logger.info("错误：{}条", error)
    skipped = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'setup' and i.when != 'teardown'])
    logger.info("跳过：{}条", skipped)
    successful = passed / total
    logger.info("成功率：{:.2%}", successful)
    duration = time.time() - terminalreporter._sessionstarttime
    logger.info("总共耗时：{:.2f}秒", duration)

    if robot == "feishu":
        send_feishu_alarm(total, passed, failed, error, skipped, successful, duration)
        # 发送飞书报警
    elif robot == "dingtalk":
        send_dingtalk_alarm(total, passed, failed, error, skipped, successful, duration)
        # 发送钉钉报警
    else:
        pass
