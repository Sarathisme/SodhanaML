from urllib.request import urlopen
from os import chdir, listdir, getcwd, path

def get_words(links):
    for link in links:
        html = urlopen(link).read()
        print(html)

if __name__ == "__main__":
    chdir('webpages')
    folders = [i for i in listdir(getcwd())]
    for i in folders:
        file = ' '.join(i.split('_')) + '.txt'
        current = path.join(i, file)
        file = open(current, 'r', encoding='utf-8')
        links = [i for i in file.readlines()]
        get_words(links)