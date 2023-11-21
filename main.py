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
count = 0
def parse_reviews (change, count):
    reviews = soup.find_all("div", class_= f"response {change}")
    for review in reviews:
        review_text = review.find("span", class_= "_reachbanner_").text.strip()
        with open(fr"C:\Users\User\Desktop\dataset\{change}\{change}_{count:04}.txt", "w", encoding="utf-8") as file:
            file.write(review_text)
        count+=1
# for i in range (1, 1000):
#     url = f"https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/all/perpage/10/page/{i}/"
#     headers = {
#         "Accept": "*/*",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.888 YaBrowser/23.9.0.0 Safari/537.36"
#     }
#     req = requests.get(url, headers = headers)
#     src = req.text

with open("index.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml")
parse_reviews ("bad")
print (count)
parse_reviews ("good")
print (count)