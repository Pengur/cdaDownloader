from bs4 import BeautifulSoup
import requests

from utils import *

class FolderHandler():
    folderId     : str
    folderAuthor : str
    siteContent  : str
    embedUrls    : list
    videoUrl     : str
    bs4          : None # Beautiful soup class

    # Get if from every video in folder
    def scrapeVideos(self, website : str):
        videoIds = []
        bs = BeautifulSoup(website, "html.parser")
        print(bs.find_all("a", class_="sister"))


    def __init__(self, url : str, quality : str):
        self.folderUrl = url
        self.siteContent = request(self.folderUrl)
        self.scrapeVideos(self.siteContent)