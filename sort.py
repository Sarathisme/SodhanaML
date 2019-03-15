import os
from shutil import copy2

os.chdir('attachments')
path = os.getcwd()

files = []
for f in os.listdir(path):
    names = f.split('.')[0].split(' ')
    files.append(('_'.join(names), f))

os.chdir('..')
dst = os.path.join(os.getcwd(), 'webpages')
src = os.path.join(os.getcwd(), 'attachments')

for folder in os.listdir(dst):
    file = ' '.join(folder.split('_')) + '.txt'
    open(os.path.join(os.path.join(dst, folder), file), 'w', encoding='utf-8')

for folder, file in files:
    copy2(os.path.join(src, file), os.path.join(dst, folder))
