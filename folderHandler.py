from bs4 import BeautifulSoup
import requests

import utils
import videoHandler

class FolderHandler():
    folderId     : str
    folderAuthor : str
    siteContent  : str
    embedUrls    : list
    bs4          : None # Beautiful soup class

    # Get if from every video in folder
    def scrapeIds(self) -> list:
        videosId = []
        bs = BeautifulSoup(self.website, "html.parser")
        divs = bs.find_all("a", {"class" : "thumbnail-link"})
        for children in divs:
            videosId.append(children["href"])
        return videosId


    def download(self, path : str):
        for videoId in self.videoIds:
            video = videoHandler.VideoHandler("cda.pl" + videoId, self.givenQuality)
            i = 3
            while(i > 0):
                try:
                    video.download(path)
                except KeyboardInterrupt:
                    print("Keyboard Interruption, exiting now...")
                    exit(1)
                except:
                    i -= 1
                    if(i < 1):
                        print("Too many failed tries, exiting now...")
                        exit(1)
                        
                    print("Something went wrong, trying again")
                    print(f"{i} tries left")
                else:
                    break
            del video

    def __init__(self, url : str, quality : str):
        self.folderUrl = url
        self.website = utils.request(self.folderUrl)
        self.videoIds = self.scrapeIds()
        self.givenQuality = quality
        self.videoHandlerObjects = []



    