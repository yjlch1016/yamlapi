import random
import string
import time


def create_random_number(digit):
    """
    生成随机数字
    :param digit: 参数为位数（长度）
    :return:
    """

    number_list = []
    for n in range(digit):
        number = str(random.randint(1, 9))
        number_list.append(number)
    random_number = " ".join(number_list).replace(" ", "")
    return random_number
    # 返回随机数字


def create_random_letters(digit):
    """
    生成随机字母
    :param digit: 大小写混合，参数为位数（长度）
    :return:
    """

    letters_list = [random.choice(string.ascii_letters) for i in range(digit)]
    # string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    random_letters = "".join(letters_list)
    return random_letters
    # 返回随机字母


def create_random_mobile_phone():
    """
    生成随机手机号码
    :return:
    """

    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第二位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 第三位数字
    suffix = random.randint(9999999, 100000000)
    # 最后八位数字
    return "1{}{}{}".format(second, third, suffix)
    # 返回随机手机号码


def create_random_datetime(start_year, end_year):
    """
    生成随机日期时间
    :param start_year: 第一个参数为开始年份
    :param end_year: 第二个参数为结束年份
    :return:
    """

    start_tuple = (int(start_year), 1, 1, 0, 0, 0, 0, 0, 0)
    # 设置开始日期时间元组（开始年份-01-01 00：00：00）
    end_tuple = (int(end_year), 12, 31, 23, 59, 59, 0, 0, 0)
    # 设置结束日期时间元组（结束年份-12-31 23：59：59）

    start_time_stamp = time.mktime(start_tuple)
    # 生成开始时间戳
    end_time_stamp = time.mktime(end_tuple)
    # 生成结束时间戳

    t = random.randint(start_time_stamp, end_time_stamp)
    # 在开始和结束时间戳中随机取出一个
    datetime_tuple = time.localtime(t)
    # 将时间戳生成时间元组
    random_datetime = time.strftime("%Y-%m-%d %H:%M:%S", datetime_tuple)
    # 将时间元组转成格式化字符串（%Y-%m-%d %H:%M:%S）

    return random_datetime
    # 返回随机日期时间
