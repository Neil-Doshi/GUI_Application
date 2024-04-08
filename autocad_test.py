
from datetime import datetime
import fitz
import os


path = 'D:\\Delete'
os.chdir(path)
for count, f in enumerate(os.listdir()):
    doc = fitz.open(f)  # document
    page = doc[0]  # first page
    words = page.get_text("words", sort=True)  # extract sorted words
    a = []
    b = []
    for i in range(len(words)):
        if words[i][4].count("/") == 2:
            a.append(words[i][4])
        if words[i][4] == 'REV':
            b.append(i-1)
    for k in b:
        if len(words[k][4]) == 1:
            word = words[k][4]
            
    a.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
    print(f)
    print(f' Revision : {word}')
    print(f' Date     : {a[-1]}')
