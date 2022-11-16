import requests
import json

webhook = "https://oapi.dingtalk.com/robot/send?access_token=df643071534d605" \
          "e447aee0f88e4f85ed7d1fbbf579ab46098c4797c385df730"
header = {
    "Content-Type": "application/json;charset=UTF-8"
}


def push_report(keyword, data):
    message_body = {
        "msgtype": "markdown",
        "markdown": {
            "title": keyword,
            "text": "## %s \n" % "有预约信息请注意查收" +
                    "#### •  预约老师: **%s** \n" % data['teacher'] +
                    "#### •  学生姓名: **%s** \n" % data['name'] +
                    "#### •  学生学校: **%s** \n" % data['school'] +
                    "#### •  学生年级: **%s** \n" % data['grade'] +
                    "#### •  学生选科: **%s** \n" % data['subjects'] +
                    "#### •  预约日期: **%s** \n" % data['date'] +
                    "#### •  预约时间: **%s** \n" % data['time']
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    return message_body


def push_report2(keyword, data):
    message_body = {
        "msgtype": "markdown",
        "markdown": {
            "title": keyword,
            "text": "## %s \n" % "有取消预约信息请注意查收" +
                    "#### •  预约老师: **%s** \n" % data['teacher'] +
                    "#### •  学生姓名: **%s** \n" % data['name'] +
                    "#### •  预约日期: **%s** \n" % data['date'] +
                    "#### •  预约时间: **%s** \n" % data['time']
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    return message_body


def push(keyword, data):
    message_body = {}
    if keyword == '预约信息':
        message_body = push_report(keyword, data)
    elif keyword == '预约取消信息':
        message_body = push_report2(keyword, data)
    send_data = json.dumps(message_body)  # 将字典类型数据转化为json格式
    chat_bot = requests.post(url=webhook, data=send_data, headers=header)
    opener = chat_bot.json()
    if opener["errmsg"] == "ok":
        print(u"%s 通知消息发送成功！" % opener)
    else:
        print(u"通知消息发送失败，原因：{}".format(opener))
