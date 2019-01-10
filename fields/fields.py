from bs4 import BeautifulSoup
fields = open("fields.html",'r')
fields_text = open("fields.txt", 'w')
bs = BeautifulSoup(fields, "html.parser")
links = []

# Extract links
for a in bs.find_all('a', href=True):
    links.append(a['href'])

# Filter links
filtered = []
for i in links:
    if i.split("/")[1] == 'wiki':
        filtered.append("https://en.wikipedia.org"+i)

# Write links into file
for i in filtered:
    fields_text.write(i+'\n')

fields_text.close()
fields.close()
