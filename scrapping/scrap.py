from lxml import html
import requests
import json

def scrapping(pageUrl:str)->list:

    class Document:
        def __init__(self,title,date,link) -> None:
            self.title=title
            self.date=date
            self.link=link

    documents=[];

    #get row html document
    page=requests.get(pageUrl);
   

    #parsing the dom tree 
    data=json.loads(page.content[41:-1])
    
  

    for item in range(data['meta']['total_entries']):
        # date_obj=datetime.strptime(data['files'][item]['created_at'][0:10],"%Y-%m-%d")
        # print(date_obj.year)
        date_doc=data['files'][item]['created_at']
        title_doc=data['files'][item]['title']
        link_doc=data['files'][item]['file']
       
        documents.append(Document(title_doc,date_doc,link_doc))

    return documents;

def scrapping_1(pageUrl:str)->list:
    class Document:
        def __init__(self,title,date,link) -> None:
            self.title=title
            self.date=date
            self.link=link
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
