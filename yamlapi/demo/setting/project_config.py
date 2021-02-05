"""
整个工程的配置文件
"""

import os
import sys
import time

import requests
from loguru import logger

current_path = os.path.dirname(os.path.dirname(__file__))
# 获取当前目录的父目录的绝对路径
# 也就是整个工程的根目录
case_path = os.path.join(current_path, "case")
# 测试用例的目录
yaml_path = os.path.join(current_path, "resource")
# yaml文件的目录
today = time.strftime("%Y-%m-%d", time.localtime())
# 年月日


report_log_path = os.path.join(current_path, "report_log")
# 测试报告和日志的目录
if os.path.exists(report_log_path):
    pass
else:
    os.mkdir(report_log_path, mode=0o777)

logging_file = os.path.join(report_log_path, "log{}.log".format(today))

logger.add(
    logging_file,
    format="{time:YYYY-MM-DD HH:mm:ss}|{level}|{message}",
    level="INFO",
    rotation="100 MB",
    encoding="utf-8",
)


# loguru日志配置


def read_apollo_config_center(config_server_url):
    # 读取Apollo配置中心

    url = config_server_url + "/configfiles/json/DemoAppId/default/application"
    # 通过带缓存的Http接口从Apollo读取配置
    # 参考文档：https://ctripcorp.github.io/apollo/#/zh/usage/other-language-client-user-guide

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


parameter = sys.argv[1]
# 从命令行获取参数
if "--cmd=" in parameter:
    parameter = parameter.replace("--cmd=", "")
else:
    pass

environment = os.getenv("measured_environment", parameter)
# 环境变量

setting_config_type = "apollo"
# setting配置类型：apollo或者local
# 使用Apollo配置中心或者本地配置文件，不可混用，只能选取一种


