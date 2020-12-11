import re

from tool.create_random import create_random_number, create_random_letters, \
    create_random_mobile_phone, create_random_datetime


def function_dollar(field, variable_list):
    """
    替换${变量名}的方法
    :param field: 第一个参数是yaml文件里面定义的字段
    :param variable_list: 第二个参数是变量列表
    :return:
    """

    if "${" in field:
        for key, value in variable_list:
            field = field.replace("${" + key + "}", value)
            # replace(old, new)把字符串中的旧字符串替换成正则表达式提取的值
    else:
        pass

    return field
    # 返回替换后的字段


def function_rn(field):
    """
    替换RN随机数字的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__RN" in field:
        digit_list = re.findall("{__RN(.+?)}", field)
        # 获取位数列表
        for i in digit_list:
            random_number = create_random_number(int(i))
            # 调用生成随机数字的方法
            field = field.replace("{__RN" + i + "}", random_number)
    else:
        pass

    return field
    # 返回替换后的字段


def function_rl(field):
    """
    替换RL随机字母的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__RL" in field:
        digit_list = re.findall("{__RL(.+?)}", field)
        # 获取位数列表
        for i in digit_list:
            random_number = create_random_letters(int(i))
            # 调用生成随机数字的方法
            field = field.replace("{__RL" + i + "}", random_number)
    else:
        pass

    return field
    # 返回替换后的字段


def function_mp(field):
    """
    替换MP随机手机号码的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__MP" in field:
        random_mobile_phone = create_random_mobile_phone()
        # 调用生成随机手机号码的方法
        field = field.replace("{__MP}", random_mobile_phone)
    else:
        pass

    return field
    # 返回替换后的字段


def function_rd(field):
    """
    替换RD随机日期时间的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__RD" in field:
        digit_list = re.findall("{__RD(.+?)}", field)
        # 获取年份列表
        for i in digit_list:
            i_split = i.split(",")
            random_datetime = create_random_datetime(i_split[0], i_split[1])
            # 调用生成随机日期时间的方法
            field = field.replace("{__RD" + i + "}", random_datetime)
    else:
        pass

    return field
    # 返回替换后的字段


def function_sql(field, mysql_result_list):
    """
    替换MySQL查询结果的方法
    :param field: 第一个参数是yaml文件里面定义的字段
    :param mysql_result_list: 第二个参数是MySQL查询结果列表
    :return:
    """

    if "{__SQL" in field:
        mysql_index_list = re.findall("{__SQL(.+?)}", field)
        # 获取索引列表
        for i in mysql_index_list:
            mysql_value = mysql_result_list[int(i)]
            if type(mysql_value) != str:
                mysql_value = str(mysql_value)
            field = field.replace("{__SQL" + i + "}", mysql_value)
    else:
        pass

    return field
    # 返回替换后的字段


def function_pgsql(field, pgsql_result_list):
    """
    替换PgSQL查询结果的方法
    :param field: 第一个参数是yaml文件里面定义的字段
    :param pgsql_result_list: 第二个参数是PgSQL查询结果列表
    :return:
    """

    if "{__PGSQL" in field:
        pgsql_index_list = re.findall("{__PGSQL(.+?)}", field)
        # 获取索引列表
        for i in pgsql_index_list:
            pgsql_value = pgsql_result_list[int(i)]
            if type(pgsql_value) != str:
                pgsql_value = str(pgsql_value)
            field = field.replace("{__PGSQL" + i + "}", pgsql_value)
    else:
        pass

    return field
    # 返回替换后的字段


def function_mongo(field, mongo_result_list):
    """
    替换Mongo查询结果的方法
    :param field: 第一个参数是yaml文件里面定义的字段
    :param mongo_result_list: 第二个参数是Mongo查询结果列表
    :return:
    """

    if "{__MONGO" in field:
        mongo_index_list = re.findall("{__MONGO(.+?)}", field)
        # 获取索引列表
        for i in mongo_index_list:
            mongo_value = mongo_result_list[int(i)]
            if type(mongo_value) != str:
                mongo_value = str(mongo_value)
            field = field.replace("{__MONGO" + i + "}", mongo_value)
    else:
        pass

    return field
    # 返回替换后的字段
