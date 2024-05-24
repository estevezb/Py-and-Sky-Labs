# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://estevezb.github.io/Fly-in-the-Ointment"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

MENUITEMS = (
    ('About Me', '{filename}/pages/about-me.md'),
    ('Python Examples', '{filename}/category/python-examples.md'),
    ('Tornado Analysis', '{filename}/category/tornado-analysis.md'),
)

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""