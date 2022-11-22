import sys
import os
import requests
import randomheader
from urllib.parse import unquote


def request(url : str):
    print(f"Connecting to {url}...")
    try:
        return requests.get(url, headers=randomheader.RandomHeader().header()).text
    except:
        print(f"Could't connect to {url}")  
        exit(1)      



def displayHelp():
    print("To specify quality use -q or --quality with value, by default this value is best possible for every video")
    print("To specify path where video will be saved use -p or --path, by default this value is current directory")
    print("cdaDownloader [url] [argument] [argument Value]")
    print("Example: cdaDownloader https://www.cda.pl/video/64920053f -q 1080p -p /home/user/Downloads")
    exit(0)


def setArgs(args : list) -> dict:
    finalArgs = {}

    if(len(args) == 1):
        displayHelp()

    i = 1   # Skip name of file, which is counted as argument
    while(i < len(args)):
        if(args[i].startswith('-')):
            # Recognize argument
            if(args[i] == "-p" or args[i] == "--path"):
                if(args[i + 1].startswith('-')):
                    raise Exception("No value was provided for path argument")

                # else:
                finalArgs.update({"path" : args[i + 1]})
                i += 2
                if(not os.path.exists(args[i + 1])):
                    print("Provided path doesn't exists, creating new directory...")
                    warnUser()
                    os.mkdir(args[i + 1])

            elif(args[i] == "-q" or args[i] == "--quality"):
                if(args[i + 1].startswith('-')):
                    raise Exception("No value was provided for quality argument")

                finalArgs.update({"quality" : args[i + 1]})
                i += 2
            
            elif(args[i] == "-h" or args[i] == "-help"):
                displayHelp()
            
            else:
                raise Exception(f"Unknown argument {arg[i]}")

        # If it doesn't start with '-' It has to be an url
        else:
            if("url" in finalArgs):
                raise Exception("2 urls are specified")

            finalArgs.update({"url" : args[i]})
            i += 1


    if(not "url" in finalArgs):
        # raise Exception("No url was specified, please use -h or --help for help")
        displayHelp()
    
    # Fill unspecified arguments
    warning = False
    if(not "path" in finalArgs):
        currentPath = os.getcwd()
        print(f"no path was specified, using current directory ({currentPath})")
        finalArgs.update({"path" : currentPath})
        warning = 1

    if(not "quality" in finalArgs):
        print("No quality was specified, downloading best available")
        # Cannot set this for now, user could provide quality that doesn't exists
        # for that video. Quality has to be passed to the website class, where will
        # be checked for user mistakes or set to highest available value.
        finalArgs.update({"quality" : "0p"})
        warning = 1

    if(warning):
        warnUser()
    
    
    return finalArgs


def warnUser(): # Ask user if he wants to continue
    while True:
        confirmation = input("Are you okay with that? y/n ")
        if(confirmation == 'y'):
            return False
        elif(confirmation == 'n'):
            print("exiting now...")
            exit(1)
        else:
            print("Please select valid option")

# Thanks to https://github.com/sovereign527
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