from ruamel import yaml

from setting.project_config import *


def read_yaml(yaml_absolute_path):
    """
    读取yaml文件
    :param yaml_absolute_path: 参数为需要读取的yaml文件的绝对路径
    :return:
    """

    with open(yaml_absolute_path, "r", encoding="utf-8") as f:
        data_list = yaml.load(f, Loader=yaml.Loader)
    return data_list
    # 返回一个数据列表


def write_yaml(yaml_relative, data_list):
    """
    写入yaml文件
    :param yaml_relative: 第一个参数为需要写入的yaml文件的相对路径
    :param data_list: 第二个参数为需要转换的数据
    :return:
    """

    with open(yaml_path + yaml_relative, "w",
              encoding="utf-8") as f:
        yaml.dump(data_list, f, Dumper=yaml.RoundTripDumper,
                  default_flow_style=False, allow_unicode=True, indent=4)
    return yaml_relative
    # 返回一个yaml文件的相对路径


def merge_yaml():
    """
    合并所有yaml文件的方法
    :return:
    """

    yaml_list = []
    for root, dirs, files in os.walk(yaml_path):
        # root为当前目录路径
        # dirs为当前路径下所有子目录，list格式
        # files为当前路径下所有非目录子文件，list格式
        for i in files:
            if os.path.splitext(i)[1] == '.yaml':
                # os.path.splitext()把路径拆分为文件名+扩展名
                if i != first_test_case_file:
                    yaml_list.append(os.path.join(root, i))
                else:
                    the_first_yaml = os.path.join(root, first_test_case_file)
    yaml_list.append(the_first_yaml)
    # 加入第一个yaml文件
    yaml_list.reverse()
    # 反转排序

    temporary_list = []
    for i in yaml_list:
        if i:
            j = read_yaml(i)
            # 调用读取yaml文件的方法
            if j:
                temporary_list.extend(j)
                # 往列表里逐步添加元素

    return temporary_list
    # 返回一个临时列表
