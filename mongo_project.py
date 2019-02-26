import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
        
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter option: ")
    return option

#helper function
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:            # variable doc should hold a cursor object if we're able to find our record.
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()}) #whatever mix of case we put in our input, it'll convert it to lowercase, which will find it in our database.
    except:
        print("Error accessing the database")
        
    if not doc:     #if document not found..print blank line..then..Error
        print("")
        print("Error! No results found!")
        
    return doc
    
def add_record():
    print("")                                #prompt us to enter this information and store it in each of these variables below.
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")
    
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}     #first,lastname in lowercase..makes easier to find
    
    
    try:
        coll.insert(new_doc)                                    #document dictionary
        print("")
        print("Document inserted")                              #all goes well...document inserted
    except:
        print("Error acessing the database")        
    
    
def main_loop():                
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        
        
        
conn = mongo_connect(MONGODB_URI)   #call our function. mongodb_uri as argument

coll = conn[DBS_NAME][COLLECTION_NAME]  #set collection name

main_loop()