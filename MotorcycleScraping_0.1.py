# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Used Motorcyle Price collection

The intent of this project is to help me track used motorcycle prices
on craigs list so I can spot potential deals.  To that end, there are
three parts this will encompass, the last one being optonal to the
functionality of this program.

Part 1: Querying Craigslist and tracking posts via an RSS feed.  More
research is required to understand how the implementation of this.

Part 2: Data Storage.  Storing all data retrieved from Craigslist into
a dataframe.  Currently, the plan is to utilize SQLite to create a
database to store this data.

Part 3: Data Analysis.  Once enough data is collected, establish
baseline prices for different categories of motorcycle.  This will
aid in determining whether a posting is a deal or not.  This process
would use a quantitative supervised learning methodology.

"""

import feedparser
import pprint
from bs4 import BeautifulSoup
import requests
from io import StringIO
import numpy as np
import pandas as pd
import os

#creates an object from an RSS link of a craigslist search
feed2 = feedparser.parse('https://minneapolis.craigslist.org/search/mca?format=rss&max_engine_displacement_cc=1200&min_engine_displacement_cc=150&query=motorcycle&sort=rel')

#pulling 1 entry out of that feed to scrape
test_link = feed2.entries[1].link
print(len(feed2.entries))

#using requests to pull data from an rss feed
with requests.Session() as s:
    download = s.get(test_link)

#Create a soup from the link found in the RSS entry
soup_test = BeautifulSoup(download.content, 'html.parser')

adtitle = soup_test.find('title').text

#pulls the uniqueu id CL assigns to the ad url to use as a primary key
motoid = feed2.entries[2].id[65:-5]

#gets the working python directory, and appends the new folder name
pathname = os.getcwd()
pathname = pathname + "/" + motoid
print(pathname)
dirname = os.path.dirname(pathname)

#create a folder to store pictures
if not os.path.exists(pathname):
    os.makedirs(pathname)
    print('creation success')

#counter to number pictures
imgcount = 0

#loops through each image and stores it in a local folder
for img in soup_test.select('a.thumb'):
    imgcount += 1
    filename = (pathname +  "/" + motoid + " - "+str(imgcount)+".jpg")
    with open(filename, 'wb') as f:
        response = requests.get(img['href'])
        f.write(response.content)

#finds the listed motorcycle attributes (ie vin, engine size, mileage . . .)
clipping = soup_test.find('p','attrgroup')

#initilize a list which will have entries appended
#motorcycle = [['garb','condition','engine','fuel','odometer','color','title','transmission']]

#for the time being, motorcycle will be innitialized as an empty list
motorcycle = []

for p in soup_test.find_all('p','attrgroup'):
    print(innn)
    #print(p.text)
    clipping = p.text
    try:
        if child.name == 'span':
            print(child.text)
    except:pass
print(clipping)

'''
this is coding to grab the stats of the motorcycle and append it to a table
the if statements account for not all information being present in all ads
due to this variability a different method of pulling data will eventually
have to be implemented to decrease exceptions and bad data.

clipping = clipping.split(':')

#first, we overwrite the garbage pull with the ID#
clipping[0] = feed2.entries[1].id[-15:]
if len(clipping) > 1:
    clipping[1] = clipping[1][1:-26]
if len(clipping) > 2:
    clipping[2] = clipping[2][1:-5]
if len(clipping) > 3:
    clipping[3] = clipping[3][1:-9]
if len(clipping) > 4:
    clipping[4] = clipping[4][1:-13]
if len(clipping) > 5:
    clipping[5] = clipping[5][1:-14]
if len(clipping) > 6:
    clipping[6] = clipping[6][1:-14]
'''

motorcycle.append(clipping)
print(motorcycle)

