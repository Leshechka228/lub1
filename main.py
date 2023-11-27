import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pathlib import Path

desktop_path = Path.home() / "Desktop"
projectname = "dataset"
folders = \
    ["good", 
    "bad"]
fullPath = os.path.join(desktop_path, projectname)
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
        if count < 1000:
            with open(fr"{desktop_path}\dataset\{change}\{change}_{count:04}.txt", "w", encoding="utf-8") as file:
                file.write(review_text)
            count += 1
        else:
            break
    return count

if __name__ == "__main__":
    bad_count = 0
    good_count = 0
    for i in range(1, 2300):
        url = f"https://www.kinopoisk.ru/film/251733/reviews/ord/date/status/all/perpage/10/page/{i}/"
        options = webdriver.ChromeOptions()
        file_path = os.path.abspath("yandexdriver.exe")
        service = webdriver.ChromeService(executable_path=file_path)
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        time.sleep(10)
        src = driver.page_source
        soup = BeautifulSoup(src, "lxml")
        driver.quit()
        
        bad_reviews = parse_reviews("bad")
        bad_count = write_reviews(bad_reviews, "bad", bad_count)

        good_reviews = parse_reviews("good")
        good_count = write_reviews(good_reviews, "good", good_count)

        print(f"Плохих отзывов: {bad_count}")
        print(f"Хороших отзывов: {good_count}")
        print(f"\n Количество итераций: {i} \n")