import os
from bs4 import BeautifulSoup
import requests

path = r"C:\Users\User\Desktop"
projectname = "dataset"
folders = \
    ["good", 
    "bad"]
fullPath = os.path.join(path, projectname)
if not os.path.exists(fullPath):
    os.mkdir(fullPath)
for f in folders:
    folder = os.path.join(fullPath, f)
    if not os.path.exists(folder):
        os.mkdir(folder)


def parse_reviews(change):
    reviews = soup.find_all("div", class_= f"response {change}")
    review_texts = []
    for review in reviews:
        review_text = review.find("span", class_="_reachbanner_").text.strip()
        review_texts.append(review_text)
    return review_texts


def write_reviews(reviews, change, count):
    for review_text in reviews:
        if count > 1000:
            with open(fr"C:\Users\User\Desktop\dataset\{change}\{change}_{count:04}.txt", "w", encoding="utf-8") as file:
                file.write(review_text)
            count += 1
        else:
            break
    return count


good_count = 0
bad_count = 0
for i in range (1, 2000):
    url = f"https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/all/perpage/10/page/{i}/"
    headers = {
        "Accept": "*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.888 YaBrowser/23.9.0.0 Safari/537.36"
    }
    src = requests.get(url, headers = headers).text

    # with open("index.html", encoding="utf-8") as file:
    #     src = file.read()
    soup = BeautifulSoup(src, "lxml")

    bad_reviews = parse_reviews("bad")
    bad_count = write_reviews(bad_reviews, "bad", bad_count)
    print(f"Плохих отзывов: {bad_count}")
    good_reviews = parse_reviews("good")
    good_count = write_reviews(good_reviews, "good", good_count)
    print(f"Хороших отзывов: {good_count}")
    print(f"\n Количество итераций: {i} \n" )