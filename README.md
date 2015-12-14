Overview
========
[Interfacelift](interfacelift.com) has a daily wallpaper on the homepage. I wrote this script to get this daily image and set it as the desktop background on my computer. I couldn't use their API because the free trial is only 100 requests, so I went with web scraping. I use [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) (which has excellent documentation) and [`requests`](http://docs.python-requests.org/en/latest/) (over [`urllib`](https://docs.python.org/2.7/library/urllib.html)). This is my first web scraping script!

How to use
----------
0. Make sure you have:
    1. Python 3
    2. Python's `requests` module (try `import requests` in Python)
    3. Beautiful Soup 4 (try `import bs4` in Python)
    4. `gsettings` (try `gsettings --version` in your terminal)

1. Download the script.

2. Set `RESOLUTION` and `DOWNLOAD_LOCATION` to your preferred values in `interfacelift.py`. I set this as `~/Pictures/Wallpapers/interfacelift`.

3. Run the script.

4. If you'd like, you can set up a Linux system to run the script regularly. Run `crontab -e` and add a line to the bottom according to the instructions. In your crontab line, run `interfacelift.sh`. See `interfacelift.sh` for more information about why it is requred to run that instead of `interfacelift.py`.
    * For example, I have `0 * * * * bash ~/path/to/interfacelift.sh` in my `crontab`.

Issues?
-------
If you have any issues, feel free to open an issue and I will see what I can do.
