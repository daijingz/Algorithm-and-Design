import pymongo

DBClient = pymongo.MongoClient("mongodb://localhost:27017/")

Db1 = DBClient["Personal_Basic_Information"]

Db_list1 = DBClient.list_database_names()
if "Personal_Basic_Information" in Db_list1:
    print("The database exists.")

Db1Col1 = Db1["customers"]

print(Db1.list_collection_names())