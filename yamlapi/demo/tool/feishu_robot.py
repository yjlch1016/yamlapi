"""
飞书机器人开发文档
https://www.feishu.cn/hc/zh-CN/articles/360024984973
"""

import base64
import hmac
import json
from hashlib import sha256

import requests

from setting.project_config import *


def send_feishu_alarm(total, passed, failed, error, skipped, successful, duration):
    """
    发送飞书报警的方法
    :param total:
    :param passed:
    :param failed:
    :param error:
    :param skipped:
    :param successful:
    :param duration:
    :return:
    """

    timestamp = str(round(time.time()))
    secret = feishu_secret

    key = f"{timestamp}\n{secret}"
    key_enc = key.encode("utf-8")
    msg = ""
    msg_enc = msg.encode("utf-8")
    hmac_code = hmac.new(key_enc, msg_enc, digestmod=sha256).digest()
    sign = base64.b64encode(hmac_code).decode("utf-8")

    url = feishu_webhook

    payload_message = {
        "timestamp": timestamp,
        "sign": sign,
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True,
                "enable_forward": True
            },
            "elements": [{
                "tag": "div",
                "text": {
                    "content": "总共：{}\n通过：{}\n失败：{}\n错误：{}\n跳过：{}\n成功率：{:.2%}\n总共耗时：{:.2f}秒"
                        .format(total, passed, failed, error, skipped, successful, duration),
                    "tag": "lark_md"
                }
            }, {
                "actions": [{
                    "tag": "button",
                    "text": {
                        "content": card_elements_actions_text_content,
                        "tag": "lark_md"
                    },
                    "url": card_elements_actions_url,
                    "type": "primary",
                    "value": {}
                }],
                "tag": "action"
            }],
            "header": {
                "title": {
                    "content": card_header_title_content,
                    "tag": "plain_text"
                },
                "template": "red"
            }
        }
    }
    # 消息卡片

    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }

    return requests.request("POST", url, data=json.dumps(payload_message), headers=headers)
