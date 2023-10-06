
import requests, re, base64
from bs4 import BeautifulSoup

from ..models.Extractor import Extractor
from ..models.Game import Game
from ..models.Link import Link
from ..util import jsunpack

class SportSurgeStream(Extractor):
    def __init__(self) -> None:
        self.domains = ["sportsurge.stream"]
        self.name = "SportSurgeStream"

    def get_games(self):
        games = []
        r = requests.get(f"https://{self.domains[0]}").text
        soup = BeautifulSoup(r, "html.parser")
        for game in soup.find_all("a"):
            name = game.text
            if not name:
                continue
            href = game.get("href")
            games.append(Game(name, links=[Link(href)]))
        return games

    def get_link(self, url):
        r = requests.get(url).text
        try:
            re_iframe = re.findall(r'iframe src="(.+?)"', r)[0] 
            if re_iframe.startswith("//"):
                re_iframe = "https:" + re_iframe
            r_iframe = requests.get(re_iframe, headers={"Referer": url}).text
            re_packed = re.findall(r"(eval\(function\(p,a,c,k,e,d\).+?{}\)\))", r_iframe)[0]
            deobfus_packed = jsunpack.unpack(re_packed)
            m3u8 = re.findall(r'var src="(.+?)"', deobfus_packed)[0]
        except:
            re_iframe = url
            re_atob = re.findall(r"window.atob\('(.+?)'\)", r)[0]
            m3u8 = base64.b64decode(re_atob).decode("ascii")
        return Link(m3u8, headers={"Referer": re_iframe, "User-Agent": self.user_agent})


