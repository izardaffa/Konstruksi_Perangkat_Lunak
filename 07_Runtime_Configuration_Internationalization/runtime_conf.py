import json

ip = "127.0.0.1"

with open("config.json", "r") as file:
    config = json.load(file)
    ip = config['serverIP']

print(f"Server IP: {ip}")
