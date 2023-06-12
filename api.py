import requests

res = requests.get("https://api.openai.com/v1/chat/completions")
print(res.json())
