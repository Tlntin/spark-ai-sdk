## [English](README.md) | 中文

## 这是什么
- 讯飞星火AI大模型的python SDK

## how to use
1. 需要从官网 https://www.xfyun.cn/ 获取API

2. 安装
```bash
git clone https://github.com/Tlntin/spark-ai-sdk.git
cd spark-ai-sdk
python setup.py install

# 或者
pip install git+https://github.com/Tlntin/spark-ai-sdk.git
```

3. 使用

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

