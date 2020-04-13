import random
import string


def create_random_number(digit):
    # 生成随机数字，参数为位数（长度）

    number_list = []
    for n in range(digit):
        number = str(random.randint(1, 9))
        number_list.append(number)
    random_number = " ".join(number_list).replace(" ", "")
    return random_number
    # 返回随机数字


def create_random_letters(digit):
    # 生成随机字母，大小写混合，参数为位数（长度）

    letters_list = [random.choice(string.ascii_letters) for i in range(digit)]
    # string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    random_letters = "".join(letters_list)
    return random_letters
    # 返回随机字母


def create_random_mobile_phone():
    # 生成随机手机号码

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
