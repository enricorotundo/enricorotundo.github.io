#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Enrico Rotundo'
SITENAME = "Enrico Rotundo's site"
SITEURL = 'https://www.enricorotundo.com'
SITELOGO = '/images/avatar.jpg'
SITETITLE = 'Enrico'
SITESUBTITLE = ''
SITEDESCRIPTION = "Enrico's Thoughts"

ROBOTS = "index, follow"

THEME = "Flex"
STATIC_PATHS = ['gifs', 'images', 'files', 'static']

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}
CUSTOM_CSS = "static/custom.css"

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

MAIN_MENU = False

SUMMARY_MAX_LENGTH = 2250

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Blog', '/blog'),
)

# create blog index page at /blog
INDEX_SAVE_AS = "blog.html"

# Social widget
SOCIAL = (
    ('envelope', 'mailto:enricoDOTrotundoATgmailDOTcom'),
    ('linkedin', 'https://www.linkedin.com/in/enricorotundo'),
    ('twitter', 'https://twitter.com/EnricoRotundo'),
)

DEFAULT_PAGINATION = False

# Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'


COPYRIGHT_YEAR = 2021



