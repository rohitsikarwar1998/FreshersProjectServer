import scrap
from datetime import datetime 
from dbstore import insertDocuments


PAGE_URL="https://informacioncorporativa.entel.cl/files.json?category=presentations&limit=40&tags=2021&callback=jQuery18308433009245375991_1625063460594"


#list of all documents which is an instance of Document class
 
documents=[];
for year in range(13,22):
    url=PAGE_URL[:90]+str(year)+PAGE_URL[92:]
    documents.extend(scrap.scrapping(url));

def strToDate(date:str)->datetime:
    ## yy-mm-dd time formate
    # date_in_proper_format=date[0:10]
    return datetime.strptime(date[0:10] ,'%Y-%m-%d')
   
 

for i in range(len(documents)):
    insertDocuments(documents[i].title,strToDate(documents[i].date),documents[i].link)