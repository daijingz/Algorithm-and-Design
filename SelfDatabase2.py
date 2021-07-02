# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Self database 1: MongoDB (pymongo) database
import pymongo

# Build a pymongo database client first
DBClient = pymongo.MongoClient("mongodb://localhost:27017/")

Db1 = DBClient["Personal_Basic_Information"]

Db_list1 = DBClient.list_database_names()
if "Personal_Basic_Information" in Db_list1:
    print("The database exists.")

Db1Col1 = Db1["customers"]

print(Db1.list_collection_names())