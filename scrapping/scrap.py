
from datetime import datetime
from lxml import html
import requests
import json
class Document:
        def __init__(self,title,date,link) -> None:
            self.title=title
            self.date=date
            self.link=link


def scrapping_1(pageUrl:str,xpaths:list)->list:
    
    documents=[];

    #get row html document
   
    page=requests.get(pageUrl);

    #parsing the dom tree 
    tree=html.fromstring(page.content)

    titles=tree.xpath(xpaths[0])
    dates=tree.xpath(xpaths[1])
    links=tree.xpath(xpaths[2])
    
   
    
     
    h="https://investor.weyerhaeuser.com"
     
   
    if(len(links)>0):
      s=links[0]
      actual_link=h+s
    
    
      documents.append(Document(titles[0],dates[0],h+links[0]))
  
   
    return documents;  






def scrapping_3(pageUrl:str)->list:

   

    documents=[];

    #get row html document
    page=requests.get(pageUrl);
   

    #parsing the dom tree 
    data=json.loads(page.content[41:-1])
    
  

    for item in range(data['meta']['total_entries']):
       
        date_doc=data['files'][item]['created_at']
        title_doc=data['files'][item]['title']
        link_doc=data['files'][item]['file']
       
        documents.append(Document(title_doc,date_doc,link_doc))

    return documents;

def scrapping_2(pageUrl:str)->list:
  
    documents=[];

    #get row html document
    page=requests.get(pageUrl);
   

    #parsing the dom tree 
    data=json.loads(page.content)
    
  

    for item in range(len(data['GetEventListResult'])):
         path=data['GetEventListResult'][item]['DocumentPath']
         if path is None :
           pass
         else:
           date=data['GetEventListResult'][item]['StartDate']
           title=data['GetEventListResult'][item]['Title']
           link=data['GetEventListResult'][item]['DocumentPath']
       
           documents.append(Document(title,date,link))

    return documents;


def scrapping_4(pageUrl:str,xpaths:list,Hd:dict)->list:

   

    documents=[];

    #get row html document
    
    page=requests.get(pageUrl,headers=Hd);

    #parsing the dom tree 
    tree=html.fromstring(page.content)

    titles=tree.xpath(xpaths[0])
    dates=tree.xpath(xpaths[1])
    links=tree.xpath(xpaths[2])
    
  

    h="https://ir.homedepot.com"
    for i in range(len(titles)):
        if links[i].startswith("/"):
          documents.append(Document(titles[i][21:],dates[i][21:],h+links[i]))
        
        
    return documents;