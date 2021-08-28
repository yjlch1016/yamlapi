import redis

from setting.project_config import *


class ConnectRedis(object):
    # 封装redis-py的增删改查

    def __init__(self):
        # 初始化
        try:
            self.pool = redis.ConnectionPool(
                host=redis_host,
                port=redis_port,
                db=redis_database,
                password=redis_password,
                max_connections=20,
                decode_responses=True,
                encoding='utf-8',
                socket_connect_timeout=15,
                socket_timeout=15,
            )
            # 连接池配置
        except Exception as e:
            logger.error("初始化Redis连接池发生错误：{}", e)
            raise e

    def query_redis_one(self, key_name):
        """
        查询Redis，一条数据
        :param key_name: 键名
        :return:
        """

        conn = redis.StrictRedis(connection_pool=self.pool)
        # 打开redis连接

        try:
            result = conn.get(key_name)
            # 获取查询的结果
            if result:
                logger.info("redis查询一条数据成功")
            else:
                logger.error("redis查询一条数据失败：无数据返回")
        except Exception as e:
            logger.error("redis查询一条数据发生错误：{}", e)
            raise e

        return result
        # 返回查询结果


    def insert_redis_str_one(self, *args):
        """
        插入Redis，str类型，一条数据
        :param args:插入参数，列表格式
        :return:
        """

        conn = redis.StrictRedis(connection_pool=self.pool)
        # 打开redis连接

        try:
            result = conn.set(*args)
            # *表示把元组里面每个元素逐一传递进来
            if result:
                logger.info("redis插入一条str数据成功")
            else:
                logger.error("redis插入一条str数据失败")
        except Exception as e:
            logger.error("redis插入一条str数据发生错误：{}", e)

    def insert_redis_str_many(self, kvs):
        """
        插入Redis，str类型，多条数据
        :param kvs: 插入的键值对，字典格式
        :return:
        """

        conn = redis.StrictRedis(connection_pool=self.pool)
        # 打开redis连接

        try:
            result = conn.mset(kvs)
            if result:
                logger.info("redis插入多条str数据成功")
            else:
                logger.error("redis插入多条str数据失败")
        except Exception as e:
            logger.error("redis插入多条str数据发生错误：{}", e)

    def delete_redis(self, key):
        """
        删除Redis
        :param key: 参数为Redis键
        :return:
        """

        conn = redis.StrictRedis(connection_pool=self.pool)
        # 打开redis连接

        try:
            if conn.exists(key):
                # 如果键存在
                result = conn.delete(key)
                logger.info("redis删除成功，删除的个数为：{}", result)
            else:
                logger.error("redis删除发生错误：键{}不存在", key)
        except Exception as e:
            logger.error("redis删除发生错误：{}", e)
