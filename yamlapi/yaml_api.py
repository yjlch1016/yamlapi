import shutil
from distutils.sysconfig import get_python_lib

import click


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('V1.2.0')
    ctx.exit()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--p', prompt='请输入工程名称', type=str, nargs=1, help='工程名称')
@click.option('--version', '-v', help='版本号',
              is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def start_project(p):
    """yamlapi接口测试框架"""

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


def copy_directory(old_directory, new_directory):
    # 拷贝目录

    try:
        shutil.copytree(
            old_directory, new_directory, ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))
    except OSError as e:
        click.echo("拷贝目录出错：", e)


if __name__ == '__main__':
    start_project()
