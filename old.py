import requests
from bs4 import BeautifulSoup
import sys


class Website():
    url         : str
    content     : str # HTML code
    urlElements : list # site name, author name, video/folder id etc
    videosID    : list


    def __init__(self, url : str):
        self.url = url
        self.urlElements = self.splitUrl()
        print(self.urlElements)
        print(f"Reading {self.url} content...")

        try:
            self.content = requests.get(self.url)
        except:
            print(f"Couldn't conect to {self.url}")

    
    # Split url skiping empty elements
    def splitUrl(self) -> list:
        urlElements = []
        for element in self.url.split("/"):
            if(element != ""):
                urlElements.append(element)
        return urlElements
    

    def interpretWebsite(self):
        soup = BeautifulSoup(self.content, "html.parser")

        # Make sure url leads to cda
        assert Website.urlElements[1] == "www.cda.pl" "Can't connect to anything other than cda.pl"
        if(self.urlElements[2] == "folder"):
            # Read id of every video in folder
            videoContainers = soup.find_all("a", {"class" : "data-file_id"})
            print(videoContainers)

        elif(self.urlElements[2] == "video"):
            # Get video id
            self.videosID.append(self.urlElements[3])
            print("video Url is: ", self.urlElements[3])

        else:
            print("pass url to folder or video")
            exit(1)


def displayHelp():
    # TODO: add help command
    print("I wass supposed to do this later, if you can read this I forgot about it")


def readArgs(args : list) -> list:
    finalArgs = []

    # Iterate through every argument to recognize it
    i = 1 # Skip main.py
    while(i < len(args)):
        if(args[i].startswith('-')):
            # Recognize argument
            if(args[i] == "-p" or "--path"):
                finalArgs.append(["path", args[i + 1]])
                i += 2

            elif(args[i] == "-q" or args[i] == "--quality"):
                finalArgs.append(["quality", args[i + 1]])
                i += 2

            elif(args[i] == "-r" or args[i] == "--recursive"):
                finalArgs.append(["recursive", None])
            
            elif(args[i] == "-h" or args[i] == "-help"):
                displayHelp()
                exit(0)
            
            else:
                print("Unknown argument: ", args[i])
                exit(1)

        # if It doesnt start with '-' It has to be an url
        else:
            finalArgs.append(["url", args[i]])
            i += 1

    return finalArgs


def download(videosID : list, args : list):
    print(args)


def main():
    args = readArgs(sys.argv)

    for arg in args:
        if(arg[0] == "url"):
            # Make sure there is only one URL specified
            if(not("url" in locals())):
                url = arg[1]
            else:
                print(f"2 urls are specified, previous one is: {url}", end="")
                print(f"encountered: {arg[1]}")
                exit(1)
            # Dont stop iteration to make sure there isnt any other url

    # Check if there is any url specified in arguments
    if (not "url" in locals()):
        print("no url was specified, please use --help or -h for help")
        exit(1)

    website = Website(url)

    # download(website.videosID, args)


if __name__ == "__main__":
    main()