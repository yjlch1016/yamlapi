from pymysql import connect

from setting.project_config import *


class ConnectMySQL(object):
    # 封装PyMySQL的增删改查

    def __init__(self):
        # 初始化
        self.host = db_host
        self.user = db_user
        self.password = db_password
        self.db = db_database
        self.port = db_port
        self.connect_timeout = 20
        self.read_timeout = 20
        self.charset = "utf8"

    def query_mysql(self, sql_sentence):
        # 查询MySQL，参数为MySQL查询语句

        db = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            port=self.port,
            connect_timeout=self.connect_timeout,
            read_timeout=self.read_timeout,
            charset=self.charset)
        # 打开数据库连接

        cur = db.cursor()
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
            db.close()
            # 断开数据库连接

        return results
        # 返回一个元组

    def insert_mysql(self, sql_sentence):
        # 插入MySQL，参数为MySQL插入语句

        db = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            port=self.port,
            connect_timeout=self.connect_timeout,
            read_timeout=self.read_timeout,
            charset=self.charset)
        # 打开数据库连接

        cur = db.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            db.commit()
            # 提交
            logger.info("mysql插入成功：{}", sql_sentence)
            logger.info("mysql插入的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql插入发生错误：{}", e)
            db.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            db.close()
            # 断开数据库连接

    def update_mysql(self, sql_sentence):
        # 更新MySQL，参数为MySQL更新语句

        db = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            port=self.port,
            connect_timeout=self.connect_timeout,
            read_timeout=self.read_timeout,
            charset=self.charset)
        # 打开数据库连接

        cur = db.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            db.commit()
            # 提交
            logger.info("mysql更新成功：{}", sql_sentence)
            logger.info("mysql更新的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql更新发生错误：{}", e)
            db.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            db.close()
            # 断开数据库连接

    def delete_mysql(self, sql_sentence):
        # 删除MySQL，参数为MySQL删除语句

        db = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            port=self.port,
            connect_timeout=self.connect_timeout,
            read_timeout=self.read_timeout,
            charset=self.charset)
        # 打开数据库连接

        cur = db.cursor()
        # 使用cursor()方法获取操作游标

        try:
            cur.execute(sql_sentence)
            # 执行sql语句
            db.commit()
            # 提交
            logger.info("mysql删除成功：{}", sql_sentence)
            logger.info("mysql删除的数据量为：{}", cur.execute(sql_sentence))
        except Exception as e:
            logger.error("mysql删除发生错误：{}", e)
            db.rollback()
            # 回滚
        finally:
            cur.close()
            # 关闭游标
            db.close()
            # 断开数据库连接
