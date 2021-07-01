import scrap
from datetime import datetime 
from dbstore import insertDocuments


PAGE_URL="https://investor.fb.com/feed/Event.svc/GetEventList?apiKey=F37D4FC40D0E4774887D6827E95013D5&eventSelection=0&eventDateFilter=0&includeFinancialReports=true&includePresentations=true&includePressReleases=true&sortOperator=1&pageSize=-1&tagList=&includeTags=true&year=-1&excludeSelection=0"


#list of all documents which is an instance of Document class
 
documents=[];

documents.extend(scrap.scrapping_1(PAGE_URL));
# print(len(documents))
# for i in range(len(documents)):
#     print(documents[i].title)
#     print(documents[i].date),
#     print(documents[i].link)

def strToDate(date:str)->datetime:
    ## mm/dd/yy time formate
   
    return datetime.strptime(date[0:10] ,'%m/%d/%Y')
   
 

for i in range(len(documents)):
    insertDocuments(documents[i].title,strToDate(documents[i].date),documents[i].link)
