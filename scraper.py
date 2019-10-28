# coding: UTF-8
import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import json
import argparse

def clear():
    pass

def hard():
    pass

def exh():
    # アクセスするURL
    url = "https://w.atwiki.jp/sp12ex-hard/pages/12.html"

    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    refs = soup.select("h2")
    refs = filter(lambda s: bool(s.string), refs)
    refs = filter(lambda s: re.match(r"難度(\d+|\?\?\?)", s.string), refs)
    refs = map(lambda s: (s["id"], s.string[2:]), refs)
    refs = list(refs)

    suffixes = [
        ("[H]", "H")
        , ("[A]", "A")
        , ("†", "L")
        , ("†LEGGENDARIA", "L")
    ]

    musics = []

    for ref in refs:
        difficulty = ref[1]
        titles = soup.select("#{} + table tr".format(ref[0]))[1:]
        titles = map(lambda s: s.select_one("td:nth-of-type(2)").string, titles)
        for title in titles:
            mode = "A"
            for suf in suffixes:
                if title.endswith(suf[0]):
                    mode = suf[1]
                    title = title[:-1 * len(suf[0])]
                    break
            musics.append((difficulty, title, mode))

    print(json.dumps(musics, ensure_ascii=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('src', metavar='S', type=str)
    args = parser.parse_args()
    
    src = args.src
    
    if src == "clear":
        clear()
    elif src == "hard":
        hard()
    elif src == "exh":
        exh()