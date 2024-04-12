from docx import Document
import fitz
import os
import re
import comtypes.client


# fl = []
# doc = fitz.open("toc.pdf")  # document
# for page in doc:
#     words = page.get_text("words", sort=True)
#     fl += [word[4] for word in words]
# # print(fl)

# # k = [fl[i] for i in range(len(fl)) if re.search("^[1-9][.][0-9]*[0-9]$",fl[i])]
# k = [i for i in range(len(fl)) if re.search("^[1-9][.][0-9]*[0-9]$",fl[i])]
# k.append(len(fl) - 1)
# # print(k)

# s = {}
# x = 0
# y = 1
# while len(k) > 1:
#     st = ""
#     for i in range(k[x]+1,k[y]):
#         if fl[i] == "|":
#             st = st[:-2]
#             break
#         st += fl[i] + " "
#     s[fl[k[x]]] = st
#     k = k[1:]


# path = "D://Scripts//Demo//"
# for j in s.keys():
#     # print(j,s[j])
#     document = Document()
#     document.add_paragraph(j + "    " + s[j])
#     n = str(j) + ".docx"
#     document.save(path + n)
  
class Submittal():
    def __init__(self,file,path):
        self.document = file # table of content pdf file
        self.save_path = path 
        self.extracted_text_from_PDF = [] # variable holds the values read from pdf
        self.indexs = [] # will hold all the numbers for each entry
        # Example : "4.9 Machine learning" is the entry in Table of content the list will hold 4.9
        self.relation = {}
        print("Code Initialized")
        self.pdf_text_extractor()
    
    def pdf_text_extractor(self):
        for page in self.document:
            words = page.get_text("words", sort=True) # iterates through each page and extracts every word in a list
            self.extracted_text_from_PDF += [word[4] for word in words] #saving the 4th value as that is the actual word we need
        print("Extracted text")
        self.index_extractor()
            
    def index_extractor(self):
        self.indexs = [i for i in range(len(fl)) if re.search("^[1-9][.][0-9]*[0-9]$",fl[i])] # iterating through all words and looking for number that resembles format 6.1..
        self.indexs.append(len(self.extracted_text_from_PDF) - 1) # saving the value to handle last index of each page
        print("Extracted index")
        self.create_relation()
    
    def create_relation(self):
        helper_var1,helper_var2 = 0,1 # helps with iteration of indexs
        while len(self.indexs) > 1:
            helper_string = ""  # helps hold value while combining the words
            for i in range(self.indexs[helper_var1]+1,self.indexs[helper_var2]): # we iterate through indexs as the values between 2 indexs is the entire entry from table of content
                if self.extracted_text_from_PDF[i] == "|": # handles edge case for last index of each page
                    helper_string = helper_string[:-2] # we end up adding 2 extra elements so we remove it
                    break
                helper_string += self.extracted_text_from_PDF[i] + " " # adding all values to get the real string
            self.relation[self.extracted_text_from_PDF[self.indexs[helper_var1]]] = helper_string # adding relation
            self.indexs = self.indexs[1:] # removing first element for next iteration
        print("Generated Relations")
        self.create_doc()
    
    def create_doc(self):
        for j in s.keys(): #iterate through keys to combine and write to word file
            document = Document() # initializes a blank document in memory
            document.add_paragraph(j + "    " + s[j]) # writes the key and value pair
            n = str(j) + ".docx" # Makes the files based on key
            document.save(self.save_path + n) # actually generates and save the files
        print("Generated word files")
        return
    
if __name__ == '__main__':
    path = "D://Scripts//Demo//"
    file = fitz.open("toc.pdf")
    obj = Submittal(file,path)
