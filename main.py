import requests
from bs4 import BeautifulSoup
import sys

import utils
import folderHandler
import videoHandler


def main():
    args = utils.setArgs(sys.argv)

    if("folder" in args["url"]):
        print("Creating folder object")
        website = folderHandler.FolderHandler(args["url"], args["quality"])
    elif("video" in args["url"]):
        print("Creating video object")
        website = videoHandler.VideoHandler(args["url"], args["quality"])
    else:
        print("Url has to lead directly to video or folder on cda.pl")
        exit(1)

    # folder.download is just video.download in loop
    # print(website.mp4Url)
    website.download(args["path"])

if __name__ == "__main__":
    main()