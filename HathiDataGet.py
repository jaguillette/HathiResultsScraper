# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

from math import ceil
import requests
import time
import re
URLparts = []
URL = "http://catalog.hathitrust.org/Search/Home?checkspelling=true&lookfor=QB&type=callnoletters&use_dismax=1"
Q = {'checkspelling':'true', 'lookfor':'QB', 'type':'callnoletters', 'use_dismax':1, 'page':1}

def getURLparts():
    URLpartsTemp=[]    #defines an empty temporary list to hold query results
    urlGet0 = requests.get(URL, params=Q)
    r = re.search('of \<span class=\"strong\"\>(.*?)\<', urlGet0.text)
    pages = int(ceil(int(r.group(1))/20))+2
    for n in range(1,pages):    #iterates over the results pages
        Q['page']=n    #sets page in results equal to the iterative value
        urlGet = requests.get(URL, params=Q)    #uses requests module to retrieve search results page
        m = re.findall('\<a href=\"\/Record\/(.*?)\"\sclass=\"cataloglinkhref\"\>', urlGet.text)    
        for i in range(len(m)):
            URLparts.append(m[i])

getURLparts()

print(URLparts)
