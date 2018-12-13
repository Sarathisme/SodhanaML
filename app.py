from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import wordnet as wn
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import os
# import nltk
# nltk.download("stopwords")
# nltk.download("wordnet")
# coding: utf-8

def get_webpage(link):
    folder = link.split("/")[-1]
    print(folder)
    if ":" in folder:
        folder = folder.split(":")[0]
    else:
        folder = folder[:-1]
        
    if not os.path.isdir(folder):
        os.mkdir(folder)

    html = urlopen(link)
    f = open(folder+"/webpage.html", 'w')
    f.writelines(str(html.read()))
    f.close()
    return folder

def scrape(name):
    file = open(name+"/webpage.html", 'r')
    bs = BeautifulSoup(file, "html.parser")

    # Open the paragraphs and links html files
    paragraphs, links = open(name+"/paragraphs.html", 'w'), open(name+"/links.html", 'w')

    # Extract links and text
    paragraph = bs.find_all("p")
    link = bs.find_all("a")

    # Write the links and text to files
    paragraphs.write(str(paragraph))
    links.write(str(link))

    # Close the files
    paragraphs.close()
    file.close()

def clean_text(text):
    text = re.sub("\n","", text)
    text = re.sub("[^A-Za-z]+","", text)
    return text

def clean(name):
    # Create stop words set
    stop_words = set(stopwords.words('english'))

    # Open files
    paragraphs, links = open(name+"/paragraphs.html", 'r'), open(name+"/links.html", 'r')
    para = BeautifulSoup(paragraphs, "html.parser")
    lin = BeautifulSoup(links, "html.parser")

    # Create new files
    link_text, paragraph_text = open(name+"/links.txt", 'a'), open(name+"/paragraphs.txt", 'a')
    keywords_text = open(name+"/keywords.txt", 'w')

    # Clean link file
    for a in lin.find_all('a', href=True):
        link_text.write(a['href']+"\n")

    # Clean paragraph file
    old_data = []
    for p in para.find_all("p"):
        old_data.append(p.get_text())

    data = []
    for i in range(len(old_data)):
        data.append((old_data[i]).split(" "))

    for i in range(len(data)):
        paragraph_text.writelines(data[i])

    # Tokenize and clean words
    total_data = []
    for i in data:
        for j in i:
            total_data.append(j)

    keywords_temp = []
    keywords = [clean_text(w) for w in total_data if not w in stop_words]
    for i in keywords:
        if i != "" and len(i) > 1:
            keywords_temp.append(i.lower())

    keywords_set = []
    errors = open(name+"/errors.txt", 'w')

    for i in keywords_temp:
        try:
            if wn.synsets(i)[0].pos() == 'n':
                keywords_set.append(i)
        except Exception as e:
            errors.write(i+"\n")
    
    keywords_set = set(keywords_set)

    for i in keywords_set:
      keywords_text.write(i + "\n")

if __name__ == "__main__":
    fields = open("fields.txt", 'r')
    for i in fields.readlines():
        folder = get_webpage(i)
        scrape(folder)
        clean(folder)
