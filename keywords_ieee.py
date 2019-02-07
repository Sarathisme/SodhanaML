from urllib.request import urlopen
from lxml import etree
import os
import json


def parse(data):
    results = []
    try:
        for dat in data['keywords']:
            for i in dat['kwd']:
                if ',' in i and i.__class__ == 'str':
                    i = i.replace(',', '')
                elif ' ' in i:
                    i = [j.lower() for j in i.split(' ')]
                    results += i
                else:
                    results.append(i.lower())
    except Exception as e:
        print(e)
        pass

    return results


def retrieve_keywords(tree):
    index_in_list = 0
    start_index = 0
    content = []
    try:
        data = tree.xpath("//script['global.document.metadata =']/text()")
        for i, j in enumerate(data):
            if 'global.document.metadata' in j:
                index_in_list = i
                start_index = data[i].index('global.document')
                break
        string_text = data[index_in_list][start_index:].strip()
        string_text = string_text[string_text.index('=') + 1:-1]
        content = json.loads(string_text)
    except Exception as e:
        print(e)
        pass
    return parse(content)


def open_links_get_page(file):
    f = open(file, 'r')
    keywords = []
    for link in f.readlines():
        response = urlopen(link)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        keywords += retrieve_keywords(tree)
    return keywords

if __name__ == "__main__":
    os.chdir('webpages')
    for subdirs, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            filename = dir.replace('_', ' ')
            os.chdir(os.path.join(os.getcwd(), dir))
            print('Started retrieving keywords for ', os.path.join(os.getcwd(), 'keywords.txt'))
            keywords = open_links_get_page(os.path.join(os.getcwd(), filename + '.txt'))
            file = open(os.path.join(os.getcwd(), 'keywords.txt'), 'a')
            if len(keywords) > 0:
                for word in keywords:
                    file.write(word+'\n')
            print('Finished writing to ', os.path.join(os.getcwd(), 'keywords.txt'), "\n")
            os.chdir('..')
        break

