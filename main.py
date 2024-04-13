import pymongo

#  provide the mongodb localhost url to connect python
client = pymongo.MongoClient("mongodb://localhost:27017")

# Database name
database = client.sample

# collection name
collection = database['Products']

# sample data
d= {
    "companyName": "ABC",
    "product":"AI OS",
    "serviceoffered":"ML"
}

# insert above records in the collections
rec = collection.insert_one(d)

# verify the records
all_record = collection.find()

# print all records
for idx,record in enumerate(all_record):
    print(f"{idx} : {record}")