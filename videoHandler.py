from bs4 import BeautifulSoup
import requests



class VideoHandler():
    url              : str
    videoId          : str
    unfilledEmbedUrl : str

    def __init__(self, url : str, quality : str):
        self.url = url
        self.videoId = self.url.split('/')[-1] # Last part of url, which is ID
        # Set quality
        
        self.incompleteEmbedUrl = "http://ebd.cda.pl/1x1/" + self.videoId