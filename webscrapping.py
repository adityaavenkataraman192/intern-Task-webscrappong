# -*- coding: utf-8 -*-
"""webscrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JSJYUSRQeXfTeHMaGXecjujZEIswQIwM
"""

from bs4 import BeautifulSoup

import urllib.request

from IPython.display import HTML

import re
import urllib
from urllib.request import urlopen

r=urllib.request.urlopen('https://www.youtube.com/').read() #requesting the url and accessing for webpage scrapping
soup=BeautifulSoup(r,'lxml')
type(soup)

print(soup.prettify()[:100]) #printing first 100 character using the  pretiffy function in order to maintain text in structured way

for link in soup.find_all('a'):   #(printing the link that are in the character of a in the source request using find all method)
  print(link.get('href'))

print(soup.getText())

print(soup.prettify())

for link in soup.find_all('a',attrs={'href':re.compile("^https")}):
  print (link)
  type(link)

from traitlets.config.loader import filefind
file=open('parsed_new.txt','w')
for link in soup.find_all():
  soup_link=str(link)
  print (soup_link)
  file.write(soup_link)
  
file.flush()
file.close()

# Commented out IPython magic to ensure Python compatibility.
# %pwd

