#pull list of scifi cons from wikipedia and count them by city in TX and state in US, then plot on maps

import os
import re
import sys
import urllib.request
from bs4 import BeautifulSoup
import datetime as dt
from html.parser import HTMLParser
import HWhtml
import string

def urlget(url,endfile):
#pull html from website and save as local file
  try:
      ufile = urllib.request.urlopen(url)
      udict = dict(ufile.info())
      if 'text/html' in udict['Content-Type']:
        text=str(ufile.read())
        h=open(endfile,'w')
        h.write(text)
        h.close()
  except IOError:
    print('problem reading url:', url)
