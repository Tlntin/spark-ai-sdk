from spark_ai_sdk.spark_ai import SparkAI


if __name__ == "__main__":
    history1 = []
    # -------------------------
    APP_ID = "xxxxxxxx"
    APISecret = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    APIKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
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