import requests
import bs4

website = requests.get("https://fast.com")
html = website.text
html1_parser = bs4.BeautifulSoup(html, "html.parser")
data= html1_parser.find ("div",attrs={"class":"your-speed-message"}).text
print(data)