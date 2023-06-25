import requests
import json

f = open("./key.txt")
API_KEY = f.read()
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
gpt_model = "gpt-3.5-turbo"


# following function is taken from
# https://medium.com/codingthesmartway-com-blog/unlocking-the-power-of-gpt-4-api-a-beginners-guide-for-developers-a4baef2b5a81
def generate_chat_completion(messages, model=gpt_model, temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
