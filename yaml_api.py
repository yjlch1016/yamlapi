import os

import click


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('V1.0.1')
    ctx.exit()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--p', prompt='请输入工程名称', type=str, nargs=1, help='工程名称')
@click.option('--version', '-v', help='版本号',
              is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def start_project(p):
    """honeybee（蜜蜂）接口测试框架"""

    if p:
        # 如果--p的值不为空

        project_path = "./" + p
        create_directory(project_path)
        # 工程的目录

        case_path = os.path.join(project_path, "case")
        # 测试用例的目录
        create_directory(case_path)
        file_name = case_path + "/__init__.py"
        create_file(file_name, "# 初始化文件\n\r")
        file_name = case_path + "/demo_test.py"
        create_file(file_name, "# 测试用例\n\r")

        log_path = os.path.join(project_path, "log")
        # 日志的目录
        create_directory(log_path)

        report_path = os.path.join(project_path, "report")
        # 测试报告的目录
        create_directory(report_path)

        yaml_path = os.path.join(project_path, "resource")
        # yaml文件的目录
        create_directory(yaml_path)
        file_name = yaml_path + "/case_list.csv"
        create_file(file_name, "此文件只作展示，不参与逻辑判断\n\r")
        file_name = yaml_path + "/demo_one.yaml"
        create_file(file_name, "# 测试用例one\n\r")
        file_name = yaml_path + "/demo_two.yaml"
        create_file(file_name, "# 测试用例two\n\r")
        file_name = yaml_path + "/demo_three.yaml"
        create_file(file_name, "# 测试用例three\n\r")

        setting_path = os.path.join(project_path, "setting")
        # 工程配置文件的目录
        create_directory(setting_path)
        file_name = setting_path + "/__init__.py"
        create_file(file_name, "# 初始化文件\n\r")
        file_name = setting_path + "/project_setting.py"
        create_file(file_name, "# 整个工程的配置文件\n\r")

        tool_path = os.path.join(project_path, "tool")
        # 工具包的目录
        create_directory(tool_path)
        file_name = tool_path + "/__init__.py"
        create_file(file_name, "# 初始化文件\n\r")

        file_name = project_path + "/Jenkinsfile"
        create_file(file_name, "")
        file_name = project_path + "/README.md"
        create_file(file_name, "")
        file_name = project_path + "/pytest.ini"
        create_file(file_name, "")
        file_name = project_path + "/requirements.txt"
        create_file(file_name, "")
        # 各种配置文件

        click.echo("%s创建成功" % p)
    else:
        click.echo("工程名称不能为空")


def create_directory(directory_path):
    try:
        os.mkdir(directory_path, mode=0o777)
    except OSError:
        pass


def create_file(file_path, characters):
    if not os.path.isfile(file_path):
        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write(characters)
    else:
        pass


if __name__ == '__main__':
    start_project()
