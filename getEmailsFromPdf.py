#!/usr/bin/env python3
import os
import re
import argparse
import sys
import PyPDF2 

def main(args):

    # Make sure the file is not empty
    filesize = os.path.getsize(args.inputFile)
    if filesize == 0:
       print("emptyFile")
       sys.exit(0)

    nPages = get_page_count(args.inputFile)
#   print (nPages)

    for i in range(nPages):
        text = get_text_from_pdf(args.inputFile, i)
        emails = find_emails_in_text(text)
        if emails:
           print(emails)

def get_page_count(inputFile):
    '''
    Count the pages in the pdf file
    '''

    # creating a pdf file object
    pdfFileObj = open(inputFile, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

    # printing number of pages in pdf file
    nPages = pdfReader.numPages

    # closing the pdf file object 
    pdfFileObj.close()

    return(nPages)

def get_text_from_pdf(inputFile, pageNumber):
    '''
    Read the text from the given pdf file
    '''

    # creating a pdf file object 
    pdfFileObj = open(inputFile, 'rb') 

    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False) 

    # creating a page object 
    pageObj = pdfReader.getPage(pageNumber) 

    # extracting text from page 
    pageText = pageObj.extractText()
    #print(pageText) 

    # closing the pdf file object 
    pdfFileObj.close()

    return(pageText)

def find_emails_in_text(page):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #emails = re.findall('\S+@\S+', page) 
    emails = re.findall(regex, page) 
    return (emails)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find email addresses in the named pdf file")
    parser.add_argument('--inputFile',  action="store", help= "Specify the file to convert")
#    parser.add_argument('--outputDir',  action="store", help ="Specify absolute path for outputs")

    args = parser.parse_args()

    main(args)
