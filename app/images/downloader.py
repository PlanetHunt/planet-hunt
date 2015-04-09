import feedparser
import os.path
import urllib2
from BeautifulSoup import BeautifulSoup
from app.images.models import Image
from app.app_and_db import db
import re


class BatchDownloader:
    def __init__(self):
        self.archive_file = "/../static/app/archive.org.mem"
        with open(os.path.dirname(__file__)+self.archive_file, "r") as myfile:
            self.data = myfile.read()
        self.base_url = "https://web.archive.org/web/"

    def get_data(self):
        return self.data

    def get_base_url(self):
        return self.base_url

batch = BatchDownloader()
data = batch.get_data()
base = batch.get_base_url()
a = data.split("/n")
pattern = "http://earthobservatory.nasa.gov/NaturalHazards/view.php?.*"
for i in a:
    d = i.split(" ")
    if len(d) > 2 and len(d) < 4:
        print d[1]
        prefix = base+str(d[1])+"/"
        nh_rss = prefix+"http://earthobservatory.nasa.gov/Feeds/rss/nh.rss"
        feed = feedparser.parse(nh_rss)
        for entry in feed["entries"]:
            match = re.search(pattern, entry["links"][0]["href"])
            if match:
                response = urllib2.urlopen(entry["links"][0]["href"])
                headers = response.info()
                url_data = response.read()
                soup = BeautifulSoup(url_data)
                image_div = soup.find("div", { "class" : "headimage-detail" }).find('a')
                if(image_div):
                    print image_div["href"]
