import os
from bs4 import BeautifulSoup
import requests

# url = "https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/all/perpage/10/page/1/"
# headers = {
#     "Accept": "*/*",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.888 YaBrowser/23.9.0.0 Safari/537.36"
# }
# req = requests.get(url, headers = headers)
# src = req.text

with open("index.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
all_names = soup.find_all(class_ = "profile_name")
all_reviews_text = soup.find_all("span", class_= "_reachbanner_")
for name in all_names:
    name_text = name.text
    print(name_text)
    print("-------")
    for review in all_reviews_text:
        review_text = review.text
        print(review_text.strip())