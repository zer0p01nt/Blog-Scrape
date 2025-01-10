from bs4 import BeautifulSoup
import requests
import urllib.request as ulr
from dotenv import load_dotenv
import os

load_dotenv()

local_path = os.environ.get("local_path")

def blog(url):
    path = f"{local_path}\\SAKURA"
    base_url = "https://sakurazaka46.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    date = soup.find("div", class_="txt").find("p", class_="date wf-a").text[-14:-6].replace("/","")

    full_name = soup.find("div", class_="eigo-inner").find("p", class_="eigo wf-a").text
    name = full_name.split()[1]

    image = soup.find("div", class_="box-article").find_all("img")

    count = 0

    for i in image:
        link = i['src']
        result = base_url + link
        count += 1
        ulr.urlretrieve(result, path + "\\" + date + "_" + name + "_" + str(count) + ".jpg")
    
    print("Download Complete!")

blog("https://sakurazaka46.com/s/s46/diary/detail/58520?ima=0000&cd=blog")
