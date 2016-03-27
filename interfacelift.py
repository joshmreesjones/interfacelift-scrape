"""
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
from subprocess import call
import os, re, requests



ROOT_DOMAIN = "http://interfacelift.com"
RESOLUTION = "1600x900"
DOWNLOAD_LOCATION = "/home/josh/Pictures/Wallpapers/interfacelift"

DEBUGGING = True

def print_debug(message):
    if (DEBUGGING): print(message)



# Get homepage HTML and parse with Beautiful Soup
homepage_raw = requests.get(ROOT_DOMAIN)
homepage = BeautifulSoup(homepage_raw.text)
print_debug("Homepage downloaded.")



# Homepage image label
image_label = homepage.body.find_all("div", class_="wallpaper")[0]



# Find <id>
# id from https://interfacelift.com/inc_NEW/jscript002.js
js_id_script_url = "https://interfacelift.com/inc_NEW/jscript002.js"
js_id_script = requests.get(js_id_script_url).text
id_line = "document.getElementById('download_'+id).innerHTML = \"<a href=\\\"/wallpaper/"
id_index = js_id_script.find(id_line) + len(id_line)
id_ = js_id_script[id_index:id_index + 7]

print_debug("<id> part of path found: " + id_)



# Find <prefix>
preview_src = image_label.a.img["src"]
prefix = re.search("[0-9]{5}_[A-Za-z0-9]+_", preview_src).group()

print_debug("<prefix> parth of path found: " + prefix)



# Construct image URL
image_url = "http://interfacelift.com/wallpaper/%s/%s%s.jpg" % (id_, prefix, RESOLUTION)
print_debug("Final image URL: " + image_url)



# Create download location if it doesn't exist
if not os.path.isdir(DOWNLOAD_LOCATION):
    print_debug("Download location not found. Creating " + DOWNLOAD_LOCATION)
    os.makedirs(DOWNLOAD_LOCATION)



# Download the image
local_filename = image_url.split("/")[-1]
local_file_path = DOWNLOAD_LOCATION + "/" + local_filename
file_exists = os.path.isfile(local_file_path)

if (file_exists):
    print_debug("Current Interfacelift image already downloaded. Skipping download.")
else:
    # Download the image if it's not downloaded already
    print_debug("Downloading file\n\tfrom: " + image_url + "\n\tto: " + local_file_path)

    # Code from: http://stackoverflow.com/q/16694907/1697249
    r = requests.get(image_url, stream=True)
    if r.status_code == 404:
        print("HTTP 404 occurred when downloading the image.")
    with open(local_file_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        print_debug("File downloaded.")



# Update desktop background
command = "gsettings set org.gnome.desktop.background picture-uri file://" + local_file_path
print_debug("Running " + command)
call(command.split(" "))
