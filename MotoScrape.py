# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

"""
Used Motorcyle Price collection
The intent of this project is to help me track used motorcycle prices
on craigs list so I can spot potential deals.
Part 1: Querying Craigslist and tracking posts via an RSS feed.  More
research is required to understand how the implementation of this.
Part 2: Data Storage.  Storing all data retrieved from Craigslist into
a dataframe.  Currently, the plan is to utilize SQLite to create a
database to store this data.
"""

#import feedparser
import pprint
from bs4 import BeautifulSoup
import requests
from io import StringIO
import numpy as np
import pandas as pd
import os
import re
import craigslisthelper as CLH

'''
#creates an object from an RSS link of a craigslist search
feed2 = feedparser.parse('https://minneapolis.craigslist.org/search/mca?format=rss&max_engine_displacement_cc=1200&min_engine_displacement_cc=150&query=motorcycle&sort=rel')

#pulling 1 entry out of that feed to scrape
test_link = feed2.entries[1].link
print(len(feed2.entries))
'''
test_link = 'https://minneapolis.craigslist.org/wsh/mcy/d/saint-paul-yamaha-yzf-r1/6941099183.html'

#using requests to pull data from an rss feed
with requests.Session() as s:
    download = s.get(test_link)

#Create a soup from the link found in the RSS entry
soup_test = BeautifulSoup(download.content, 'html.parser')

adtitle = soup_test.find('title').text

'''
#pulls the uniqueu id CL assigns to the ad url to use as a primary key
motoid = re.search(r'(\d*)(.html)', feed2.entries[2].id).group(1)
'''
motoid = 'ScrapeTest'

#gets the working python directory, and appends the new folder name
pathname = os.getcwd()
pathname = pathname + "/" + motoid
print(pathname)
dirname = os.path.dirname(pathname)

#create a folder to store pictures
if not os.path.exists(pathname):
    os.makedirs(pathname)
    print('creation success')

#calling ImageScrap module to create a folder with pictures and return picture count
imgcount = CLH.image_scraper(pathname, motoid, soup_test)





#finds the listed motorcycle attributes (ie vin, engine size, mileage . . .)
clipping = soup_test.find('p','attrgroup')
print(clipping)

#initilize a new list starting with the unique page id, then appending stats as we scrape them
motorcycle = [motoid]
motorcycle.append(clipping.text[1:-2])
for p in soup_test.find_all('p','attrgroup'):
    clipping = p.text
    try:
        if child.name == 'span':
            print(child.text)
    except:pass
print(clipping)

'''
this is coding to grab the stats of the motorcycle and append it to a list.
the if statements account for not all information being present in all ads
'''

CLH.stat_collector(re, clipping, motorcycle)


#print(feed2.entries[1].id)
#if regex grabs are within a loop, precompiling will save computational time

print(motorcycle)