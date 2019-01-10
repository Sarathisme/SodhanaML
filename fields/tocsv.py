import pandas as pd
import openpyxl

links = open('fields.txt', 'r')
links_text = [(i.split('/')[-1])[:-1] for i in links.readlines()]

df = (pd.DataFrame(data=links_text)).T

df.to_csv('domains.csv', index=False)

writer = pd.ExcelWriter('domains.xlsx')
df.to_excel(writer, 'Domains')
writer.save()