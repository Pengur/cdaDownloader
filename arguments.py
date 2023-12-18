import sys
import os


def displayHelpAndExit():
    print("Cda Downlaoder by https://github.com/Pengur")
    print("Usage: python3 cda.py [url] [options]")
    print("-q [quality] - choose quality of video")
    print("-d [directory] - choose directory to save video")
    print("-p [password] - password to folder if its password protected")
    print("-h [help] - display help and exit")
    exit(0)


# Read given arguments
# Some value may be left empty
# It is up to checkArgs to decide what to do with them
def getArgs() -> dict:
    if (len(sys.argv) < 2):
        displayHelpAndExit()

    args = {
            "quality": "",
            "directory": os.getcwd(),
            "url": "",
            "password": "",
            "type": ""
    }

    i = 1
    while i < len(sys.argv):
        if (sys.argv[i].startswith("https://www.cda.pl/")):
            args["url"] = sys.argv[i]
            # Check if url is to folder or video
            if ("folder" in args["url"]):
                args["type"] = "folder"
            else:
                args["type"] = "video"
            i += 1
            continue
        if (sys.argv[i] in ("-q", "--quality")):
            args["quality"] = sys.argv[i + 1]
            i += 2
            continue
        if (sys.argv[i] in ("-d", "--directory")):
            args["directory"] = sys.argv[i + 1]
            i += 2
            continue
        if (sys.argv[i] in ("-p", "--password")):
            args["password"] = sys.argv[i + 1]
            i += 2
            continue
        if (sys.argv[i] in ("-h", "--help")):
            displayHelpAndExit()
            exit(0)
        # If none conditions were met
        print(f"Unknown argument {sys.argv[i]} exiting now...")
        exit(1)
    return args


def getUserConsent():
    print("Do you want to continue? (y/n)")
    while True:
        answer = input()
        if (answer == "y"):
            return
        elif (answer == "n"):
            print("Exiting now...")
            exit(0)
        else:
            print("Unknown answer, please type y or n")


# Check if all arguments are valid
# If not, ask user if he wants to continue with default values
def checkArgs(args: dict):
    warn = False
    if (args["url"] == ""):
        print("No url provided")
        exit(1)

    if (args["quality"] == ""):
        print("No quality provided, using default one")
        warn = True  # Store if user should be warned

    if (args["directory"] == ""):
        print("No directory provided, using current directory")
        warn = True  # Store if user should be warned

    # I really dont like this solution
    # But it is not worth to optimize one if at cost of readability
    if (warn):
        getUserConsent()
