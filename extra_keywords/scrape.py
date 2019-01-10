from bs4 import BeautifulSoup
from urllib.request import urlopen

# Static search url
URL = "https://ieeexplore.ieee.org/search/searchresult.jsp?action=search&newsearch=true&searchField=Search_All&matchBoolean=true&queryText="

# Extracting query names
file = open('../fields/fields.txt', 'r')
queries = ['('+'%20'.join((i.split('/')[-1][:-1]).split('_'))+')' for i in file.readlines()]

# Creating search queries
queries = [URL + query for query in queries]

# Getting html page
print(queries[0])
temp = open('sample.html', 'w')
temp.write(str(urlopen('https://ieeexplore.ieee.org/document/6506967').read()))