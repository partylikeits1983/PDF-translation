import PyPDF2
import Split
from subprocess import call

from googletrans import Translator, constants
from pprint import pprint

filename = 'pdf.pdf'
directory = "splitted/" + filename

Split.split(directory, filename)
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):
    splitted_file_name = directory + "/" + repr(i)
    call(["pdftotext", splitted_file_name + ".pdf"])
    f = open(splitted_file_name + '.txt', 'r')
    
    data = f.read().replace('\n', '')
    translator = Translator()

    translation = translator.translate(data, src="en", dest="ru")
    
    text = translation.text

    with open('test.txt','a') as f:
        f.write(text)


