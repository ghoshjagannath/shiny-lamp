#in this project we will extract data from pdf  as text and 
# print only the data what we need 

# Mr.jagannath ghosh

#it is a path for dl of a person  , we need to extract only the date for test
path=r"C:\\Users\\ghosh\Downloads\dl appointment.pdf"


#importing modules 
import PyPDF2 as pdf
import re



#we use PdfFileReader for reading and extracting string 
file=pdf.PdfFileReader(path)

#initilize first page of pdf 
page1=file.getPage(0)

#Extracted data
paragraph=page1.extractText()



# pattern for date 
date_pattern='\d{2}-\d{2}-\d{4}'


#printing the date for dl test 
# there is 3 type of date in this pdf so last one is needed
print(re.findall(date_pattern,paragraph)[2])


#printing time 
print(re.findall('\d{2}\.\d{2}-\d{2}\.\d{2}',paragraph))


#user name
print(re.findall('Dear[A-Z]+\s[A-Z]+',paragraph))

#father name
print(re.findall('S/o.\s+[A-Z]+\s+[A-Z]+',paragraph))
