import sys
import requests
import datetime

# 定义python系统变量
JOB_URL = sys.argv[0]
JOB_NAME = sys.argv[0]

# 获取当前系统时间
current_time = datetime.datetime.now()
# 飞书机器人的webhook地址
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/76560fd1-9aff-4be6-9397-9d7a2e767b6f'
method = 'post'
headers = {'Content-Type': 'application/json'}

data = {
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True,
            "enable_forward": True
        },
        "elements": [{
            "tag": "div",
            "text": {
                "content": f"【测试完毕】{current_time}",  # 这是卡片的内容，也可以添加其他的内容：比如构建分支，构建编号等
                "tag": "lark_md"
            }
        }, {
            "actions": [{
                "tag": "button",
                "text": {
                    "content": "查看测试报告",  # 这是卡片的按钮，点击可以跳转到url指向的allure路径
                    "tag": "lark_md"
                },
                "url": f"{JOB_URL}/allure/",  # JOB_URL 调用python定义的变量，该url是服务器下的allure路径
                "type": "default",
                "value": {}
            }],
            "tag": "action"
        }],
        "header": {
            "title": {
                "content": JOB_NAME + "构建报告",  # JOB_NAME 调用python定义的变量，这是卡片的标题
                "tag": "plain_text"
            }
        }
    }
}
res = requests.request(method=method, url=url, headers=headers, json=data)
print(res)
print(res.json())
# 早上吃了一个苹果，一个蛋，一个馒头，一碗粥，2个油条，一个沙琪玛，鸭脖