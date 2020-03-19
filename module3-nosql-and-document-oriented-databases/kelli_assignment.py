import pymongo

# MongtoDB is used as a non-relational database. Instead of having a schema made up of keys to index into, it is
# a documented oriented database where you throw keys at it to get specific values. Because of this, it scales
# much better. From what I know so far, it seems like mongoDB or noSQL is more useful for when we have so much
# data that a relational database can't really handle it. The data may need to be stored over multiple systems....
# idk. 

# get a mongo client database!
import json

client = pymongo.MongoClient("mongodb://<user>:<password>abEqXA4j8EBEq0YS@cluster0-shard-00-00-e9lir.mongodb.net:27017,cluster0-shard-00-01-e9lir.mongodb.net:27017,cluster0-shard-00-02-e9lir.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

# mongo client db object 
db = client["characters"]


json_file: list
with open("./test_data.json", "r") as f:
    json_file = json.load(f)



for document in json_file:
    # get the name of the collection
    collection = db[document["model"]]
    collection.insert_one(document)
    print(f"Inserting document {document}")

example = db["charactercreator.thief"].find_one()
print(example)
