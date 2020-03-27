"""
测试用例
"""

import json
import re
import os
import sys
import unittest
from itertools import chain
from time import sleep

import allure
import ddt
import demjson
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from setting.project_config import *
from tool.connect_mysql import ConnectMySQL
from tool.read_write_yaml import merge_yaml, write_yaml
from tool.beautiful_report_run import beautiful_report_run
from tool.function_assistant import function_dollar, function_rn, function_rl, function_sql


@allure.feature(test_scenario)
@ddt.ddt
# 声明使用ddt
class DemoTest(unittest.TestCase):
    temporary_yaml = yaml_path + "/temporary.yaml"
    if os.path.isfile(temporary_yaml):
        # 如果临时yaml文件存在
        os.remove(temporary_yaml)
        # 删除之
    temporary_list = merge_yaml()
    # 调用合并所有yaml文件的方法
    temporary_yaml = yaml_path + write_yaml("/temporary.yaml", temporary_list)

    # 调用写入yaml文件的方法

    @classmethod
    def setUpClass(cls) -> None:
        cls.variable_result_dict = {}
        # 定义一个变量名与提取的结果字典
        # cls.variable_result_dict与self.variable_result_dict都是本类的公共属性

    @allure.story(test_story)
    @allure.severity(test_case_priority[0])
    @allure.testcase(test_case_address, test_case_address_title)
    @ddt.file_data(yaml_path + "/temporary.yaml")
    # 传入临时yaml文件
    def test_demo(self, **kwargs):
        """
        测试用例
        :param kwargs:
        :return:
        """

        global mysql_result_list_after

        kwargs = str(kwargs)
        if "None" in kwargs:
            kwargs = kwargs.replace("None", "''")
        kwargs = demjson.decode(kwargs)
        # 把值为None的替换成''空字符串，因为None无法拼接
        # demjson.decode()等价于json.loads()反序列化

        case_name = kwargs.get("case_name")
        # 用例名称
        self._testMethodDoc = case_name
        # 测试报告里面的用例描述
        mysql = kwargs.get("mysql")
        # mysql语句
        request_mode = kwargs.get("request_mode")
        # 请求方式
        api = kwargs.get("api")
        # 接口路径
        if type(api) != str:
            api = str(api)
        payload = kwargs.get("data")
        # 请求体
        if type(payload) != str:
            payload = str(payload)
        headers = kwargs.get("headers")
        # 请求头
        if type(headers) != str:
            headers = str(headers)
        query_string = kwargs.get("query_string")
        # 请求参数
        if type(query_string) != str:
            query_string = str(query_string)
        expected_code = kwargs.get("expected_code")
        # 预期的响应代码
        expected_result = kwargs.get("expected_result")
        # 预期的响应结果
        if type(expected_result) != str:
            expected_result = str(expected_result)
        regular = kwargs.get("regular")
        # 正则

        logger.info("{}>>>开始执行", case_name)
        if environment == "formal" and mysql:
            self.skipTest("生产环境跳过此用例，请忽略")
        # 生产环境不能连接MySQL数据库，因此跳过，此行后面的都不会执行

        if self.variable_result_dict:
            # 如果变量名与提取的结果字典不为空
            if mysql:
                if mysql[0]:
                    mysql[0] = function_dollar(mysql[0], self.variable_result_dict.items())
                # 调用替换$的方法
                if mysql[1]:
                    mysql[1] = function_dollar(mysql[1], self.variable_result_dict.items())
                if mysql[2]:
                    mysql[2] = function_dollar(mysql[2], self.variable_result_dict.items())
            if api:
                api = function_dollar(api, self.variable_result_dict.items())
            if payload:
                payload = function_dollar(payload, self.variable_result_dict.items())
            if headers:
                headers = function_dollar(headers, self.variable_result_dict.items())
            if query_string:
                query_string = function_dollar(query_string, self.variable_result_dict.items())
            if expected_result:
                expected_result = function_dollar(expected_result, self.variable_result_dict.items())
        else:
            pass

        if mysql:
            db = ConnectMySQL()
            # 实例化一个MySQL操作对象
            if mysql[0]:
                mysql[0] = function_rn(mysql[0])
                # 调用替换RN随机数字的方法
                mysql[0] = function_rl(mysql[0])
                # 调用替换RL随机字母的方法
                if "INSERT" in mysql[0]:
                    db.insert_mysql(mysql[0])
                    # 调用插入mysql的方法
                    sleep(2)
                    # 等待2秒钟
                if "UPDATE" in mysql[0]:
                    db.update_mysql(mysql[0])
                    # 调用更新mysql的方法
                    sleep(2)
                if "DELETE" in mysql[0]:
                    db.delete_mysql(mysql[0])
                    # 调用删除mysql的方法
                    sleep(2)
            if mysql[1]:
                mysql[1] = function_rn(mysql[1])
                # 调用替换RN随机数字的方法
                mysql[1] = function_rl(mysql[1])
                # 调用替换RL随机字母的方法
                if "SELECT" in mysql[1]:
                    mysql_result_tuple = db.query_mysql(mysql[1])
                    # mysql查询结果元祖
                    mysql_result_list = list(chain.from_iterable(mysql_result_tuple))
                    # 把二维元祖转换为一维列表
                    logger.info("发起请求之前mysql查询的结果列表为：{}", mysql_result_list)
                    if api:
                        api = function_sql(api, mysql_result_list)
                        # 调用替换MySQL查询结果的方法
                    if payload:
                        payload = function_sql(payload, mysql_result_list)
                    if headers:
                        headers = function_sql(headers, mysql_result_list)
                    if query_string:
                        query_string = function_sql(query_string, mysql_result_list)
                    if expected_result:
                        expected_result = function_sql(expected_result, mysql_result_list)

        if api:
            api = function_rn(api)
            api = function_rl(api)
        if payload:
            payload = function_rn(payload)
            payload = function_rl(payload)
            payload = demjson.decode(payload)
        if headers:
            headers = function_rn(headers)
            headers = function_rl(headers)
            headers = demjson.decode(headers)
        if query_string:
            query_string = function_rn(query_string)
            query_string = function_rl(query_string)
            query_string = demjson.decode(query_string)

        url = service_domain + api
        # 拼接完整地址

        logger.info("请求方式为：{}", request_mode)
        logger.info("地址为：{}", url)
        logger.info("请求体为：{}", payload)
        logger.info("请求头为：{}", headers)
        logger.info("请求参数为：{}", query_string)
        logger.info("预期的响应代码为：{}", expected_code)
        logger.info("预期的响应结果为：{}", expected_result)

        response = requests.request(
            request_mode, url, data=json.dumps(payload),
            headers=headers, params=query_string, timeout=(12, 18)
        )
        # 发起HTTP请求
        # json.dumps()序列化把字典转换成字符串，json.loads()反序列化把字符串转换成字典
        # data请求体为字符串，headers请求头与params请求参数为字典

        actual_time = response.elapsed.total_seconds()
        # 实际的响应时间
        actual_code = response.status_code
        # 实际的响应代码
        actual_result_text = response.text
        # 实际的响应结果（文本格式）

        if mysql:
            if mysql[2]:
                mysql[2] = function_rn(mysql[2])
                mysql[2] = function_rl(mysql[2])
                if "SELECT" in mysql[2]:
                    db_after = ConnectMySQL()
                    mysql_result_tuple_after = db_after.query_mysql(mysql[2])
                    mysql_result_list_after = list(chain.from_iterable(mysql_result_tuple_after))
                    mysql_result_list_after = list(map(str, mysql_result_list_after))
                    # 把列表里面的元素类型全部改为str
                    logger.info("发起请求之后mysql查询的结果列表为：{}", mysql_result_list_after)

        logger.info("实际的响应代码为：{}", actual_code)
        logger.info("实际的响应结果为：{}", actual_result_text)
        logger.info("实际的响应时间为：{}", actual_time)

        if regular:
            # 如果正则不为空
            extract_list = []
            # 定义一个提取结果列表
            for i in regular["expression"]:
                regular_result = re.findall(i, actual_result_text)[0]
                # re.findall(正则表达式, 实际的响应结果)返回一个符合规则的list，取第1个
                extract_list.append(regular_result)
                # 把提取结果添加到提取结果列表里面
            temporary_dict = dict(zip(regular["variable"], extract_list))
            # 把变量列表与提取结果列表转为一个临时字典
            for key, value in temporary_dict.items():
                self.variable_result_dict[key] = value
            # 把临时字典合并到变量名与提取的结果字典，已去重
        else:
            pass

        for key in list(self.variable_result_dict.keys()):
            if not self.variable_result_dict[key]:
                del self.variable_result_dict[key]
        # 删除变量名与提取的结果字典中为空的键值对

        expected_result = re.sub("{|}|\'|\"|\\[|\\]| ", "", expected_result)
        actual_result_text = re.sub("{|}|\'|\"|\\[|\\]| ", "", actual_result_text)
        # 去除大括号{、}、单引号'、双引号"、中括号[、]与空格
        expected_result_list = re.split(":|,", expected_result)
        actual_result_list = re.split(":|,", actual_result_text)
        # 把文本转为列表，并去除:与,
        logger.info("切割之后预期的响应结果列表为：{}", expected_result_list)
        logger.info("切割之后实际的响应结果列表为：{}", actual_result_list)

        boolean_expression = set(expected_result_list) <= set(actual_result_list)
        # 布尔表达式，判断是否是其子集
        # 预期的响应结果与实际的响应结果是被包含关系
        if mysql:
            if mysql[2]:
                boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                    mysql_result_list_after) <= set(actual_result_list)
            # 双重断言
            # 预期的响应结果与实际的响应结果是被包含关系
            # 发起请求之后mysql查询结果与实际的响应结果是被包含关系
        if expected_code == actual_code:
            if boolean_expression:
                logger.info("{}>>>执行通过", case_name)
            else:
                logger.error("{}>>>执行失败！！！", case_name)
            logger.info("##########用例分隔符##########\n")
            self.assertTrue(boolean_expression)
        else:
            logger.error("{}>>>执行失败！！！", case_name)
            try:
                self.assertEqual(expected_code, actual_code)
            except AssertionError as e:
                logger.error("预期的响应代码与实际的响应代码不相等：{}", e)
                logger.info("##########用例分隔符##########\n")
                raise e


if __name__ == '__main__':
    beautiful_report_run(DemoTest)
    # 调用BeautifulReport运行方式
