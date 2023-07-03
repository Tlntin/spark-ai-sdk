## English | [中文](README_zh.md)

## what is?
- python sdk for XunFei (iFLYTEK) Spark AI

## how to use
1. get Spark AI api in https://www.xfyun.cn/

2. install
```bash
git clone https://github.com/Tlntin/spark_api
cd html2epub
python setup.py install

# or
pip install git+https://github.com/Tlntin/spark_ai_sdk
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
server = SparkAPI(
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

