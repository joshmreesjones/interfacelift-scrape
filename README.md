Overview
========
[Interfacelift](interfacelift.com) has a daily wallpaper on the homepage. I wrote this script to get this daily image and set it as the desktop background on my computer. I couldn't use their API because the free trial is only 100 requests, so I went with web scraping. I use [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) (which has excellent documentation) and [`requests`](http://docs.python-requests.org/en/latest/) (over [`urllib`](https://docs.python.org/2.7/library/urllib.html)). This is my first web scraping script!

How to use
----------
0. Make sure you have Beautiful Soup 4, Python's `requests`, and Python 3. Make sure you run something that has `gsettings` (I run Ubuntu 14.04).

1. Download the script.

2. Set `RESOLUTION` and `DOWNLOAD_LOCATION` to your preferred values in `interfacelift.py`.

3. Run the script.

4. If you'd like, you can set up a Linux system to run the script regularly. Run `crontab -e` and add a line to the bottom according to the instructions. For example, to run it at 4:00 am every morning, I put `0 4 * * * python /path/to/interfacelift.py`.
