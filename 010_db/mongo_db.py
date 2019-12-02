from pymongo import MongoClient
import pprint

client = MongoClient(host="localhost", port=27017)

collection = client["test_01"]["user"]  # 库 - 表

# ret = collection.insert_on"name":"sookie"})

# ret = collection.update_one({"name":"tommy"},{"$set":{"name":"tommywhy"}})

pprint.pprint(list(collection.find()))
