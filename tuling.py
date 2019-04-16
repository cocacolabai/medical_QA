
import json
import requests

# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "58a614b618684bc8b4967221b70c867d"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "225240"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]


x = auto_reply("hello")
print(x)

