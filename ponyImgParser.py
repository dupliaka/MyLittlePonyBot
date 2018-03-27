import bs4
import requests


def get_pony_img_url():
    data = requests.get("https://pikabu.ru/community/mlp")
    bsData = bs4.BeautifulSoup(data.text, "html.parser")
    allStory = bsData.find_all("div", attrs={"class": "story-image__content"})
    allStory.reverse()
    return allStory.pop().find("img").get("src")
