'''
The Purpose of this Code is to extract the content from a pdf file which consists of table of content for a project
Since the extracted text is not proper format i.e. same as table of content we use the code below to reformat it
For now this file only reads table of cable and generated word file for each entry in table of content.
'''


import os
import re
import fitz
import comtypes.client
from docx import Document
from docx2pdf import convert

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
        self.indexs = [i for i in range(len(self.extracted_text_from_PDF)) if re.search("^[1-9][.][0-9]*[0-9]$",self.extracted_text_from_PDF[i])] # iterating through all words and looking for number that resembles format 6.1..
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
        for j in self.relation.keys(): #iterate through keys to combine and write to word file
            document = Document() # initializes a blank document in memory
            document.add_paragraph(j + "    " + self.relation[j]) # writes the key and value pair
            n = str(j) + ".docx" # Makes the files based on key
            document.save(self.save_path + n) # actually generates and save the files
        print("Generated word files")
        return
    
    def create_pdf(self):
        for i in os.listdir(self.save_path):
            convert(i)
        return
    
if __name__ == '__main__':
    path = "D://Scripts//Demo//"
    file = fitz.open("toc.pdf")
    obj = Submittal(file,path)
