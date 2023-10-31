import os
from bs4 import BeautifulSoup
import requests
#for i in range (1, 2340, 1)
    # url = f"https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/all/perpage/10/page/{i}/"
    # headers = {
    #     "Accept": "*/*",
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.888 YaBrowser/23.9.0.0 Safari/537.36"
    # }
    # req = requests.get(url, headers = headers)
    # src = req.text

with open("index.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
os.mkdir("dataset")
bad_reviews = soup.find_all("div", class_= "response bad")
count = 0
for bad_review in bad_reviews:
    bad_review_text = bad_review.find("span", class_= "_reachbanner_").text.strip()
    with open(f"bad_{count:04}.txt", "w", encoding="utf-8") as file:
        file.write(bad_review_text)
    count+=1
good_reviews = soup.find_all("div", class_= "response good")
count = 0
for good_review in good_reviews:
    good_review_text = good_review.find("span", class_= "_reachbanner_").text.strip()
    with open(f"good_{count:04}.txt", "w", encoding="utf-8") as file:
        file.write(good_review_text)
    count+=1