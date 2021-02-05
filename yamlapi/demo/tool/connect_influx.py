from datetime import datetime

from influxdb import InfluxDBClient

from setting.project_config import *


class ConnectInflux(object):
    # 封装InfluxDB的增删改查

    def __init__(self):
        # 初始化
        try:
            self.client = InfluxDBClient(
                host=influxdb_host,
                port=influxdb_port,
                username=influxdb_user,
                password=influxdb_password,
                database=influxdb_database,
                timeout=20)
        except Exception as e:
            logger.error("初始化InfluxDB连接池发生错误：{}", e)
            raise e

    def insert_influx_one(self, environment, case_name, step_name, url, actual_time, actual_code):
        """
        插入InfluxDB，一条数据
        :param environment: 环境
        :param case_name: 用例名称
        :param step_name: 步骤名称
        :param url: 接口地址
        :param actual_time: 实际的响应时间
        :param actual_code: 实际的响应代码
        :return:
        """

        time_key = datetime.utcnow().isoformat("T")
        try:
            points = [
                {
                    "measurement": influxdb_measurement,
                    "tags": {
                        "environment": environment,
                        "case_name": case_name,
                        "step_name": step_name,
                        "url": url
                    },
                    "time": time_key,
                    "fields": {
                        "actual_time": actual_time,
                        "actual_code": actual_code
                    }
                }
            ]

            result = self.client.write_points(points)
            if result:
                logger.info("InfluxDB插入一条数据成功")
            else:
                logger.error("InfluxDB插入一条数据失败")
        except Exception as e:
            logger.error("InfluxDB插入一条数据发生错误：{}", e)
        finally:
            self.client.close()
            # 断开数据库连接
