import feedparser
import os.path
import urllib2
from datetime import datetime
from BeautifulSoup import BeautifulSoup
from app.images.models import Image
from app.app_and_db import db, app
from app.startup.init_app import init_app
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
init_app(app, db)
batch = BatchDownloader()
data = batch.get_data()
base = batch.get_base_url()
a = data.split("/n")
pattern = "http://earthobservatory.nasa.gov/NaturalHazards/view.php?.*"
for i in a:
    d = i.split(" ")
    if len(d) > 2 and len(d) < 4:
        dt_str = str(d[1])
        date_published = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
        prefix = base+str(d[1])+"/"
        nh_rss = prefix+"http://earthobservatory.nasa.gov/Feeds/rss/nh.rss"
        feed = feedparser.parse(nh_rss)
        prefix = os.path.dirname(__file__)+"/../static/app/images/"
        for entry in feed["entries"]:
            link = entry["links"][0]["href"]
            summary = entry["summary"]
            title = entry["title"]
            match = re.search(pattern, link)
            if match:
                response = urllib2.urlopen(link)
                headers = response.info()
                url_data = response.read()
                soup = BeautifulSoup(url_data)
                image_div = soup.find("div",
                                      {"class": "headimage-detail"}).find('a')
                if(image_div):
                    image_url = image_div["href"]
                    image = Image()
                    image_url_array = image_url.split("/")
                    image.path = image_url_array[len(image_url_array)-1]
                    if not os.path.isfile(prefix+image.path):
                        f = urllib2.urlopen(image_url)
                        with open(prefix+image.path, "wb") as code:
                            code.write(f.read())
                    image.location = ""
                    image.lat = 00.00
                    image.lon = 00.00
                    image.add_at = datetime.now()
                    image.published_at = date_published
                    image.desc = summary
                    image.title = title
                    image.source = link
                    image.license = "PB"
                    print image.source
                    db.session.add(image)
                    db.session.commit()
