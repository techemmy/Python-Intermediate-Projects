import requests
import webbrowser
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Special:Random"

article_page = requests.get(url)

soup = BeautifulSoup(article_page.text, "html.parser")
article_title = soup.find(id='firstHeading')
print("The title of the Random article is:", article_title.string)

read = input("Do you want to view the article: (y/n)")
if read == "y":
    webbrowser.open(article_page.url)

print("The URL is:", article_page.url)
