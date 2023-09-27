import pymongo

client = pymongo.MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
db = client.anticafe
coll = db.testHW
coll.insert_one({"_id": 1, "text":"Hello world!"})