if setting_config_type == "apollo":
    if environment == "dev":

        apollo_config_dict = read_apollo_config_center("http://dev.apollo.com")
        # 传入开发环境的Apollo配置域名

        test_scenario = apollo_config_dict["test_scenario"]
        test_story = apollo_config_dict["test_story"]
        test_case_priority = apollo_config_dict["test_case_priority"]
        test_case_address = apollo_config_dict["test_case_address"]
        test_case_address_title = apollo_config_dict["test_case_address_title"]
        # allure配置

        beautiful_filename = apollo_config_dict["beautiful_filename"]
        beautiful_description = apollo_config_dict["beautiful_description"]
        # BeautifulReport配置

        html_report_title = apollo_config_dict["html_report_title"]
        project_name = apollo_config_dict["project_name"]
        swagger_address = apollo_config_dict["swagger_address"]
        test_department = apollo_config_dict["test_department"]
        tester = apollo_config_dict["tester"]
        # conftest配置

        test_case_format = apollo_config_dict["test_case_format"]
        # 测试用例的格式：yaml或者json
        # 不可混用，只能选取一种格式
        first_test_case_file = apollo_config_dict["first_test_case_file"]
        # 第一个测试用例文件

        robot = apollo_config_dict["robot"]
        # 机器人：feishu、dingtalk或者为空
        # 不可混用，只能选取一种

        feishu_webhook = apollo_config_dict["feishu_webhook"]
        # 飞书机器人webhook
        feishu_secret = apollo_config_dict["feishu_secret"]
        # 飞书机器人密钥
        card_header_title_content = apollo_config_dict["card_header_title_content"]
        # 飞书消息卡片标题
        card_elements_actions_text_content = apollo_config_dict["card_elements_actions_text_content"]
        # 飞书消息卡片跳转链接文字
        card_elements_actions_url = apollo_config_dict["card_elements_actions_url"]
        # 飞书消息卡片跳转链接

        dingtalk_webhook = apollo_config_dict["dingtalk_webhook"]
        # 钉钉机器人webhook
        dingtalk_secret = apollo_config_dict["dingtalk_secret"]
        # 钉钉机器人密钥

        service_domain = apollo_config_dict["service_domain"]
        # 开发环境接口域名

        db_host = apollo_config_dict["db_host"]
        db_port = apollo_config_dict["db_port"]
        db_user = apollo_config_dict["db_user"]
        db_password = apollo_config_dict["db_password"]
        db_database = apollo_config_dict["db_database"]
        # 开发环境MySQL数据库配置

        pgsql_host = apollo_config_dict["pgsql_host"]
        pgsql_port = apollo_config_dict["pgsql_port"]
        pgsql_user = apollo_config_dict["pgsql_user"]
        pgsql_password = apollo_config_dict["pgsql_password"]
        pgsql_database = apollo_config_dict["pgsql_database"]
        # 开发环境PgSQL数据库配置

        mongo_host = apollo_config_dict["mongo_host"]
        mongo_port = apollo_config_dict["mongo_port"]
        mongo_database = apollo_config_dict["mongo_database"]
        mongo_user = apollo_config_dict["mongo_user"]
        mongo_password = apollo_config_dict["mongo_password"]
        # 开发环境MongoDB数据库配置

        influxdb_switch = apollo_config_dict["influxdb_switch"]
        # 是否插入到influxDB, true或者为空
        # 不可混用，只能选取一种
        influxdb_host = apollo_config_dict["influxdb_host"]
        influxdb_port = apollo_config_dict["influxdb_port"]
        influxdb_database = apollo_config_dict["influxdb_database"]
        influxdb_user = apollo_config_dict["influxdb_user"]
        influxdb_password = apollo_config_dict["influxdb_password"]
        influxdb_measurement = apollo_config_dict["influxdb_measurement"]
        # influxDB数据库配置

    elif environment == "test":

        apollo_config_dict = read_apollo_config_center("http://test.apollo.com")
        # 传入测试环境的Apollo配置域名

        test_scenario = apollo_config_dict["test_scenario"]
        test_story = apollo_config_dict["test_story"]
        test_case_priority = apollo_config_dict["test_case_priority"]
        test_case_address = apollo_config_dict["test_case_address"]
        test_case_address_title = apollo_config_dict["test_case_address_title"]
        # allure配置

        beautiful_filename = apollo_config_dict["beautiful_filename"]
        beautiful_description = apollo_config_dict["beautiful_description"]
        # BeautifulReport配置

        html_report_title = apollo_config_dict["html_report_title"]
        project_name = apollo_config_dict["project_name"]
        swagger_address = apollo_config_dict["swagger_address"]
        test_department = apollo_config_dict["test_department"]
        tester = apollo_config_dict["tester"]
        # conftest配置

        test_case_format = apollo_config_dict["test_case_format"]
        # 测试用例的格式：yaml或者json
        # 不可混用，只能选取一种格式
        first_test_case_file = apollo_config_dict["first_test_case_file"]
        # 第一个测试用例文件

        robot = apollo_config_dict["robot"]
        # 机器人：feishu、dingtalk或者为空
        # 不可混用，只能选取一种

        feishu_webhook = apollo_config_dict["feishu_webhook"]
        # 飞书机器人webhook
        feishu_secret = apollo_config_dict["feishu_secret"]
        # 飞书机器人密钥
        card_header_title_content = apollo_config_dict["card_header_title_content"]
        # 飞书消息卡片标题
        card_elements_actions_text_content = apollo_config_dict["card_elements_actions_text_content"]
        # 飞书消息卡片跳转链接文字
        card_elements_actions_url = apollo_config_dict["card_elements_actions_url"]
        # 飞书消息卡片跳转链接

        dingtalk_webhook = apollo_config_dict["dingtalk_webhook"]
        # 钉钉机器人webhook
        dingtalk_secret = apollo_config_dict["dingtalk_secret"]
        # 钉钉机器人密钥

        service_domain = apollo_config_dict["service_domain"]
        # 测试环境接口域名

        db_host = apollo_config_dict["db_host"]
        db_port = apollo_config_dict["db_port"]
        db_user = apollo_config_dict["db_user"]
        db_password = apollo_config_dict["db_password"]
        db_database = apollo_config_dict["db_database"]
        # 测试环境MySQL数据库配置

        pgsql_host = apollo_config_dict["pgsql_host"]
        pgsql_port = apollo_config_dict["pgsql_port"]
        pgsql_user = apollo_config_dict["pgsql_user"]
        pgsql_password = apollo_config_dict["pgsql_password"]
        pgsql_database = apollo_config_dict["pgsql_database"]
        # 测试环境PgSQL数据库配置

        mongo_host = apollo_config_dict["mongo_host"]
        mongo_port = apollo_config_dict["mongo_port"]
        mongo_database = apollo_config_dict["mongo_database"]
        mongo_user = apollo_config_dict["mongo_user"]
        mongo_password = apollo_config_dict["mongo_password"]
        # 测试环境MongoDB数据库配置

        influxdb_switch = apollo_config_dict["influxdb_switch"]
        # 是否插入到influxDB, true或者为空
        # 不可混用，只能选取一种
        influxdb_host = apollo_config_dict["influxdb_host"]
        influxdb_port = apollo_config_dict["influxdb_port"]
        influxdb_database = apollo_config_dict["influxdb_database"]
        influxdb_user = apollo_config_dict["influxdb_user"]
        influxdb_password = apollo_config_dict["influxdb_password"]
        influxdb_measurement = apollo_config_dict["influxdb_measurement"]
        # influxDB数据库配置

    elif environment == "pre":

        apollo_config_dict = read_apollo_config_center("http://pro.apollo.com")
        # 传入预生产环境的Apollo配置域名

        test_scenario = apollo_config_dict["test_scenario"]
        test_story = apollo_config_dict["test_story"]
        test_case_priority = apollo_config_dict["test_case_priority"]
        test_case_address = apollo_config_dict["test_case_address"]
        test_case_address_title = apollo_config_dict["test_case_address_title"]
        # allure配置

        beautiful_filename = apollo_config_dict["beautiful_filename"]
        beautiful_description = apollo_config_dict["beautiful_description"]
        # BeautifulReport配置

        html_report_title = apollo_config_dict["html_report_title"]
        project_name = apollo_config_dict["project_name"]
        swagger_address = apollo_config_dict["swagger_address"]
        test_department = apollo_config_dict["test_department"]
        tester = apollo_config_dict["tester"]
        # conftest配置

        test_case_format = apollo_config_dict["test_case_format"]
        # 测试用例的格式：yaml或者json
        # 不可混用，只能选取一种格式
        first_test_case_file = apollo_config_dict["first_test_case_file"]
        # 第一个测试用例文件

        robot = apollo_config_dict["robot"]
        # 机器人：feishu、dingtalk或者为空
        # 不可混用，只能选取一种

        feishu_webhook = apollo_config_dict["feishu_webhook"]
        # 飞书机器人webhook
        feishu_secret = apollo_config_dict["feishu_secret"]
        # 飞书机器人密钥
        card_header_title_content = apollo_config_dict["card_header_title_content"]
        # 飞书消息卡片标题
        card_elements_actions_text_content = apollo_config_dict["card_elements_actions_text_content"]
        # 飞书消息卡片跳转链接文字
        card_elements_actions_url = apollo_config_dict["card_elements_actions_url"]
        # 飞书消息卡片跳转链接

        dingtalk_webhook = apollo_config_dict["dingtalk_webhook"]
        # 钉钉机器人webhook
        dingtalk_secret = apollo_config_dict["dingtalk_secret"]
        # 钉钉机器人密钥

        service_domain = apollo_config_dict["service_domain"]
        # 预生产环境接口域名

        db_host = apollo_config_dict["db_host"]
        db_port = apollo_config_dict["db_port"]
        db_user = apollo_config_dict["db_user"]
        db_password = apollo_config_dict["db_password"]
        db_database = apollo_config_dict["db_database"]
        # 预生产环境MySQL数据库配置

        pgsql_host = apollo_config_dict["pgsql_host"]
        pgsql_port = apollo_config_dict["pgsql_port"]
        pgsql_user = apollo_config_dict["pgsql_user"]
        pgsql_password = apollo_config_dict["pgsql_password"]
        pgsql_database = apollo_config_dict["pgsql_database"]
        # 预生产环境PgSQL数据库配置

        mongo_host = apollo_config_dict["mongo_host"]
        mongo_port = apollo_config_dict["mongo_port"]
        mongo_database = apollo_config_dict["mongo_database"]
        mongo_user = apollo_config_dict["mongo_user"]
        mongo_password = apollo_config_dict["mongo_password"]
        # 预生产环境MongoDB数据库配置

        influxdb_switch = apollo_config_dict["influxdb_switch"]
        # 是否插入到influxDB, true或者为空
        # 不可混用，只能选取一种
        influxdb_host = apollo_config_dict["influxdb_host"]
        influxdb_port = apollo_config_dict["influxdb_port"]
        influxdb_database = apollo_config_dict["influxdb_database"]
        influxdb_user = apollo_config_dict["influxdb_user"]
        influxdb_password = apollo_config_dict["influxdb_password"]
        influxdb_measurement = apollo_config_dict["influxdb_measurement"]
        # influxDB数据库配置

    elif environment == "formal":

        apollo_config_dict = read_apollo_config_center("https://formal.apollo.com")
        # 传入生产环境的Apollo配置域名

        test_scenario = apollo_config_dict["test_scenario"]
        test_story = apollo_config_dict["test_story"]
        test_case_priority = apollo_config_dict["test_case_priority"]
        test_case_address = apollo_config_dict["test_case_address"]
        test_case_address_title = apollo_config_dict["test_case_address_title"]
        # allure配置

        beautiful_filename = apollo_config_dict["beautiful_filename"]
        beautiful_description = apollo_config_dict["beautiful_description"]
        # BeautifulReport配置

        html_report_title = apollo_config_dict["html_report_title"]
        project_name = apollo_config_dict["project_name"]
        swagger_address = apollo_config_dict["swagger_address"]
        test_department = apollo_config_dict["test_department"]
        tester = apollo_config_dict["tester"]
        # conftest配置

        test_case_format = apollo_config_dict["test_case_format"]
        # 测试用例的格式：yaml或者json
        # 不可混用，只能选取一种格式
        first_test_case_file = apollo_config_dict["first_test_case_file"]
        # 第一个测试用例文件

        robot = apollo_config_dict["robot"]
        # 机器人：feishu、dingtalk或者为空
        # 不可混用，只能选取一种

        feishu_webhook = apollo_config_dict["feishu_webhook"]
        # 飞书机器人webhook
        feishu_secret = apollo_config_dict["feishu_secret"]
        # 飞书机器人密钥
        card_header_title_content = apollo_config_dict["card_header_title_content"]
        # 飞书消息卡片标题
        card_elements_actions_text_content = apollo_config_dict["card_elements_actions_text_content"]
        # 飞书消息卡片跳转链接文字
        card_elements_actions_url = apollo_config_dict["card_elements_actions_url"]
        # 飞书消息卡片跳转链接

        dingtalk_webhook = apollo_config_dict["dingtalk_webhook"]
        # 钉钉机器人webhook
        dingtalk_secret = apollo_config_dict["dingtalk_secret"]
        # 钉钉机器人密钥

        service_domain = apollo_config_dict["service_domain"]
        # 生产环境接口域名

        db_host = apollo_config_dict["db_host"]
        db_port = apollo_config_dict["db_port"]
        db_user = apollo_config_dict["db_user"]
        db_password = apollo_config_dict["db_password"]
        db_database = apollo_config_dict["db_database"]
        # 生产环境MySQL数据库配置

        pgsql_host = apollo_config_dict["pgsql_host"]
        pgsql_port = apollo_config_dict["pgsql_port"]
        pgsql_user = apollo_config_dict["pgsql_user"]
        pgsql_password = apollo_config_dict["pgsql_password"]
        pgsql_database = apollo_config_dict["pgsql_database"]
        # 生产环境PgSQL数据库配置

        mongo_host = apollo_config_dict["mongo_host"]
        mongo_port = apollo_config_dict["mongo_port"]
        mongo_database = apollo_config_dict["mongo_database"]
        mongo_user = apollo_config_dict["mongo_user"]
        mongo_password = apollo_config_dict["mongo_password"]
        # 生产环境MongoDB数据库配置

        influxdb_switch = apollo_config_dict["influxdb_switch"]
        # 是否插入到influxDB, true或者为空
        # 不可混用，只能选取一种
        influxdb_host = apollo_config_dict["influxdb_host"]
        influxdb_port = apollo_config_dict["influxdb_port"]
        influxdb_database = apollo_config_dict["influxdb_database"]
        influxdb_user = apollo_config_dict["influxdb_user"]
        influxdb_password = apollo_config_dict["influxdb_password"]
        influxdb_measurement = apollo_config_dict["influxdb_measurement"]
        # influxDB数据库配置

