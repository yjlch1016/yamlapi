from psycopg2.pool import SimpleConnectionPool

from setting.project_config import *


class ConnectPostgreSQL(object):
    # 封装PostgreSQL的增删改查

    def __init__(self):
        # 初始化
        try:
            self.pool = SimpleConnectionPool(
                host=pgsql_host,
                port=pgsql_port,
                user=pgsql_user,
                password=pgsql_password,
                database=pgsql_database,
                connect_timeout=20,
                client_encoding="UTF-8",
                minconn=2,
                maxconn=30
            )
            # 连接池配置
        except Exception as e:
            logger.error("初始化PostgreSQL连接池发生错误：{}", e)
            raise e

    def query_postgresql(self, sql_sentence):
        # 查询PostgreSQL，参数为PostgreSQL查询语句

        conn = self.pool.getconn()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            results = cur.fetchall()
            # 获取查询的结果
            logger.info("PostgreSQL查询成功：{}", sql_sentence)
            logger.info("PostgreSQL查询的数据量为：{}", cur.rowcount)
        except Exception as e:
            logger.error("PostgreSQL查询发生错误：{}", e)
            raise e
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接

        return results
        # 返回一个元组

    def insert_postgresql(self, sql_sentence):
        # 插入PostgreSQL，参数为PostgreSQL插入语句

        conn = self.pool.getconn()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            conn.commit()
            # 提交
            logger.info("PostgreSQL插入成功：{}", sql_sentence)
            logger.info("PostgreSQL插入的数据量为：{}", cur.rowcount)
        except Exception as e:
            logger.error("PostgreSQL插入发生错误：{}", e)
            conn.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接

    def update_postgresql(self, sql_sentence):
        # 更新PostgreSQL，参数为PostgreSQL更新语句

        conn = self.pool.getconn()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            conn.commit()
            # 提交
            logger.info("PostgreSQL更新成功：{}", sql_sentence)
            logger.info("PostgreSQL更新的数据量为：{}", cur.rowcount)
        except Exception as e:
            logger.error("PostgreSQL更新发生错误：{}", e)
            conn.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接

    def delete_postgresql(self, sql_sentence):
        # 删除PostgreSQL，参数为PostgreSQL删除语句

        conn = self.pool.getconn()
        # 打开数据库连接
        cur = conn.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            conn.commit()
            # 提交
            logger.info("PostgreSQL删除成功：{}", sql_sentence)
            logger.info("PostgreSQL删除的数据量为：{}", cur.rowcount)
        except Exception as e:
            logger.error("PostgreSQL删除发生错误：{}", e)
            conn.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            conn.close()
            # 断开数据库连接
