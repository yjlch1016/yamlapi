import datetime
import decimal


def data_conversion_string(mysql_result_list):
    # 数据类型转换的方法，参数为MySQL查询结果列表

    if mysql_result_list:
        for index in range(len(mysql_result_list)):
            if type(mysql_result_list[index]) == datetime.datetime:
                mysql_result_list[index] = mysql_result_list[index].strftime(
                    "%Y-%m-%d %H:%M:%S")
                # 把datetime.datetime转为str
            if type(mysql_result_list[index]) == decimal.Decimal:
                mysql_result_list[index] = str(
                    decimal.Decimal(mysql_result_list[index]).quantize(decimal.Decimal('0.00')))
                # 把decimal.Decimal转为str，保留两位小数

    return mysql_result_list
    # 返回替换后的MySQL查询结果列表
