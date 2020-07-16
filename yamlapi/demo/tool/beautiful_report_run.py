import unittest

from BeautifulReport import BeautifulReport

from setting.project_config import *


def beautiful_report_run(test_class):
    """
    BeautifulReport运行方式
    :param test_class: 参数为测试类名
    :return:
    """

    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    result = BeautifulReport(suite)
    result.report(
        filename=beautiful_filename,
        # 测试报告文件名称, 如果不指定，默认文件名为report.html
        description=beautiful_description,
        # 测试报告名称展示
        report_dir=report_log_path,
        # 测试报告文件写入路径
        theme="theme_default",
        # 测试报告主题样式
    )
    # BeautifulReport生成html测试报告

    logger.info("被测环境：{}", environment)
    logger.info("用例总数：{}", result.testsRun)
    logger.info("通过总数：{}", result.success_count)
    logger.info("失败总数：{}", result.failure_count)
    logger.info("跳过总数：{}", result.skipped)
    logger.info("错误总数：{}", result.error_count)
    # 日志
