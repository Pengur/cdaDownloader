import sys
import os



def request(url : str):
    print(f"Connecting...")
    try:
        return requests.get(url)
    except err:
        raise Exception(f"Cannot connect to {url}")
        

def download(mediaUrl : str, path = ""):
    pass


def setArgs(args : list) -> dict:
    finalArgs = {}

    i = 1
    while(i < len(args)):
        if(args[i].startswith('-')):
            # Recognize argument
            if(args[i] == "-p" or "--path"):
                if(args[i + 1].startswith('-')):
                    raise Exception("No value was provided for path argument")

                # else:
                finalArgs.update({"path" : args[i + 1]})
                i += 2
                # TODO: check if provided path exists
                # If doesn't ask if user wants to create this directory

            elif(args[i] == "-q" or args[i] == "--quality"):
                if(args[i + 1].startswith('-')):
                    raise Exception("No value was provided for quality argument")

                finalArgs.update({"quality" : arg[i + 1]})
                i += 2
            
            elif(args[i] == "-h" or args[i] == "-help"):
                displayHelp()
                exit(1)
            
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
        exit(0)
    
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
        finalArgs.update({"quality" : "0"})
        warning = 1

    if(warning):
        while True:
            confirmation = input("Are you okay with that? y/n ")
            if(confirmation == 'y'):
                break
            elif(confirmation == 'n'):
                print("exiting now...")
                exit(1)
            else:
                print("Please type y or n")
    
    
    return finalArgs
