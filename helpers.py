# Please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv('PPLX_APIKEY'), base_url="https://api.perplexity.ai/"
)


def search(query: str) -> str:
    return nlpProcess(query)


def nlpProcess(query: str, llm="sonar-pro") -> str:
    response = client.chat.completions.create(
        model=llm,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": query},
        ],
        stream=False,
    )
    resp = response.choices[0].message.content
    print("查询响应结果:" + resp)
    return resp


if __name__ == "__main__":
    resp = nlpProcess("大模型会思考吗")
    print(resp)
