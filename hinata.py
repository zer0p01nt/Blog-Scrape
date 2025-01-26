from bs4 import BeautifulSoup
import requests
import certifi
import urllib.request as ulr
from dotenv import load_dotenv
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

local_path = os.environ.get("local_path")

def blog(url):
    path = f"{local_path}\\HINATA"
    r = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(r.content, "html.parser")

    date = soup.find("div", class_="c-blog-article__date").text.replace("\n","").split(" ")[0].replace(".","-")
    
    name = soup.find("div", class_="c-blog-article__name").find("a").text.split()[0]

    image = soup.find("div", class_="c-blog-article__text").find_all("img")

    count = 0

    for i in image:
        link = i["src"]
        count += 1
        ulr.urlretrieve(link, path + "\\" + date + "_" + name + "_" + str(count) + ".jpg")

    print("Download Complete!")

blog("https://www.hinatazaka46.com/s/official/diary/detail/58553?ima=0000&cd=member")