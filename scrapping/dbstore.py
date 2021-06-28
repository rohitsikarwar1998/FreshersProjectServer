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

def insertDocuments(title:str,date:datetime,link:str):
    document={
        "title":title,
        "date":date,
        "link":link,
    }
    collection.insert_one(document)