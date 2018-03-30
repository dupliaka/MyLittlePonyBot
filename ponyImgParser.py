import ssl
import time

import bs4
import requests


def get_pony_img_url():
    try:
        data = requests.get("https://pikabu.ru/community/mlp")
    except (requests.RequestException, requests.ReadTimeout, ssl.SSLError)as e:
        print('ConnectionError = ' + str(e))
        time.sleep(180)
        get_pony_img_url()
    bsData = bs4.BeautifulSoup(data.text, "html.parser")
    allStory = bsData.find_all("div", attrs={"class": "story-image__content"})
    allStory.reverse()
    return allStory.pop().find("img").get("src")



