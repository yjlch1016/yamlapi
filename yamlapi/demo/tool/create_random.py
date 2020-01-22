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
