import requests

def get(url,paylaod,json):

url = "https://www.autohotkey.com/download/ahk-install.exe"

res = requests.get(url)

if res == 200:
    print("installed!")
else : 
    print("ERROR!")