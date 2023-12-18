import arguments
import videoHandler
import folderHandler
import utils


def main():
    args = arguments.getArgs()
    arguments.checkArgs(args)
    if (args["type"] == "folder"):
        folder = folderHandler.Folder(args["url"], args["password"])
        utils.downlaod(folder.getVideos(), args)
    else:
        video = videoHandler.Video(args["url"])
        utils.downlaod([video], args)

if __name__ == "__main__":
    main()
