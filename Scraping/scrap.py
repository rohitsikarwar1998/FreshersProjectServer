from lxml import html
import requests

def scrapping(pageUrl:str,xpaths:list)->list:

    class Document:
        def __init__(self,title,date,link) -> None:
            self.title=title
            self.date=date
            self.link=link

    documents=[];

    #get row html document
    page=requests.get(pageUrl);

    #parsing the dom tree 
    tree=html.fromstring(page.content)

    titles=tree.xpath(xpaths[0])
    dates=tree.xpath(xpaths[1])
    links=tree.xpath(xpaths[2])

    for i in range(len(titles)):
        documents.append(Document(titles[i],dates[i],links[i]))

    return documents;


