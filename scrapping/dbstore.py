from pymongo import MongoClient 
from datetime import datetime

try:
    conn=MongoClient()
    print("connected successfully")
except:
    print("could not connect to mongodb")

# database
db = conn.freshers_project

# Created or Switched to collection names:.testing
collection = db.documents

def insertDocuments(title:str,date:datetime,link:str,num:int):
    document={
        "title":title,
        "date":date,
        "link":link,
        "num":num
    }
    collection.insert_one(document)