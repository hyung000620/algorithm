import requests
import os

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
data = {
    "content": "1일 1알고리즘 푸실 시간입니다",
    "username": "GitHub Bot"
}

result = requests.post(webhook_url, json=data)
print("Response Code:", result.status_code)
