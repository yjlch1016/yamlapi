from ruamel import yaml

from setting.project_config import *


def read_yaml(yaml_relative):
    # 读取yaml文件，参数为需要读取的yaml文件的相对路径

    with open(yaml_path + yaml_relative, "r",
              encoding="utf-8") as f:
        data_list = yaml.load(f, Loader=yaml.Loader)
    return data_list
    # 返回一个数据列表


def write_yaml(yaml_relative, data_list):
    # 写入yaml文件，第一个参数为需要写入的yaml文件的相对路径，第二个参数为需要转换的数据

    with open(yaml_path + yaml_relative, "w",
              encoding="utf-8") as f:
        yaml.dump(data_list, f, Dumper=yaml.RoundTripDumper,
                  default_flow_style=False, allow_unicode=True, indent=4)
    return yaml_relative
    # 返回一个yaml文件的相对路径
