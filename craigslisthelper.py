# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:22:32 2019

@author: Slave II
"""
import requests

#method to scrape images listed in the ad and save them to a folder
def image_scraper(pathname, moto_tag, soup):
    
    imgcount = 0

    #loops through each image and stores it in a local folder
    for img in soup.select('a.thumb'):
        imgcount += 1
        filename = (pathname +  "/" + moto_tag + " - "+str(imgcount)+".jpg")
        with open(filename, 'wb') as f:
            response = requests.get(img['href'])
            f.write(response.content)
    
    return (imgcount)


#finds the motorcyle stats listed in the ad, and appends them to the list 
#started in the main program with the motorcycle id
def stat_collector(re, clipping, motorcycle):
    if re.search(r'([(]CC[)]: )', clipping):
        motorcycle.append(re.search(r'([(]CC[)]: )(\d*)', clipping).group(2))
    else:
        motorcycle.append(re.match(r'([(]CC[)]: )', clipping))

    if re.search(r'(condition)', clipping):
        motorcycle.append(re.search(r'(condition: )(\w*)', clipping).group(2))
    else:
        motorcycle.append(re.match(r'(condition)', clipping))

    if re.search(r'(odometer:)', clipping):
        motorcycle.append(re.search(r'(odometer: )(\d*)', clipping).group(2))
    else:
        motorcycle.append(re.match(r'(odometer)', clipping))

    if re.search(r'(VIN:)', clipping):
        motorcycle.append(re.search(r'(VIN: )(\w*)', clipping).group(2))
    else:
        motorcycle.append(re.match(r'(VIN:)', clipping))

    if re.search(r'(color:)', clipping):
        motorcycle.append(re.search(r'(color: )(\w*)', clipping).group(2))
    else:
        motorcycle.append(re.match(r'(color:)', clipping))

    if re.search(r'(status:)', clipping):
        motorcycle.append(re.search(r'(status: )(\w*)', clipping).group(2))
    else:
        motorcycle.append(re.match(r'(status:)', clipping))
    