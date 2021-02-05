"""
钉钉自定义机器人开发文档
https://developers.dingtalk.com/document/app/custom-robot-access
"""

import base64
import hashlib
import hmac
import json
import urllib.parse

from setting.project_config import *


def send_dingtalk_alarm(total, passed, failed, error, skipped, successful, duration):
    """
    发送钉钉报警的方法
    :param total:
    :param passed:
    :param failed:
    :param error:
    :param skipped:
    :param successful:
    :param duration:
    :return:
    """

    timestamp = str(round(time.time() * 1000))
    # 时间戳
    secret = dingtalk_secret
    # 密钥

    secret_enc = secret.encode("utf-8")
    string_to_sign = "{}\n{}".format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    # 签名

    url = dingtalk_webhook + "&timestamp=" + timestamp + "&sign=" + sign
    # https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX

    payload = {
        "msgtype": "text",
        "text": {
            "content": "环境：{}\n总共：{}条\n通过：{}条\n失败：{}条\n错误：{}条\n跳过：{}条\n成功率：{:.2%}\n总共耗时：{:.2f}秒"
                .format(environment, total, passed, failed, error, skipped, successful, duration)
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    # 请求体

    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    # 请求头

    return requests.request("POST", url, data=json.dumps(payload), headers=headers) \
        .content.decode("utf8")
    # 发起HTTP请求
