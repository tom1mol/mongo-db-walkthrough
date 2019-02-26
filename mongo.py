import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")    #use os library to set constant called MONGODB_URI using getenv method
DBS_NAME = "myTestDB"                   #another constant DBS_NAME..and give it the name of our database
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):             #mongo connect function. take url as an argument
    try:                                                    #try block
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn                                         #rtn connection object
    except pymongo.errors.ConnectionFailure as e:           #except block(pymogo throws an error connection failure)
        print("Could not connect to MongoDB: %s") % e       #print Could not... and error message(%s)
        
conn = mongo_connect(MONGODB_URI)   #call our function. mongodb_uri as argument

coll = conn[DBS_NAME][COLLECTION_NAME]  #set collection name

"""new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

coll.insert(new_doc)
"""
"""
new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/4/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]

coll.insert_many(new_docs)
"""

"""
coll.remove({'first': 'douglas'})         #new variable called documents

documents = coll.find()
"""

"""
coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})
"""

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)          
    