if setting_config_type == "local":

    test_scenario = "测试场景：XXX接口测试"
    test_story = "测试故事：XXX接口测试"
    test_case_priority = "critical"
    test_case_address = "http://www.testcase.com"
    test_case_address_title = "XXX接口测试用例地址"
    # allure配置

    beautiful_filename = "xxx_report"
    beautiful_description = "XXX接口测试报告"
    # BeautifulReport配置

    html_report_title = "XXX接口测试报告"
    project_name = "XXX接口自动化测试"
    swagger_address = "http://www.swagger.com/swagger-ui.html"
    test_department = "测试部门："
    tester = "测试人员："
    # conftest配置

    test_case_format = "yaml"
    # 测试用例的格式：yaml或者json
    # 不可混用，只能选取一种格式
    first_test_case_file = "demo_one.yaml"
    # 第一个测试用例文件

    robot = "feishu"
    # 机器人：feishu、dingtalk或者为空
    # 不可混用，只能选取一种

    feishu_webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/XXXXXX"
    # 飞书机器人webhook
    feishu_secret = "abcdefghij1234567890"
    # 飞书机器人密钥
    card_header_title_content = "飞书消息卡片标题"
    # 飞书消息卡片标题
    card_elements_actions_text_content = "飞书消息卡片跳转链接文字"
    # 飞书消息卡片跳转链接文字
    card_elements_actions_url = "https://demo.fesihu.com"
    # 飞书消息卡片跳转链接

    dingtalk_webhook = "https://oapi.dingtalk.com/robot/send?access_token=XXXXXX"
    # 钉钉机器人webhook
    dingtalk_secret = "1234567890abcdefghij"
    # 钉钉机器人密钥

    influxdb_switch = "true"
    # 是否插入到influxDB, true或者为空
    # 不可混用，只能选取一种
    influxdb_host = "www.influxdb.com"
    influxdb_port = 8086
    influxdb_database = "influxdb_database"
    influxdb_user = "root"
    influxdb_password = "123456"
    influxdb_measurement = "influxdb_measurement"
    # InfluxDB数据库配置

    if environment == "dev":
        service_domain = "http://www.dev.com"
        # 开发环境接口域名

        db_host = 'mysql.dev.com'
        db_port = 3306
        db_user = 'root'
        db_password = '123456'
        db_database = ''
        # 开发环境MySQL数据库配置

        pgsql_host = 'pgsql.dev.com'
        pgsql_port = 5432
        pgsql_user = 'root'
        pgsql_password = '123456'
        pgsql_database = 'pgsql_db_1'
        # 开发环境PgSQL数据库配置

        mongo_host = "mongo.dev.com"
        mongo_port = "27017"
        mongo_database = "mongo_db_1"
        mongo_user = "root"
        mongo_password = "123456"
        # 开发环境MongoDB数据库配置

    elif environment == "test":
        service_domain = "http://www.test.com"
        # 测试环境接口域名

        db_host = 'mysql.test.com'
        db_port = 3307
        db_user = 'root'
        db_password = '123456'
        db_database = ''
        # 测试环境MySQL数据库配置

        pgsql_host = 'pgsql.test.com'
        pgsql_port = 5432
        pgsql_user = 'root'
        pgsql_password = '123456'
        pgsql_database = 'pgsql_db_1'
        # 测试环境PgSQL数据库配置

        mongo_host = "mongo.test.com"
        mongo_port = "27017"
        mongo_database = "mongo_db_1"
        mongo_user = "root"
        mongo_password = "123456"
        # 测试环境MongoDB数据库配置

    elif environment == "pre":
        service_domain = "http://www.pre.com"
        # 预生产环境接口域名

        db_host = 'mysql.pre.com'
        db_port = 3308
        db_user = 'root'
        db_password = '123456'
        db_database = ''
        # 预生产环境MySQL数据库配置

        pgsql_host = 'pgsql.pre.com'
        pgsql_port = 5432
        pgsql_user = 'root'
        pgsql_password = '123456'
        pgsql_database = 'pgsql_db_1'
        # 预生产环境PgSQL数据库配置

        mongo_host = "mongo.pre.com"
        mongo_port = "27017"
        mongo_database = "mongo_db_1"
        mongo_user = "root"
        mongo_password = "123456"
        # 预生产环境MongoDB数据库配置

    elif environment == "formal":
        service_domain = "https://www.formal.com"
        # 生产环境接口域名

        db_host = None
        db_port = None
        db_user = None
        db_password = None
        db_database = None
        # 生产环境MySQL数据库配置

        pgsql_host = None
        pgsql_port = None
        pgsql_user = None
        pgsql_password = None
        pgsql_database = None
        # 生产环境PgSQL数据库配置

        mongo_host = None
        mongo_port = None
        mongo_database = None
        mongo_user = None
        mongo_password = None
        # 生产环境MongoDB数据库配置
