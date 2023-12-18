import utils
from json import loads


class Video:
    def __init__(self, url):
        #  Url
        self.id = url.split("/")[4]
        self.url = f"https://ebd.cda.pl/1x1/{self.id}"
        # Get video data
        # Soup is used only to get basic data independent of quality
        # thus any data with user quality should not be readed from this
        self.soup = utils.requestSoupGET(self.url)  # Website content
        self.title = self.soup.find("title").text.replace(" ", "_")
        # Possible qualities
        self.versions = loads(
            self.soup.find(
                "div", {"id": f"mediaplayer{self.id}"}
            ).attrs["player_data"]
        )["video"]["qualities"]

    def urlForQuality(self, quality):
        # No quality chosen means user wants best one
        if (quality == ""):
            quality = list(self.versions.keys())[-1]
        elif (not quality in self.versions.keys()):
            return 0;

        soup = utils.requestSoupGET(
            f"https://ebd.cda.pl/1x1/{self.id}/?wersja={quality}"
        )
        return utils.encodeJs(
            loads(
                soup.find(
                    "div", {"id": f"mediaplayer{self.id}"}
                ).attrs["player_data"])["video"]["file"]
        )
