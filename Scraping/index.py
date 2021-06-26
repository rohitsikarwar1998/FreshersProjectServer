import scrap


PAGE_URL="https://investor.weyerhaeuser.com/events-and-presentations"

title_xpath="//div[@class='wd_title']/a/text()"
date_xpath="//div[@class='item_date wd_event_sidebar_item wd_event_date']/text()"
link_xpath="//div[@class='wd_title']/a/@href"



#list of all documents which is an instance of Document class
documents=[];
xpaths=[title_xpath,date_xpath,link_xpath]

documents.extend(scrap.scrapping(PAGE_URL,xpaths));

for i in range(len(documents)):
    print(documents[i].title,end=' ')
    print(documents[i].date,end=' ')
    print(documents[i].link,end=' ')
    print()