from docx import Document
import fitz
import os
import re



fl = []
doc = fitz.open("toc.pdf")  # document
for page in doc:
    words = page.get_text("words", sort=True)
    fl += [word[4] for word in words]
# print(fl)

# k = [fl[i] for i in range(len(fl)) if re.search("^[1-9][.][0-9]*[0-9]$",fl[i])]
k = [i for i in range(len(fl)) if re.search("^[1-9][.][0-9]*[0-9]$",fl[i])]
k.append(len(fl) - 1)
# print(k)

s = {}
x = 0
y = 1
while len(k) > 1:
    st = ""
    for i in range(k[x]+1,k[y]):
        if fl[i] == "|":
            st = st[:-2]
            break
        st += fl[i] + " "
    s[fl[k[x]]] = st
    k = k[1:]

for j in s.keys():
    print(j,s[j])

