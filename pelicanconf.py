#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Enrico Rotundo'
SITENAME = 'Enrico Rotundo\'s Blog'
SITEURL = 'https://enricorotundo.github.io'
SITELOGO =  '//avatars2.githubusercontent.com/u/4340327?s=400&u=1a4d1ea78282e967366b5c5beb0e32bd24c4236b&v=4'
SITETITLE = AUTHOR
SITESUBTITLE = '.: Data Scientist :.'

PATH = 'content'

STATIC_PATHS = ['gifs', 'images', 'files']

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

THEME='Flex'

MAIN_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Blog', 'https://medium.com/@enrico.rotundo'),
)

# Social widget
SOCIAL = (
    ('envelope-o', 'mailto:enrico.rotundo@gmail.com'),
    ('medium', 'https://medium.com/@enrico.rotundo'),
    ('github', 'https://github.com/enricorotundo'),
    ('linkedin', 'https://www.linkedin.com/in/enricorotundo'),
    ('twitter', 'https://twitter.com/EnricoRotundo'),
    ('tumblr', 'https://enrico-rotundo.tumblr.com'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISQUS_SITENAME = "https-enricorotundo-github-io"
GOOGLE_ANALYTICS = "UA-50634042-4"

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018
