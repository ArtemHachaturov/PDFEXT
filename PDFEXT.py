
from PyPDF2 import PdfReader, PdfWriter
from tqdm import trange
from time import sleep

#Data input
print('\n***WELCOME TO PDFEXT SUPERACTION PROGRAM V1.0.0 BETA VERSION***')

print('\n\033[31m   Before performing certain manipulations with a PDF document, do the following:\n1. Make sure that the document consists exclusively of files that should be disassembled by name, remove the rest of the files from the PDF.\n2.Check the value of the name in the files, for the absence of instances and the same font size.\033[0m')

enter =  input('\nIf you read successfully, press ENTER...')

#Read the file
while True:
    try:
        inpNameFile = input('\n\033[32m>>>Enter the name of the document to form into separate sheets...for example:\033[31m File for testing...\033[32m\033[0m')
        reader = PdfReader(inpNameFile+ str('.pdf'))
        if reader == reader:
                break
    except:
        print('\n***File with the given name' ' ' '"' + str(inpNameFile)+ '"' ' ' 'not found, please try again...***')
        
inpNamelist = input('\n\033[32m>>>Enter the name of the file indicated on the first page...for example: \033[31m 1AI1...\033[0m ')

#Remove the number of pages
numPages = len(reader.pages)

#Create empty lists 
parts0 = []
parts1 = []

print('\n Just a moment, data is being retrieved to determine the file name\n')
for i in trange(numPages):
    #Обращаемся к первой страницы файла 
    page = reader.pages[i]
    #Put page text and font height into lists 
    def visitor_body(text, cm, tm, fontDict, fontSize):

        parts0.append(text) 
        parts1.append(fontSize)
                
    page.extract_text(visitor_text=visitor_body)

#Retrieve the text index from the list 
indexNum = parts0.index(str(inpNamelist))

#Find the font height by index
inpFontSize =  parts1[indexNum]

print('\n Assignment and unpacking has already begun\n')
for b in trange(numPages):
        parts = [] 
        page = reader.pages[b]
        #Place the height of the text found by the index and find it in this sheet using the comparison tool, after which we remove this text and use it as the file name.
        def visitor_body1(text, cm, tm, fontDict, fontSize):
        
            if fontSize == float(inpFontSize):
                parts.append(text)

        page.extract_text(visitor_text=visitor_body1)
        text_body = "".join(parts)

        #Save the file with a specific name for each sheet
        pdfWriter = PdfWriter()
        pdfWriter.add_page(page)
        fileName = str(text_body) + '.pdf'
        newFile = open(fileName, 'wb')
        pdfWriter.write(newFile) 
         
print('\nALL IS READY!')  
print('\nNow you can start colonizing planets!')    

sleep(10)
    



    
    
    
    
