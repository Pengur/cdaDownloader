import requests
from bs4 import BeautifulSoup
import sys

import utils
import folderHandler
import videoHandler


def main():
    args = utils.setArgs(sys.argv)


    if("folder" in args["url"]):
        print("FOLDER: ", args)
        # website = folderHandler.FolderHandler(url)

    elif("video" in args["url"]):
        print("VIDEO: ", args)
        # website = videoHandler.VideoHandler(url)

    else:
        print("Url has to lead directly to video or folder on cda.pl")
        exit(1)

    # download(args)


if __name__ == "__main__":
    main()