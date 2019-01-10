import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords

cyberwarfare = open('keywords-cyberwarfare.txt', 'r')
unlearning = open('keywords-unsupervisedlearning.txt', 'r')

first, second = {i[:-1] for i in cyberwarfare.readlines()}, {i[:-1] for i in unlearning.readlines()}

query = [i.lower() for i in input("Enter a query: ").split(" ")]

stop_words = set(stopwords.words('english'))
query = set(query) - stop_words

score1 = len(query & first) / len(query)
score2 = len(query & second) / len(query)

print(score1, score2)
