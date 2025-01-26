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
    path = f"{local_path}\\NOGI"
    base_url = "https://www.nogizaka46.com"
    r = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(r.content, "html.parser")

    date = soup.find("p", class_="bd--hd__date a--tx js-tdi").text.replace(".","")[2:8]

    name = soup.find("p", class_="bd--prof__name f--head").text
    
    image = soup.find("div", class_="bd--edit").find_all("img")

    count = 0

    for i in image:
        link = i["src"]
        result = base_url + link
        count += 1
        ulr.urlretrieve(result, path + "\\" + date + "_" + name + "_" + str(count) + ".jpg")

    print("Download Complete!")

blog("https://www.nogizaka46.com/s/n46/diary/detail/103015?ima=3521")