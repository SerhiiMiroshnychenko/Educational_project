import requests  # type: ignore

# defining the api-endpoint
API_ENDPOINT = "https://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "FlBvpNxoEmyJvvotbyyJv4ybC5Bn2YD9"

# data to be sent to api
data = {"api_dev_key": API_KEY,
        'api_user_key': '7f5e0a669e1e57b226383a0b7c526298',
        "api_option": "list",
        'api_result_limit': 25
        }

r = requests.post(API_ENDPOINT, data=data)

# extracting response text
pastebin_url = r.text
print(f"The pastebin URL is:{pastebin_url}")
