import os
import requests
import json

os.system('clear')
url = "http://localhost:8033/health"

x1 = requests.get(url)
print(x1.json())