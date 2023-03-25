import requests
from bs4 import BeautifulSoup
import logging
from urllib.request import urlopen
import os


save_dir = "images/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
}

query = "elon musk"
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUbd4EeTscHWSj9kEjoSL-AIAg5Lg:1678974049925&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiVzdTeyeD9AhVaBbcAHWb2BOsQ_AUoAnoECAEQBA")

# print(response)
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
img_tags = soup.find_all("img")
del img_tags[0]
# print(len(img_tags))
# print(img_tags)

img_data_mongo = []
for i in img_tags:
    img_url = i["src"]
    img_data = requests.get(img_url).content
    my_dict = {"index": img_url, "image": img_data}
    img_data_mongo.append(my_dict)
    with open(os.path.join(save_dir, f"{query}_{img_tags.index(i)}.jpg"), "wb") as f:
        f.write(img_data)

print(img_data_mongo)