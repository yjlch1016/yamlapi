import re

from tool.create_random import create_random_number, create_random_letters, create_random_mobile_phone


def function_dollar(field, variable_list):
    # 替换$的方法，第一个参数是yaml文件里面定义的字段，第二个参数是变量列表

    if "{$" in field:
        for key, value in variable_list:
            field = field.replace("{" + key + "}", value)
            # replace(old, new)把字符串中的旧字符串替换成正则表达式提取的值
        field = re.sub("\\$", "", field)
        # re.sub(old, new, 源字符串)默认全部替换
        # 如果遇到带有转义的字符被当作特殊字符时，使用双反斜杠\\来转义，或者在引号前面加r
    else:
        pass

    return field
    # 返回替换后的字段


def function_rn(field):
    # 替换RN随机数字的方法，参数为yaml文件里面定义的字段

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
    # 替换RL随机字母的方法，参数为yaml文件里面定义的字段

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
    # 替换MP随机手机号码的方法，参数为yaml文件里面定义的字段

    if "{__MP" in field:
        random_mobile_phone = create_random_mobile_phone()
        # 调用生成随机手机号码的方法
        field = field.replace("{__MP}", random_mobile_phone)
    else:
        pass

    return field
    # 返回替换后的字段


def function_sql(field, mysql_result_list):
    # 替换MySQL查询结果的方法，第一个参数是yaml文件里面定义的字段，第二个参数是MySQL查询结果列表

    if "{__SQL" in field:
        mysql_index_list = re.findall("{__SQL(.+?)}", field)
        # 获取索引列表
        for i in mysql_index_list:
            mysql_value = mysql_result_list[int(i)]
            if type(mysql_value) != str:
                mysql_value = str(mysql_value)
            field = field.replace("{__SQL" + i + "}", mysql_value)

    return field
    # 返回替换后的字段
