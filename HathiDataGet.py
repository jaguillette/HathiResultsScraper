# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

from urllib import urlopen
from math import ceil
import requests
import time
import re
import csv
URLparts = []
IDs = []
URL = "http://catalog.hathitrust.org/Search/Home?type%5B%5D=callnoletters&lookfor%5B%5D=QB&filter%5B%5D=ht_availability%3AFull%20text&use_dismax=1"
Q = {'page':1}

def getURLparts():
    URLpartsTemp=[]    #defines an empty temporary list to hold query results
    urlGet0 = requests.get(URL, params=Q)
    r = re.search('of \<span class=\"strong\"\>(.*?)\<', urlGet0.text)
    pages = ceil(int(r.group(1))/20)+2
    for n in range(1,pages):    #iterates over the results pages
        Q['page']=n    #sets page in results equal to the iterative value
        urlGet = requests.get(URL, params=Q)    #uses requests module to retrieve search results page
        m = re.findall('\<a href=\"\/Record\/(.*?)\"\sclass=\"cataloglinkhref\"\>', urlGet.text)
        for i in range(len(m)):
            URLparts.append(m[i])

def getIDfromURL():
    for arg in URLparts:
        IDurl='http://catalog.hathitrust.org/Record/' + arg
        urlGet=requests.get(IDurl)
        m=re.findall('\<a href=\"http\:\/\/hdl.handle.net\/2027\/(.*?)\"', urlGet.text)
        time.sleep(1)
        for i in range(len(m)):
            IDs.append(m[i])

getURLparts()

getIDfromURL()

with open('URLparts.csv', 'wb') as csvfile:
    IDwriter=csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    IDwriter.writerow(URLparts)

with open('IDs.csv', 'wb') as csvfile:
    IDwriter=csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    IDwriter.writerow(IDs)
