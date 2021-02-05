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
from tool.connect_postgresql import ConnectPostgreSQL
from tool.connect_mongo import ConnectMongo
from tool.connect_influx import ConnectInflux
from tool.data_type_conversion import data_conversion_string
from tool.export_test_case import export_various_formats
from tool.read_write_yaml import merge_yaml
from tool.read_write_json import merge_json
from tool.beautiful_report_run import beautiful_report_run
from tool.function_assistant import function_dollar, function_rn, function_rl, \
    function_sql, function_mp, function_rd, function_mongo, function_pgsql


@allure.feature(test_scenario)
@ddt.ddt
# 声明使用ddt
class DemoTest(unittest.TestCase):
    if test_case_format == "yaml":
        temporary_list = merge_yaml()
        # 调用合并所有yaml文件的方法
    if test_case_format == "json":
        temporary_list = merge_json()
        # 调用合并所有json文件的方法

    @classmethod
    def setUpClass(cls) -> None:
        """
        准备工作
        :return:
        """

        cls.variable_result_dict = {}
        # 定义一个变量名与提取的结果字典
        # cls.variable_result_dict与self.variable_result_dict都是本类的公共属性

        cls.test_case_data_list = []
        # 定义一个测试用例数据列表

    @allure.story(test_story)
    @allure.severity(test_case_priority)
    @allure.testcase(test_case_address, test_case_address_title)
    @ddt.data(*temporary_list)
    # 传入临时yaml列表
    @ddt.unpack
    # 解包
    def test_demo(self, case_name, step):
        """{case_name}"""

        global mysql_result_list_after, pgsql_result_list_after, \
            mongo_result_list_after, temporary_list

        self._testMethodDoc = case_name
        # 测试报告里面的用例描述
        logger.info("**********{}>>>开始执行**********\n", case_name)

        for item in step:
            # 步骤列表
            item = str(item)
            if "None" in item:
                item = item.replace("None", "''")
            item = demjson.decode(item)
            # 把值为None的替换成''空字符串，因为None无法拼接
            # demjson.decode()等价于json.loads()反序列化
            step_name = item.get("step_name")
            # 步骤名称
            mysql = item.get("mysql")
            # mysql语句
            pgsql = item.get("pgsql")
            # pgsql语句
            mongo = item.get("mongo")
            # mongo语句
            request_mode = item.get("request_mode")
            # 请求方式
            api = item.get("api")
            # 接口路径
            if type(api) != str:
                api = str(api)
            file = item.get("file")
            # 文件
            payload = item.get("body")
            # 请求体
            if payload:
                if type(payload) != str:
                    payload = str(payload)
            headers = item.get("headers")
            # 请求头
            if headers:
                if type(headers) != str:
                    headers = str(headers)
            query_string = item.get("query_string")
            # 请求参数
            if query_string:
                if type(query_string) != str:
                    query_string = str(query_string)
            expected_time = item.get("expected_time")
            # 预期的响应时间
            if expected_time:
                if type(expected_time) != float:
                    expected_time = float(expected_time)
            expected_code = item.get("expected_code")
            # 预期的响应代码
            expected_result = item.get("expected_result")
            # 预期的响应结果
            if type(expected_result) != str:
                expected_result = str(expected_result)
            regular = item.get("regular")
            # 正则

            logger.info("步骤名称为：{}", step_name)
            if environment == "formal" and mysql or \
                    environment == "formal" and pgsql or \
                    environment == "formal" and mongo:
                self.skipTest("跳过生产环境，请忽略")
            # 生产环境不能连接MySQL数据库或者PostgreSQL数据库或者Mongo数据库，因此跳过，此行后面的都不会执行

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
                if pgsql:
                    if pgsql[0]:
                        pgsql[0] = function_dollar(pgsql[0], self.variable_result_dict.items())
                    # 调用替换$的方法
                    if pgsql[1]:
                        pgsql[1] = function_dollar(pgsql[1], self.variable_result_dict.items())
                    if pgsql[2]:
                        pgsql[2] = function_dollar(pgsql[2], self.variable_result_dict.items())
                if mongo:
                    if mongo[0]:
                        if mongo[0][2]:
                            if type(mongo[0][2]) != str:
                                mongo[0][2] = str(mongo[0][2])
                            mongo[0][2] = function_dollar(mongo[0][2], self.variable_result_dict.items())
                            # 调用替换$的方法
                    if mongo[1]:
                        if mongo[1][1]:
                            if type(mongo[1][1]) != str:
                                mongo[1][1] = str(mongo[1][1])
                            mongo[1][1] = function_dollar(mongo[1][1], self.variable_result_dict.items())
                    if mongo[2]:
                        if mongo[2][1]:
                            if type(mongo[2][1]) != str:
                                mongo[2][1] = str(mongo[2][1])
                            mongo[2][1] = function_dollar(mongo[2][1], self.variable_result_dict.items())
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
                    mysql[0] = function_mp(mysql[0])
                    # 调用替换MP随机手机号码的方法
                    mysql[0] = function_rd(mysql[0])
                    # 调用替换RD随机日期时间的方法
                    if "INSERT" in mysql[0] or "insert" in mysql[0]:
                        db.insert_mysql(mysql[0])
                        # 调用插入mysql的方法
                        sleep(2)
                        # 等待2秒钟
                    if "UPDATE" in mysql[0] or "update" in mysql[0]:
                        db.update_mysql(mysql[0])
                        # 调用更新mysql的方法
                        sleep(2)
                    if "DELETE" in mysql[0] or "delete" in mysql[0]:
                        db.delete_mysql(mysql[0])
                        # 调用删除mysql的方法
                        sleep(2)
                if mysql[1]:
                    if "SELECT" in mysql[1] or "select" in mysql[1]:
                        mysql_result_tuple = db.query_mysql(mysql[1])
                        # mysql查询结果元祖
                        if mysql_result_tuple:
                            mysql_result_list = list(chain.from_iterable(mysql_result_tuple))
                            # 把二维元祖转换为一维列表
                            mysql_result_list = data_conversion_string(mysql_result_list)
                            # 调用数据类型转换的方法
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

            if pgsql:
                pgsql_db = ConnectPostgreSQL()
                # 实例化一个PostgreSQL操作对象
                if pgsql[0]:
                    pgsql[0] = function_rn(pgsql[0])
                    # 调用替换RN随机数字的方法
                    pgsql[0] = function_rl(pgsql[0])
                    # 调用替换RL随机字母的方法
                    pgsql[0] = function_mp(pgsql[0])
                    # 调用替换MP随机手机号码的方法
                    pgsql[0] = function_rd(pgsql[0])
                    # 调用替换RD随机日期时间的方法
                    if "INSERT" in pgsql[0] or "insert" in pgsql[0]:
                        pgsql_db.insert_postgresql(pgsql[0])
                        # 调用插入pgsql的方法
                        sleep(2)
                        # 等待2秒钟
                    if "UPDATE" in pgsql[0] or "update" in pgsql[0]:
                        pgsql_db.update_postgresql(pgsql[0])
                        # 调用更新pgsql的方法
                        sleep(2)
                    if "DELETE" in pgsql[0] or "delete" in pgsql[0]:
                        pgsql_db.delete_postgresql(pgsql[0])
                        # 调用删除pgsql的方法
                        sleep(2)
                if pgsql[1]:
                    if "SELECT" in pgsql[1] or "select" in pgsql[1]:
                        pgsql_result_tuple = pgsql_db.query_postgresql(pgsql[1])
                        # PostgreSQL查询结果元祖
                        if pgsql_result_tuple:
                            pgsql_result_list = list(chain.from_iterable(pgsql_result_tuple))
                            # 把二维元祖转换为一维列表
                            logger.info("发起请求之前PostgreSQL查询的结果列表为：{}", pgsql_result_list)
                            if api:
                                api = function_pgsql(api, pgsql_result_list)
                                # 调用替换PostgreSQL查询结果的方法
                            if payload:
                                payload = function_pgsql(payload, pgsql_result_list)
                            if headers:
                                headers = function_pgsql(headers, pgsql_result_list)
                            if query_string:
                                query_string = function_pgsql(query_string, pgsql_result_list)
                            if expected_result:
                                expected_result = function_pgsql(expected_result, pgsql_result_list)

            if mongo:
                mongo_db = ConnectMongo()
                # 实例化一个Mongo操作对象
                if mongo[0]:
                    if mongo[0][2]:
                        if type(mongo[0][2]) != str:
                            mongo[0][2] = str(mongo[0][2])
                        mongo[0][2] = function_rn(mongo[0][2])
                        mongo[0][2] = function_rl(mongo[0][2])
                        mongo[0][2] = function_mp(mongo[0][2])
                        mongo[0][2] = function_rd(mongo[0][2])
                        if type(mongo[0][2]) != dict:
                            mongo[0][2] = demjson.decode(mongo[0][2])
                    if mongo[0][1] == "insert":
                        if mongo[0][2]:
                            if type(mongo[0][2]) == dict:
                                mongo_db.insert_mongo_one(mongo[0][0], mongo[0][2])
                                # 调用插入Mongo（一条数据）的方法
                            if type(mongo[0][2]) == list:
                                mongo_db.insert_mongo_many(mongo[0][0], mongo[0][2])
                                # 调用插入Mongo（多条数据）的方法
                        sleep(2)
                    if mongo[0][1] == "remove":
                        if mongo[0][2]:
                            mongo_db.delete_mongo_one(mongo[0][0], mongo[0][2])
                            # 调用删除Mongo（一条数据）的方法
                        sleep(2)
                    if mongo[0][1] == "update":
                        if mongo[0][2]:
                            mongo_db.update_mongo_one(mongo[0][0], *mongo[0][2])
                            # 调用更新Mongo（一条数据）的方法
                        sleep(2)
                if mongo[1]:
                    mongo_result_dict = mongo_db.query_mongo_one(mongo[1][0], *mongo[1][1])
                    # 调用查询Mongo（一条数据）的方法
                    if mongo_result_dict:
                        mongo_result_list = list(mongo_result_dict.values())
                        # 把字典转换成列表
                        logger.info("发起请求之前mongo查询的结果列表为：{}", mongo_result_list)
                        if api:
                            api = function_mongo(api, mongo_result_list)
                            # 调用替换Mongo查询结果的方法
                        if payload:
                            payload = function_mongo(payload, mongo_result_list)
                        if headers:
                            headers = function_mongo(headers, mongo_result_list)
                        if query_string:
                            query_string = function_mongo(query_string, mongo_result_list)
                        if expected_result:
                            expected_result = function_mongo(expected_result, mongo_result_list)

            if api:
                api = function_rn(api)
                api = function_rl(api)
            if payload:
                payload = function_rn(payload)
                payload = function_rl(payload)
                payload = function_mp(payload)
                payload = function_rd(payload)
                payload = demjson.decode(payload)
            if headers:
                headers = function_rn(headers)
                headers = function_rl(headers)
                headers = function_mp(headers)
                payload = function_rd(payload)
                headers = demjson.decode(headers)
            if query_string:
                query_string = function_rn(query_string)
                query_string = function_rl(query_string)
                query_string = function_mp(query_string)
                query_string = function_rd(query_string)
                query_string = demjson.decode(query_string)
            if expected_result:
                expected_result = demjson.decode(expected_result)

            url = service_domain + api
            # 拼接完整地址

            logger.info("请求方式为：{}", request_mode)
            logger.info("请求地址为：{}", url)
            if payload:
                logger.info("请求体为：{}", json.dumps(payload, ensure_ascii=False))
            if headers:
                logger.info("请求头为：{}", json.dumps(headers, ensure_ascii=False))
            if query_string:
                logger.info("请求参数为：{}", json.dumps(query_string, ensure_ascii=False))
            if expected_time:
                logger.info("预期的响应时间为：{}秒", expected_time)
            logger.info("预期的响应代码为：{}", expected_code)
            logger.info("预期的响应结果为：{}", json.dumps(expected_result, ensure_ascii=False))

            self.test_case_data_list.append((
                case_name,
                step_name,
                request_mode,
                url,
                json.dumps(payload, ensure_ascii=False),
                json.dumps(headers, ensure_ascii=False),
                json.dumps(query_string, ensure_ascii=False),
                expected_time,
                expected_code,
                json.dumps(expected_result, ensure_ascii=False)
            ))
            # 把用例数据添加到测试用例数据列表

            try:
                if file:
                    # 如果file字段不为空
                    files = {file[0]: (file[1], open(yaml_path + "/" + file[1], 'rb'), file[2], {'Expires': '0'})}
                    response = requests.request(
                        request_mode, url, files=files, data=json.dumps(payload),
                        headers=headers, params=query_string, timeout=(15, 20)
                    )
                    # 上传文件
                else:
                    response = requests.request(
                        request_mode, url, data=json.dumps(payload),
                        headers=headers, params=query_string, timeout=(15, 20)
                    )
                    # 发起HTTP请求
                    # json.dumps()序列化把字典转换成字符串，json.loads()反序列化把字符串转换成字典
                    # data请求体为字符串，headers请求头与params请求参数为字典
            except Exception as e:
                logger.error("HTTP请求发生错误：{}", e)
                raise e

            try:
                actual_time = response.elapsed.total_seconds()
                logger.info("实际的响应时间为：{}秒", actual_time)
            except Exception as e:
                logger.error("获取实际的响应时间发生错误：{}", e)
                raise e
            try:
                actual_code = response.status_code
                logger.info("实际的响应代码为：{}", actual_code)
            except Exception as e:
                logger.error("获取实际的响应代码发生错误：{}", e)
                raise e
            try:
                actual_headers = response.headers
                logger.info("实际的响应头为：{}", actual_headers)
            except Exception as e:
                logger.error("获取实际的响应头发生错误：{}", e)
                raise e
            try:
                actual_result_text = response.text
                logger.info("实际的响应结果为：{}", actual_result_text)
            except Exception as e:
                logger.error("获取实际的响应结果发生错误：{}", e)
                raise e

            if influxdb_switch:
                influx_db = ConnectInflux()
                # 实例化一个InfluxDB操作对象
                influx_db.insert_influx_one(environment, case_name, step_name, url, actual_time, actual_code)
                # 往InfluxDB插入一条数据

            if mysql:
                if mysql[2]:
                    if "SELECT" in mysql[2] or "select" in mysql[2]:
                        db_after = ConnectMySQL()
                        mysql_result_tuple_after = db_after.query_mysql(mysql[2])
                        if mysql_result_tuple_after:
                            mysql_result_list_after = list(chain.from_iterable(mysql_result_tuple_after))
                            mysql_result_list_after = data_conversion_string(mysql_result_list_after)
                            logger.info("发起请求之后mysql查询的结果列表为：{}", mysql_result_list_after)
                            mysql_result_list_after = list(map(str, mysql_result_list_after))
                            # 把列表里面的元素类型全部转为str
            if pgsql:
                if pgsql[2]:
                    if "SELECT" in pgsql[2] or "select" in pgsql[2]:
                        pgsql_db_after = ConnectPostgreSQL()
                        pgsql_result_tuple_after = pgsql_db_after.query_postgresql(pgsql[2])
                        if pgsql_result_tuple_after:
                            pgsql_result_list_after = list(chain.from_iterable(pgsql_result_tuple_after))
                            logger.info("发起请求之后PostgreSQL查询的结果列表为：{}", pgsql_result_list_after)
                            pgsql_result_list_after = list(map(str, pgsql_result_list_after))
                            # 把列表里面的元素类型全部改为str
            if mongo:
                if mongo[2]:
                    mongo_db_after = ConnectMongo()
                    mongo_result_dict_after = mongo_db_after.query_mongo_one(mongo[2][0], *mongo[2][1])
                    if mongo_result_dict_after:
                        mongo_result_list_after = list(mongo_result_dict_after.values())
                        logger.info("发起请求之后mongo查询的结果列表为：{}", mongo_result_list_after)
                        mongo_result_list_after = list(map(str, mongo_result_list_after))
                        # 把列表里面的元素类型全部转为str

            if regular:
                # 如果正则不为空
                extract_list = []
                # 定义一个提取结果列表
                for i in regular["expression"]:
                    regular_result_list = re.findall(i, actual_result_text)
                    # re.findall(正则表达式, 实际的响应结果)返回一个符合规则的list，取第1个
                    if regular_result_list:
                        regular_result = regular_result_list[0]
                        extract_list.append(regular_result)
                        # 把提取结果添加到提取结果列表里面
                temporary_dict = dict(zip(regular["variable"], extract_list))
                # 把变量列表与提取结果列表转为一个临时字典
                for key, value in temporary_dict.items():
                    self.variable_result_dict[key] = value
                # 把临时字典合并到变量名与提取的结果字典，已去重
            else:
                pass

            if self.variable_result_dict:
                for key in list(self.variable_result_dict.keys()):
                    if not self.variable_result_dict[key]:
                        del self.variable_result_dict[key]
                # 删除变量名与提取的结果字典中为空的键值对

            expected_result = re.sub("{|}|\'|\"|\\[|\\]| ", "", json.dumps(expected_result, ensure_ascii=False))
            # 去除大括号{、}、单引号'、双引号"、中括号[、]与空格
            if actual_result_text:
                actual_result_text = re.sub("{|}|\'|\"|\\[|\\]| ", "", actual_result_text)
            expected_result_list = re.split(":|,", expected_result)
            # 把文本转为列表，并去除:与,
            actual_result_list = re.split(":|,", actual_result_text)
            logger.info("切割之后预期的响应结果列表为：{}", expected_result_list)
            if actual_result_list:
                logger.info("切割之后实际的响应结果列表为：{}", actual_result_list)

            boolean_expression = set(expected_result_list) <= set(actual_result_list)
            # 布尔表达式，判断是否是其子集
            if expected_time:
                boolean_expression = set(expected_result_list) <= set(
                    actual_result_list) and actual_time <= expected_time
            if mysql:
                if mysql[2]:
                    boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                        mysql_result_list_after) <= set(actual_result_list)
                if mysql[2] and expected_time:
                    boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                        mysql_result_list_after) <= set(actual_result_list) and actual_time <= expected_time
            if pgsql:
                if pgsql[2]:
                    boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                        pgsql_result_list_after) <= set(actual_result_list)
                if pgsql[2] and expected_time:
                    boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                        pgsql_result_list_after) <= set(actual_result_list) and actual_time <= expected_time
            if mongo:
                if mongo[2]:
                    boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                        mongo_result_list_after) <= set(actual_result_list)
                if mongo[2] and expected_time:
                    boolean_expression = set(expected_result_list) <= set(actual_result_list) and set(
                        mongo_result_list_after) <= set(actual_result_list) and actual_time <= expected_time
            # 多重断言
            # 预期的响应结果与实际的响应结果是被包含关系
            # 发起请求之后mysql查询结果与实际的响应结果是被包含关系
            # 发起请求之后pgsql查询结果与实际的响应结果是被包含关系
            # 发起请求之后mongo查询结果与实际的响应结果是被包含关系
            # 实际的响应时间应该小于或者等于预期的响应时间
            if expected_code == actual_code:
                if boolean_expression:
                    logger.info("{}>>>执行通过", step_name)
                else:
                    logger.error("{}>>>执行失败！！！", step_name)
                logger.info("##########步骤分隔符##########\n")
                self.assertTrue(boolean_expression)
            else:
                logger.error("{}>>>执行失败！！！", step_name)
                try:
                    self.assertEqual(expected_code, actual_code)
                except AssertionError as e:
                    logger.error("预期的响应代码与实际的响应代码不相等：{}", e)
                    logger.info("##########步骤分隔符##########\n")
                    raise e

        logger.info("**********{}>>>执行结束**********\n", case_name)

    @classmethod
    def tearDownClass(cls):
        """
        清理工作
        :return:
        """

        export_various_formats(cls.test_case_data_list)
        # 调用导出各种格式的测试用例的方法


if __name__ == '__main__':
    beautiful_report_run(DemoTest)
    # 调用BeautifulReport运行方式
