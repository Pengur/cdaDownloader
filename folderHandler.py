import utils
import videoHandler
import arguments

class Folder:
    # folderinputPassword: "Samper"
    def __init__(self, url, password = ""):
        self.url = url
        # Check if folder is password protected
        self.soup = utils.requestSoupGET(self.url)
        if (self.soup.find("input", {"id": "folderinputPassword"})):
            self.tryPassword(password)
        # if not there is nothing to do


    # returns list of video objects
    def getVideos(self):
        # Get every video and append its id to list
        videos = self.soup.find_all("a", {"class": "thumbnail-link"})
        urls = []
        for video in videos:
            urls.append(f"https://cda.pl{video['href']}")

        # Create video objects
        print(urls)
        videoObjects = []
        for url in urls:
            videoObjects.append(videoHandler.Video(url))

        print(urls)
        return videoObjects

    def tryPassword(self, password):
        if(password == ""):
            print("Folder is password protected")
            print("Enter password using -p argument")
            exit(0)

        self.soup = utils.requestSoupPOST(
            self.url,
            {"folderinputPassword": f'{password}'}
        )
        # If there still is password prompt then password is incorrect, abort
        if (self.soup.find("input", {"id": "folderinputPassword"})):
            print("Password is incorrect")
            exit(0)
        # If there is no prompt then continue, as soup is already changed


