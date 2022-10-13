import json

filename = 'username.json'
file_path = f"C:/Users/admin/Desktop/For files/{filename}"

with open(file_path) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
