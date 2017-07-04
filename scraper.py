from bs4 import BeautifulSoup
import requests
import time
import re
from tokens import url


def get_info():
    r = requests.get("https://www.warmane.com/information")
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    outland = soup.find_all("div", {"class": "stats"})[1].find_all("div")

    players = str(outland[0])[5:-6]
    uptime = str(outland[1])[5:-6]
    return players, uptime


while True:
    players, uptime = get_info()
    min = int(re.search("(\d+)", uptime).group(0))
    if min < 5:
        requests.get(url + "Server reset!\n" + players)
        time.sleep(600)
    time.sleep(60)
