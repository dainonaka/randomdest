from bottle import route, run
import requests
from bs4 import BeautifulSoup
import random

class DestinationJp():
    def __init__(self):
        r = requests.get("https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E8%A6%B3%E5%85%89%E5%9C%B0%E4%B8%80%E8%A6%A7")
        soup = BeautifulSoup(r.content, "html.parser")
        soup_lis = soup.find_all("li")
        dest_dict = {}
        for soup_li in soup_lis:
            if soup_li:
                dest = soup_li.find("a").string
                url = soup_li.find("a").get("href")
                if dest and len(dest) <7: dest_dict[dest] = url
                elif dest: break

        dest_list = [dest for dest in dest_dict.keys() if dest and dest[-1] != "県"]
        random_dest = random.choice(dest_list)
        
        self.city = random_dest
        self.url = ("https://ja.wikipedia.org" + dest_dict[random_dest].strip(","))
        
@route("/")
def drandom_destination():
    destination = DestinationJp()
    return f"""
<div style = "text-align: center; background-color: pink;"><h2>↓あなたのおすすめ観光地↓</h2></div>
<div style = "text-align: center;"><a href = "{destination.url}", style = "font-size: 200px;">{destination.city}</a></div>"""


run(host = "localhost", port = 8080)
    
