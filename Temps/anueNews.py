
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.cnyes.com/news/cat/headline?exp=a")
soup = BeautifulSoup(response, "html.parser")

go = soup.find("div", {"class": "_2bFl theme-list"})
basic = "https://news.cnyes.com"
news = []
for i in range(5):
    news.append(
        [go.find_all("a")[i]].text(),
        basic + go.find_all("a")[i]['herf']
    )

print(news)    