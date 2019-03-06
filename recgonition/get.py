import os
os.chdir('../webpages')
for i in os.listdir(os.getcwd()):
    os.chdir(i)
    file = open('keywords.txt', 'r')
    keywords = open('../../testing/keywords/' + i + ".txt", 'w')
    keywords.writelines(file.readlines())
    os.chdir('..')