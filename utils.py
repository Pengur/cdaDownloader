import requests
from bs4 import BeautifulSoup
import randomheader
import shutil
import os
from arguments import *
from urllib.parse import unquote
import randomheader


def requestSoupGET(url: str):
    print(f"connecting to {url}")
    website = requests.get(
        url,
        headers=randomheader.RandomHeader().header()
    )
    if (website.status_code != 200):
        print(f"Error while connecting to {url}")
        print(f"status code {website.status_code}")
        exit(1)

    return BeautifulSoup(website.content, "html.parser")

def requestSoupPOST(url: str, data: dict):
    print(f"connecting to {url} using with data {data}")
    website = requests.post(
        url,
        data=data,
        headers=randomheader.RandomHeader().header()
    )
    if (website.status_code != 200):
        print(f"Error while connecting to {url}")
        print(f"status code {website.status_code}")
        exit(1)

    return BeautifulSoup(website.content, "html.parser")


def downlaod(videos: list, args: dict):
    # Prepare
    for video in videos:
        if (not (url := video.urlForQuality(args["quality"]))):
            print(f"Couldn't find url for quality {args['quality']}")
            exit(1)
        # Download
        print(f"Downloading {video.title} to {args['directory']}")
        with requests.get(url, stream=True) as r:
            with open(f"{args['directory']}/{video.title}.mp4", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print(f"Saved {video.title} to {args['directory']}")

def encodeJs(encoded_url: str):
    for remove in ("_XDDD", "_CDA", "_ADC", "_CXD", "_QWE", "_Q5", "_IKSDE"):
        encoded_url = encoded_url.replace(remove, "")
    encoded_url = "".join(chr(33 + (ord(f) + 14) % 94) if 33 <= ord(f) <= 126 else f for f in unquote(encoded_url))
    for remove, replace in {
        ".3cda.pl": ".cda.pl",
        ".2cda.pl": ".cda.pl",
        ".cda.mp4": "",
    }.items():
        encoded_url = encoded_url.replace(remove, replace)
    return rf"https://{encoded_url}.mp4"
