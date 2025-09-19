import os
from openai import OpenAI
import json


client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "you are a speclist on python language"},
        {"role": "user", "content": "怎么显式定义一个变量的类型"},
    ],
    # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
    # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
    # extra_body={"enable_thinking": False},
)
res = completion.model_dump_json()
jsonRes:dict = json.loads(res)
res1:list = jsonRes.get('choices')
res2: dict =res1[0]
res3: dict=res2.get('message')
res4: str=res3.get('content')
print(res4)
