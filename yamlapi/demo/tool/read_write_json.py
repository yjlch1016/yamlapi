import demjson

from setting.project_config import *


def read_json(json_absolute_path):
    """
    读取json文件
    :param json_absolute_path: 参数为需要读取的json文件的绝对路径
    :return:
    """

    with open(json_absolute_path, "r", encoding="utf-8") as f:
        data_list = demjson.decode(f.read(), encoding="utf-8")
    return data_list
    # 返回一个数据列表


def write_json(json_relative, data_list):
    """
    写入json文件
    :param json_relative: 第一个参数为需要写入的json文件的相对路径
    :param data_list: 第二个参数为需要转换的数据
    :return:
    """

    with open(yaml_path + json_relative, "wb") as f:
        f.write(demjson.encode(data_list, encoding="utf-8"))
    return json_relative
    # 返回一个json文件的相对路径


def merge_json():
    """
    合并所有json文件的方法
    :return:
    """

    json_list = []
    for root, dirs, files in os.walk(yaml_path):
        # root为当前目录路径
        # dirs为当前路径下所有子目录，list格式
        # files为当前路径下所有非目录子文件，list格式
        for i in files:
            if os.path.splitext(i)[1] == '.json':
                # os.path.splitext()把路径拆分为文件名+扩展名
                if i != first_test_case_file:
                    json_list.append(os.path.join(root, i))
                else:
                    the_first_json = os.path.join(root, first_test_case_file)
    json_list.append(the_first_json)
    # 加入第一个json文件
    json_list.reverse()
    # 反转排序

    temporary_list = []
    for i in json_list:
        if i:
            j = read_json(i)
            # 调用读取json文件的方法
            if j:
                temporary_list.extend(j)
                # 往列表里逐步添加元素

    return temporary_list
    # 返回一个临时列表
