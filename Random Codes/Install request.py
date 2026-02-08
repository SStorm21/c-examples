import requests


res = requests.get(url="https://192.168.0.1?")

if res == 200:
    print("installed!")
else : 
    print("ERROR!")