import motor.motor_asyncio
from datetime import datetime


MONGO_DETAILS="mongodb://localhost:27017"

client=motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# freshers_project is database name
database=client.freshers_project

documentCollection=database.get_collection("documents")

def documentHelper(document)->dict:
    return {
        "id":str(document["_id"]),
        "title":document["title"],
        "date":document["date"],
        "link":document["link"],
    }

def filter(documents:list,date:str):
    newDocuments=[]
    for document in documents:
        if document["date"]!=date:
            newDocuments.append(document)
    return newDocuments

async def retrieveDocuments(num:int,startDate:datetime):
    documents=[]
    if num==0:
        async for document in documentCollection.find({"date":{"$lt":startDate}}).limit(20):
            documents.append(documentHelper(document))
    else:
        async for document in documentCollection.find({"$and":[{"date":{"$lt":startDate}},{"num":{"$eq":num}}]}).limit(20):
            documents.append(documentHelper(document))
        
    if len(documents)!=0:
        date=documents[len(documents)-1]["date"];
        # print(date)
        documents=filter(documents,date);
    return documents