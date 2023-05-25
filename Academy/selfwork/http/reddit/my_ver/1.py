import requests
import json
from datetime import datetime

start_time = datetime.strptime("01_31_2023", "%m_%d_%Y")
end_time = datetime.strptime("01_29_2023", "%m_%d_%Y")
start_epoch = str(int(start_time.timestamp()))
end_epoch = str(int(end_time.timestamp()))

# Зробити виклик через API та зберегти відповідь

subreddit = "r/ideavim"
url = f"https://api.pushshift.io/reddit/" \
      f"comment/search?limit=1000&order=desc&subreddit={subreddit}&before={start_epoch}&after={end_epoch}"
r = requests.get(url)  # Робимо запит
print(f"Status code: {r.status_code}")  # Атрибут status_code повідомляє нам, чи був запит успішним
# Зберегти відповідь API у змінну
response_dict = r.json()
file_name = 'comments.json'
with open(file_name, 'w') as f:
    json.dump(response_dict, f, indent=4)