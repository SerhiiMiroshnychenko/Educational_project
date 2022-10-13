import json

username = input("What is your name? ")

filename = 'username.json'
file_path = f"C:/Users/admin/Desktop/For files/{filename}"
with open(file_path, 'w') as f:
    json.dump(username, f)
    print(f"We`ll remember you when you come back, {username}!")
