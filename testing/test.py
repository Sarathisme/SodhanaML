import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords

cyberwarfare = open('keywords-cyberwarfare.txt', 'r')
unlearning = open('keywords-unsupervisedlearning.txt', 'r')
algorithm = open('keywords-algorithm.txt', 'r')

first, second, third = {i[:-1] for i in cyberwarfare.readlines()}, {i[:-1] for i in unlearning.readlines()}, {i[:-1] for i in algorithm.readlines()}

query = [i.lower() for i in input("Enter a query: ").split(" ")]

stop_words = set(stopwords.words('english'))
query = set(query) - stop_words

score1 = len(query & first) / len(query)
score2 = len(query & second) / len(query)
score3 = len(query & third) / len(query)

print('Cyberwarfare', score1)
print('Unsupervised learning', score2)
print('Algorithm', score3)
