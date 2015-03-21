"""
Overview
========
Interfacelift (interfacelift.com) has a daily wallpaper on the homepage. I wrote
this script to get this daily image and set it as the desktop background on my
computer. I couldn't use their API because the free trial is only 100 requests,
so I went with web scraping. I use Beautiful Soup (which has excellent
documentation). This is my first web scraping script!

Getting the image
=================
The final link to the image is of the format:
http://interfacelift.com/wallpaper/<id>/<prefix><resolution>.jpg
Example:
https://interfacelift.com/wallpaper/7yz4ma1/03868_thorswell_1600x900.jpg

We obtain <id> from the JavaScript source file:
https://interfacelift.com/inc_NEW/jscript002.js
From line 161
document.getElementById(...omit...<a href=\"/wallpaper/7yz4ma1/"+...omit...";
we obtain
7yz4ma1

We obtain <prefix> from the homepage preview image's src attribute.
Example: from
src="/wallpaper/previews/03870_kaikouracoastline_medium@1x.jpg"
we obtain
"03870_kaikouracoastline_"

We can specify a number of resolutions, but at the time of this writing, we
use 1600x900.
"""

from bs4 import BeautifulSoup
import re, requests

ROOT_DOMAIN = "http://interfacelift.com"
RESOLUTION = "1600x900"

# get homepage HTML and parse with Beautiful Soup
homepage_raw = requests.get(ROOT_DOMAIN)
homepage = BeautifulSoup(homepage_raw.text)

# homepage image label
image_label = homepage.body.find_all("div", class_="wallpaper")[0]

# <id>
# id from https://interfacelift.com/inc_NEW/jscript002.js
js_id_script_url = "https://interfacelift.com/inc_NEW/jscript002.js"
js_id_script = requests.get(js_id_script_url).text
id_line = "document.getElementById('download_'+id).innerHTML = \"<a href=\\\"/wallpaper/"
id_index = js_id_script.find(id_line) + len(id_line)
id_ = js_id_script[id_index:id_index + 7]

# <prefix>
preview_src = image_label.a.img["src"]
prefix = re.search("[0-9]{5}_[A-Za-z0-9]+_", preview_src).group()

image_link = "http://interfacelift.com/wallpaper/%s/%s%s.jpg" % (
					id_, prefix, RESOLUTION)

