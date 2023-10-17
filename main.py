import os
from bs4 import BeautifulSoup
import requests

def parse_reviews():
url = "https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/all/perpage/10/page/1/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
reviews = soup.find_all("div", class_="response")

for review in reviews:
text = review.find("span", itemprop="description").text.strip()
rating = review.find("span", class_="rating").text.strip()
print(f"Рецензия: {text}")
print(f"Рейтинг: {rating}")
print("---")