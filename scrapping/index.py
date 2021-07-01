
import scrap
from datetime import datetime 
from dbstore import insertDocuments

#------ website 3-----

PAGE_URL_3="https://informacioncorporativa.entel.cl/files.json?category=presentations&limit=40&tags=2021&callback=jQuery18308433009245375991_1625063460594"


#list of all documents which is an instance of Document class
 
documents=[];
for year in range(13,22):
    url=PAGE_URL_3[:90]+str(year)+PAGE_URL_3[92:]
    documents.extend(scrap.scrapping_3(url));

def strToDate(date:str)->datetime:
    ## yy-mm-dd time formate
    # date_in_proper_format=date[0:10]
    return datetime.strptime(date[0:10] ,'%Y-%m-%d')
   
 

for i in range(len(documents)):
    insertDocuments(documents[i].title,strToDate(documents[i].date),documents[i].link,3)


#-----------website 2-----



PAGE_URL_2="https://investor.fb.com/feed/Event.svc/GetEventList?apiKey=F37D4FC40D0E4774887D6827E95013D5&eventSelection=0&eventDateFilter=0&includeFinancialReports=true&includePresentations=true&includePressReleases=true&sortOperator=1&pageSize=-1&tagList=&includeTags=true&year=-1&excludeSelection=0"


#list of all documents which is an instance of Document class
 
documents=[];

documents.extend(scrap.scrapping_2(PAGE_URL_2));
# print(len(documents))
# for i in range(len(documents)):
#     print(documents[i].title)
#     print(documents[i].date),
#     print(documents[i].link)

def strToDate(date:str)->datetime:
    ## mm/dd/yy time formate
   
    return datetime.strptime(date[0:10] ,'%m/%d/%Y')
   
 
for i in range(len(documents)):
    insertDocuments(documents[i].title,strToDate(documents[i].date),documents[i].link,2)