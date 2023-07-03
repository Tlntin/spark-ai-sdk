## English | [中文](https://github.com/Tlntin/spark-ai-sdk/blob/main/README_zh.md)

## what is?
- python sdk for XunFei (iFLYTEK) Spark AI

## how to use
1. get Spark AI api in https://www.xfyun.cn/

2. install
```bash
pip install spark-ai-sdk
```

3. use

```python
from spark_ai_sdk.spark_ai import SparkAI

history1 = []
# -------------------------
APP_ID = "xxxxx"
APISecret = "xxxxxxxxxxxxxxxxxxxxx"
APIKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
API_URL = "wss://spark-api.xf-yun.com/v1.1/chat"
# ------------------------
server = SparkAI(
    app_id=APP_ID,
    api_key=APIKey,
    api_secret=APISecret,
    api_url=API_URL
)
while True:
    query1 = input("User: ")
    if query1 == "exit" or query1 == "stop":
        break
    for response1, history1 in server.chat_stream(query1, history1):
        print("\rAI: ", response1, end="")
    print("")
```

