import nltk
import os
nltk.download("stopwords")
from nltk.corpus import stopwords

def process_query():
    query = [i.lower() for i in input("Enter a query: ").split(" ")]

    stop_words = set(stopwords.words('english'))
    query = set(query) - stop_words
    return query

def process_name(name):
    if '(' in name:
        name.remove('(')

    if ')' in name:
        name.remove(')')

    name = ''.join([i.lower() for i in name])
    return name

def get_keywords():
    data = {}
    os.chdir('keywords')
    for _, _, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            file_name = filename.split('.')[0]
            file = open(file_name + ".txt", 'r')
            words = [i[:-1] for i in file.readlines()]
            data[file_name] = words
            process_name(list(file_name))
            data[file_name] += [i.lower() for i in file_name.split('_')]
    return data

def get_scores():
    data = get_keywords()
    query = process_query()

    scores = []
    for domain in data:
        commons = set(query) & set(data[domain])
        scores.append((domain, len(commons) / len(set(query))))

    maximum = max([score for _, score in scores])

    results = []
    for domain, score in scores:
        if len(set(process_name(list(domain)).split('_')) - set(query)) == 0:
            return [(domain, 1.0)]
        elif score == maximum:
            results.append((domain, score))

    return results

if __name__ == "__main__":
    print(get_scores())
    
