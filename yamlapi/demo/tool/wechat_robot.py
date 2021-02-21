"""
企业微信机器人开发文档
https://work.weixin.qq.com/api/doc/90000/90136/91770
"""

import json

from setting.project_config import *


def send_wechat_alarm(total, passed, failed, error, skipped, successful, duration):
    """
    发送企业微信报警的方法
    :param total:
    :param passed:
    :param failed:
    :param error:
    :param skipped:
    :param successful:
    :param duration:
    :return:
    """

    url = wechat_webhook
    # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXXXX

    payload = {
        "msgtype": "text",
        "text": {
            "content": "环境：{}\n总共：{}条\n通过：{}条\n失败：{}条\n错误：{}条\n跳过：{}条\n成功率：{:.2%}\n总共耗时：{:.2f}秒"
                .format(environment, total, passed, failed, error, skipped, successful, duration),
            "mentioned_list": [],
            "mentioned_mobile_list": []
        }
    }
    # 请求体

    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    # 请求头

    return requests.request("POST", url, data=json.dumps(payload), headers=headers)
    # 发起HTTP请求
