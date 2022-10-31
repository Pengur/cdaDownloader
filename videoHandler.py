from bs4 import BeautifulSoup
import requests
from json import loads
import utils



class VideoHandler():
    url                 : str
    quality             : str
    videoId             : str
    possibleQualities   : str
    website             : str
    mp4Url              : str

    

    # Check if user's quality choice is valid
    def checkVideoQuality(self, givenQuality : str):
        self.website = utils.request(f"http://ebd.cda.pl/1920x1080/{self.videoId}/?wersja={givenQuality}")

        # Read video's quality and possible qualities for this video
        self.soup              = BeautifulSoup(self.website, "html.parser")
        # In case provided by user quality doesn't exist cda will set it to 480p by default
        self.quality           = loads(self.soup.find("div", {"id": f"mediaplayer{self.videoId}"}).attrs["player_data"])["video"]["quality"]
        # List of possible qualities for video
        self.possibleQualities = loads(self.soup.find("div", {"id": f"mediaplayer{self.videoId}"}).attrs["player_data"])["video"]["qualities"]
        self.bestQuality       = list(self.possibleQualities.keys())[-1] # Best quality is always last element of possible qualities
        
        # Check if given quality in one of the possible qualities
        # print(type(self.possibleQualities.keys()))
        for key in list(self.possibleQualities.keys()):
            if(key == givenQuality):
                self.quality = givenQuality # = self.bestQuality
                return

        # Else ask user if he's okay with best possible quality
        # If quality is equal to 0 user agreed before he wants best quality
        if(givenQuality != "0p"):
            print(f"Video with quality {givenQuality} doesn't exists, continuing with best quality")
            utils.warnUser()

        self.website = utils.request(f"http://ebd.cda.pl/1920x1080/{self.videoId}/?wersja={self.bestQuality}")
        self.soup = BeautifulSoup(self.website, "html.parser")
        self.quality = self.bestQuality
        return
        
        # Set quality to best possible, which is always last element of possibleQualities
        self.quality = bestQuality
        

    def setMp4Url(self):
        self.mp4Url = utils.encodeJs(loads(self.soup.find("div", {"id": f"mediaplayer{self.videoId}"}).attrs["player_data"])["video"]["file"])


    def download(self, path : str):
        url = self.mp4Url
        nameWithPath = path + '/' + self.videoTitle + ".mp4"
        print(f"Downloading {self.videoTitle} to {path}")
        r = requests.get(url)
        with open(nameWithPath, 'wb') as file:
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    file.write(chunk) 
        file.close()
        print("Downloading complete!")
        

    def __init__(self, url : str, givenQuality : str):
        self.url = url
        self.videoId = self.url.split('/')[-1] # Last part of url, which is ID
        self.checkVideoQuality(givenQuality)
        self.videoTitle = (self.soup.title.text).replace(" ", "_") # I really don't want any spaces in file names
        self.setMp4Url()