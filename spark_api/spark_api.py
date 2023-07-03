import json
from datetime import datetime, timezone
from websocket import create_connection, WebSocketConnectionClosedException
import hmac
import base64
from urllib.parse import urlencode, urlparse


class SparkAPI:
    def __init__(self, app_id, api_key, api_secret, api_url):
        """
         you can get this in https://www.xfyun.cn/
        :param app_id:
        :param api_key:
        :param api_secret:
        :param api_url:
        """
        self.app_id = app_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_url = api_url

    def get_authorization_url_url(self):
        """
        doc url: https://www.xfyun.cn/doc/spark/general_url_authentication.html
        :return:
        """
        url = urlparse(self.api_url)
        date = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S %Z')
        signature_origin = "host: {}\ndate: {}\nGET {} HTTP/1.1".format(
            url.netloc, date, url.path
        )
        signature = base64.b64encode(
            hmac.new(
                self.api_secret.encode(),
                signature_origin.encode(),
                digestmod='sha256'
            ).digest()
        ).decode()
        authorization_origin = \
            'api_key="{}",algorithm="{}",headers="{}",signature="{}"'.format(
                self.api_key, "hmac-sha256", "host date request-line", signature
            )
        authorization = base64.b64encode(authorization_origin.encode()).decode()
        params = {
            "authorization": authorization,
            "date": date,
            "host": url.netloc
        }
        ws_url = self.api_url + "?" + urlencode(params)
        return ws_url

    @staticmethod
    def get_prompt(query: str, history: list):
        """
        :param query:
        :param history:
        :return: dict
        """
        use_message = {"role": "user", "content": query}
        history.append(use_message)
        message = {"text": history}
        return message

    def build_inputs(
            self,
            message: dict,
            user_id: str = "001",
            domain: str = "general",
            temperature: float = 0.5,
            max_tokens: int = 2048
    ):
        input_dict = {
            "header": {
                "app_id": self.app_id,
                "uid": user_id,
            },
            "parameter": {
                "chat": {
                    "domain": domain,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }
            },
            "payload": {
                "message": message
            }
        }
        return json.dumps(input_dict)

    @staticmethod
    def process_response(response_str: str, history: list):
        res_dict: dict = json.loads(response_str)
        code = res_dict.get("header", {}).get("code")
        status = res_dict.get("header", {}).get("status", 2)
        if code == 0:
            res_dict = res_dict.get("payload", {}).get("choices", {}).get("text", [{}])[0]
            res_content = res_dict.get("content", "")
            if len(res_dict) > 0 and len(res_content) > 0:
                if "index" in res_dict:
                    del res_dict["index"]
                response = res_content
                if status == 0:
                    history.append(res_dict)
                else:
                    history[-1]["content"] += response
                    response = history[-1]["content"]
                return response, history, status
            else:
                return "", history, status
        else:
            print("error code ", code)
            print("you can see this website to know code detail")
            print("https://www.xfyun.cn/doc/spark/%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E.html")
            return "", history, status

    def chat_stream(
            self,
            query: str,
            history: list,
            user_id: str = "001",
            domain: str = "general",
            max_tokens: int = 2048,
            temperature: float = 0.5,
    ):
        # the max of max_length is 4096
        max_tokens = min(max_tokens, 4096)
        url = self.get_authorization_url_url()
        ws = create_connection(url)
        message = self.get_prompt(query, history)
        # print("message: ", message1)
        input_str = self.build_inputs(
            message=message,
            user_id=user_id,
            domain=domain,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        ws.send(input_str)
        response_str = ws.recv()
        try:
            while True:
                response, history, status = self.process_response(
                    response_str, history
                )
                yield response, history
                if len(response) == 0 or status == 2:
                    break
                response_str = ws.recv()
        except WebSocketConnectionClosedException:
            print("Connection closed")
        finally:
            ws.close()


