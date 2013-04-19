# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from urllib import urlopen
import requests
from bs4 import BeautifulSoup
import time
import re
URL = "http://www.cfa.harvard.edu/news/1994/press.html"

# <codecell>

urlGet = requests.get(URL)

# <codecell>

print urlGet

# <codecell>

m = re.search('\<a href=\"\/Record\/(.*?)\"\sclass=\"cataloglinkhref\"\>', str(urlopened))
m.group(1)

# <codecell>

scrapeTarget = BeautifulSoup(urlopened)

# <rawcell>

# r'\<a href=\"\/Record\/(.*?)\"\sclass=\"cataloglinkhref\"\>'

# <codecell>

body = scrapeTarget.body
div1 = body.find(id='doc3')
div2 = div1.find(id='contentContainer')
div3 = div2.find(id='bd')
div4 = div2.find(class_='yui-main content')
div5 = div2.find(class_="yui-b first contentbox")
div6 = div5.form.find(class_='result record1')
div7 = div6.div.div.find(class_='resultitem')
div8 = div7.find(class_='AccessLink')
div8.li
print div8

# <codecell>

body.contents

# <codecell>


