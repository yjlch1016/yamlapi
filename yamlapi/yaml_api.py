import os
import shutil
import subprocess
from distutils.sysconfig import get_python_lib

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('V1.3.6')
    ctx.exit()


def copy_directory(old_directory, new_directory):
    # 拷贝目录

    try:
        shutil.copytree(
            old_directory, new_directory, ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))
    except OSError as e:
        click.echo("拷贝目录出错：", e)


def del_files(filepath):
    # 删除测试报告与日志目录下的所有文件

    try:
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    except OSError as e:
        click.echo("删除测试报告与日志目录下的所有文件出错：", e)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--version', '-v', help='版本号',
              is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def cli():
    """yamlapi接口测试框架"""
    pass


@cli.command()
@click.option('--p', prompt='请输入工程名称', type=str, nargs=1, help='工程名称')
def create(p):
    """创建接口测试工程"""

    if p:
        # 如果--p的值不为空
        project_path = "./" + p
        # 工程的目录
        demo_path = get_python_lib() + "/yamlapi/demo"
        copy_directory(demo_path, project_path)
        # 拷贝目录
        click.echo("%s创建成功！" % p)
    else:
        click.echo("工程名称不能为空！")


@cli.command()
@click.option('--c', prompt='请输入环境缩写', type=str, nargs=1, help='环境缩写')
def run(c):
    """运行接口测试工程"""

    if c:
        # 如果--c的值不为空
        subprocess.run('pytest --cmd=' + c, shell=True)
        # 调用pytest命令
        click.echo("运行环境：%s" % c)
    else:
        click.echo("环境缩写不能为空！")


@cli.command()
def clean():
    """清理测试报告与日志目录下的所有文件"""

    report_log_path = "./report_log"
    report_log_path = os.path.abspath(report_log_path)

    if os.path.exists(report_log_path):
        if os.listdir(report_log_path):
            del_files(report_log_path)
            click.echo("清理测试报告与日志目录下的所有文件成功！")
        else:
            click.echo("%s为空！" % report_log_path)
    else:
        click.echo("%s不存在！" % report_log_path)


if __name__ == '__main__':
    cli()
