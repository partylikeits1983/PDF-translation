import PyPDF2
from subprocess import call
import sys

#split function
from PyPDF2 import PdfFileWriter, PdfFileReader
import os, errno

#google translate
from googletrans import Translator, constants
from pprint import pprint

def split(directory, filename):
    inputpdf = PdfFileReader(open(filename, "rb"))
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(directory+ "/%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

#define pdf file
filename = '/home/ubuntu/Desktop/pdf.pdf'
directory = "splitted/" + filename

split(directory, filename)

pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):
    splitted_file_name = directory + "/" + repr(i)
    call(["pdftotext", splitted_file_name + ".pdf"])
    f = open(splitted_file_name + '.txt', 'r')
    
    data = f.read().replace('\n', '')
    translator = Translator()

    translation = translator.translate(data, src="en", dest="ru")
    print(translation)
      

if __name__ == "__main__":
    split(directory, filename)

