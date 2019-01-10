import os
from shutil import copy2

os.chdir('attachments')
path = os.getcwd()

files = [('_'.join((''.join(f.split('.')[:-1])).split(' ')), f) for f in os.listdir(path)]

os.chdir('..')
dst = os.path.join(os.getcwd(), 'webpages')
src = os.path.join(os.getcwd(), 'attachments')

for folder, file in files:
    copy2(os.path.join(src, file), os.path.join(dst, folder))
