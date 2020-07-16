import tablib

from setting.project_config import *


def export_various_formats(test_case_data_list):
    """
    导出各种格式的测试用例
    :param test_case_data_list: 参数为测试用例数据列表
    :return:
    """

    test_case_data_list_removal = list(set(test_case_data_list))
    test_case_data_list_removal.sort(key=test_case_data_list.index)
    # 去重并且不改变顺序

    headers = ["用例名称", "步骤名称", "请求方式", "请求地址", "请求体", "请求头", "请求参数",
               "预期的响应时间", "预期的响应代码", "预期的响应结果"]
    # 文件头
    dataset = tablib.Dataset(headers=headers, *test_case_data_list_removal)
    # 添加数据

    try:
        with open(report_log_path + '/test_case.xlsx', 'wb') as x:
            x.write(dataset.export('xlsx'))
    except Exception as e:
        logger.error("测试用例导出为xlsx发生错误：{}", e)

    try:
        with open(report_log_path + '/test_case.csv', 'w', newline='') as c:
            c.write(dataset.export('csv'))
    except Exception as e:
        logger.error("测试用例导出为csv发生错误：{}", e)

    try:
        with open(report_log_path + '/test_case.json', 'w') as j:
            j.write(dataset.export('json').encode("utf-8").decode("unicode_escape"))
    except Exception as e:
        logger.error("测试用例导出为json发生错误：{}", e)

    try:
        with open(report_log_path + '/test_case.yaml', 'w') as y:
            y.write(dataset.export('yaml').encode("utf-8").decode("unicode_escape"))
    except Exception as e:
        logger.error("测试用例导出为yaml发生错误：{}", e)

    try:
        with open(report_log_path + '/test_case.html', 'w') as h:
            h.write(dataset.export('html'))
    except Exception as e:
        logger.error("测试用例导出为html发生错误：{}", e)
