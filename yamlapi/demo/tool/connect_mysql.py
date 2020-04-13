import pymysql
from DBUtils.PooledDB import PooledDB

from setting.project_config import *


class ConnectMySQL(object):
    # 封装PyMySQL的增删改查

    def __init__(self):
        # 初始化
        try:
            self.pool = PooledDB(
                creator=pymysql,
                # 使用链接数据库的模块
                maxconnections=30,
                # 连接池允许的最大连接数，0和None表示不限制连接数
                mincached=2,
                # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                maxcached=5,
                # 链接池中最多闲置的链接，0和None不限制
                maxshared=5,
                # 链接池中最多共享的链接数量，0和None表示全部共享
                blocking=True,
                # 连接池中如果没有可用连接后，是否阻塞等待
                # True，等待；False，不等待然后报错
                maxusage=None,
                # 一个链接最多被重复使用的次数，None表示无限制
                setsession=[],
                # 开始会话前执行的命令列表
                # 如：["set datestyle to ...", "set time zone ..."]
                ping=0,
                # ping MySQL服务端，检查是否服务可用。
                # 如：0 = None = never
                # 1 = default = whenever it is requested
                # 2 = when a cursor is created
                # 4 = when a query is executed
                # 7 = always
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_database,
                charset='utf8',
                connect_timeout=20,
                read_timeout=20,
            )
            # 连接池配置
        except Exception as e:
            logger.error("初始化MySQL连接池发生错误：{}", e)
            raise e

    def query_mysql(self, sql_sentence):
        # 查询MySQL，参数为MySQL查询语句

        conn = self.pool.connection()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            results = cur.fetchall()
            # 获取查询的结果
            logger.info("mysql查询成功：{}", sql_sentence)
            logger.info("mysql查询的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql查询发生错误：{}", e)
            raise e
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接

        return results
        # 返回一个元组

    def insert_mysql(self, sql_sentence):
        # 插入MySQL，参数为MySQL插入语句

        conn = self.pool.connection()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            conn.commit()
            # 提交
            logger.info("mysql插入成功：{}", sql_sentence)
            logger.info("mysql插入的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql插入发生错误：{}", e)
            conn.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接

    def update_mysql(self, sql_sentence):
        # 更新MySQL，参数为MySQL更新语句

        conn = self.pool.connection()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            conn.commit()
            # 提交
            logger.info("mysql更新成功：{}", sql_sentence)
            logger.info("mysql更新的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql更新发生错误：{}", e)
            conn.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接

    def delete_mysql(self, sql_sentence):
        # 删除MySQL，参数为MySQL删除语句

        conn = self.pool.connection()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            conn.commit()
            # 提交
            logger.info("mysql删除成功：{}", sql_sentence)
            logger.info("mysql删除的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql删除发生错误：{}", e)
            conn.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接
