import shutil

import bs4
import requests


def get_pony_img_url():
    data = requests.get("https://pikabu.ru/community/mlp")
    bsData = bs4.BeautifulSoup(data.text, "html.parser")
    allStory = bsData.find_all("div", attrs={"class": "story-image__content"})
    lastStory = allStory.pop()
    return lastStory.find("img").get("data-large-image")

