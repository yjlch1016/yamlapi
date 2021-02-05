import pymongo

from setting.project_config import *


class ConnectMongo(object):
    # 封装pymongo的增删改查

    def __init__(self):
        # 初始化
        try:
            mongo_url = "mongodb://{}:{}@{}:{}/?authSource={}".format(
                mongo_user, mongo_password, mongo_host, mongo_port, mongo_database)
            # 连接池配置
            self.conn = pymongo.MongoClient(mongo_url)
            self.db = self.conn[mongo_database]
        except Exception as e:
            logger.error("初始化Mongo连接池发生错误：{}", e)
            raise e

    def query_mongo_one(self, collection_name, *args):
        """
        查询Mongo，一条数据
        :param collection_name: 集合名
        :param args: 查询参数，参数个数不限
        :return:
        """

        try:
            coll = self.db[collection_name]
            result = coll.find_one(*args)
            # *表示把元组里面每个元素逐一传递进来
            # 获取查询的结果
            if result:
                logger.info("mongo查询一条数据成功")
            else:
                logger.error("mongo查询一条数据失败：无数据返回")
        except Exception as e:
            logger.error("mongo查询一条数据发生错误：{}", e)
            raise e
        finally:
            self.conn.close()
            # 断开数据库连接

        return result
        # 返回查询结果

    def insert_mongo_one(self, collection_name, *args):
        """
        插入Mongo，一条数据
        :param collection_name: 集合名
        :param args: 插入参数，参数个数不限
        :return:
        """

        try:
            coll = self.db[collection_name]
            result = coll.insert_one(*args)
            # *表示把元组里面每个元素逐一传递进来
            if result:
                logger.info("mongo插入一条数据成功，id为：{}", result.inserted_id)
            else:
                logger.error("mongo插入一条数据失败")
        except Exception as e:
            logger.error("mongo插入一条数据发生错误：{}", e)
            raise e
        finally:
            self.conn.close()
            # 断开数据库连接

    def insert_mongo_many(self, collection_name, *args):
        """
        插入Mongo，多条数据
        :param collection_name: 集合名
        :param args: 插入参数，参数个数不限
        :return:
        """

        try:
            coll = self.db[collection_name]
            result = coll.insert_many(*args)
            # *表示把元组里面每个元素逐一传递进来
            if result:
                logger.info("mongo插入多条数据成功，ids为：{}", result.inserted_ids)
            else:
                logger.error("mongo插入多条数据失败")
        except Exception as e:
            logger.error("mongo插入多条数据发生错误：{}", e)
            raise e
        finally:
            self.conn.close()
            # 断开数据库连接

    def update_mongo_one(self, collection_name, *args):
        """
        更新Mongo，一条数据
        :param collection_name: 集合名
        :param args: 更新参数，参数个数不限
        :return:
        """

        try:
            coll = self.db[collection_name]
            result = coll.update_one(*args)
            # *表示把元组里面每个元素逐一传递进来
            if result:
                logger.info(
                    "mongo更新一条数据成功，匹配的数据条数为：{}，影响的数据条数为：{}",
                    result.matched_count, result.modified_count)
            else:
                logger.error("mongo更新一条数据失败")
        except Exception as e:
            logger.error("mongo更新一条数据发生错误：{}", e)
            raise e
        finally:
            self.conn.close()
            # 断开数据库连接

    def delete_mongo_one(self, collection_name, *args):
        """
        删除Mongo，一条数据
        :param collection_name: 集合名
        :param args: 删除参数，参数个数不限
        :return:
        """

        try:
            coll = self.db[collection_name]
            result = coll.delete_one(*args)
            # *表示把元组里面每个元素逐一传递进来
            if result:
                logger.info("mongo删除一条数据成功，删除的数据条数为：{}", result.deleted_count)
            else:
                logger.error("mongo删除一条数据失败")
        except Exception as e:
            logger.error("mongo删除一条数据发生错误：{}", e)
            raise e
        finally:
            self.conn.close()
            # 断开数据库连接
