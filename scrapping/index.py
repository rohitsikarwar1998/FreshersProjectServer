
import scrap
from dbstore import insertDocuments
import requests
from lxml import html
from datetime import datetime 

#------ website 1-----

documents=[];
i=51
while i<=123:
  if(i==66):
    i=i+1
    continue

  URL="https://investor.weyerhaeuser.com/events-and-presentations?item="
 
  PAGE_URL=URL+str(i)
  
  title_xpath="//div[@class='wd_attachment_title']/a/text()"
  date_xpath="//div[@class='item_date wd_event_sidebar_item wd_event_date']/text()"
  link_xpath="//div[@class='wd_attachment_title']/a/@href"

#list of all documents which is an instance of Document class
  
  xpaths=[title_xpath,date_xpath,link_xpath]
   
  documents.extend(scrap.scrapping_1(PAGE_URL,xpaths));
  # print(i)
  i=i+1
  
  
  def strToDate(date:str)->datetime:
    return datetime.strptime(date, '%A, %B %d, %Y')

for i in range(len(documents)):
    insertDocuments(documents[i].title,strToDate(documents[i].date),documents[i].link,1)


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


#-------website 4----


HEADERS={
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}


URL="https://ir.homedepot.com/events-and-presentations?async=1&page="
documents=[];
for page_no in range(7):
 
 PAGE_URL=URL+str(page_no)

 title_xpath="//span[@class='event-title']/text()"
 date_xpath="//span[@class='event-date']/text()"
 link_xpath="//p[@class='event-document event-document-1 first']/a/@href"



#list of all documents which is an instance of Document class

 xpaths=[title_xpath,date_xpath,link_xpath]

 documents.extend(scrap.scrapping_4(PAGE_URL,xpaths,HEADERS));

 def strToDate(date:str)->datetime:
    return datetime.strptime(date,'%b %d, %Y') 

for i in range(len(documents)):
    insertDocuments(documents[i].title,strToDate(documents[i].date[0:12]),documents[i].link,4)
# print(datetime.now())