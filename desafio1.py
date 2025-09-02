import requests

requisição = requests.get("https://teste1-aa255-default-rtdb.firebaseio.com/.json")
print(requisição.json())