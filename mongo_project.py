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

#searches to find/edit/delete records are based on NAME
#helper function. store first name first, last name last,
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:            # variable doc should hold a cursor object if we're able to find our record.
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})     # our key is 'first'
                                #whatever mix of case we put in our input, it'll convert it to lowercase, which will find it in our database.
    except:
        print("Error accessing the database")
        
    if not doc:     #if document not found(empty)..print blank line..then..Error
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
    
    #dictionary to insert into database
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}     #first,lastname in lowercase..makes easier to find
    
    
    try:
        coll.insert(new_doc)                                    #document dictionary
        print("")
        print("Document inserted")                              #all goes well...print document inserted
    except:
        print("Error acessing the database")   
        
        
        

def find_record():
    doc = get_record()
    if doc:                 #if there's results...print blank line first
        print("")           #k,v = keys,values
        for k,v in doc.items(): #calling the items method here to step through each individual value in our dictionary.
            if k != "_id":      #  check if key is not equal to ID. ID is default key created by MONGO
                print(k.capitalize() + ": " + v.capitalize())       #capitalize..first letter capitalized
                
                

def edit_record():
    doc = get_record()      #store results of get_record function in doc
    if doc:                 #check to see if something is in the dictionary
        update_doc={}   #create empty dictionary called update_doc. we will add to that dictionary. We're going to build that as we go on to                 iterate through our keys and our values.
                        #That dictionary forms the basis of what we're going to use and insert into the database.
        print("")
        for k, v in doc.items():        #iterate through using k, v
            if k != "_id":              #filter out ID field as we dont want to edit that
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                #add to update_doc dictionary..provide the key for it..and the value(v) will be = our input. we want the value to appear in these square brackets so that we can see what the current value of them is.We should get a prompt that contains both the key and what the value is currently set to.
                
                if update_doc[k] == "":   #if nothing is entered into update_doc(left blank)
                    update_doc[k] = v       #leave it as it was before(dont delete it)
                    
        try:
            coll.update_one(doc, {'$set': update_doc}) #current doc we want to update. dictionary we pass in is update_doc
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")
            

def delete_record():
    
    doc = get_record()      #store results of get_record in doc
    
    if doc:     #check if any results are returned
        print("")
        for k,v in doc.items():     #iterate through and print each of the values to ensure we delete the right document
            if k != "_id":          #filter out the ID(dont want to delete that)
                print(k.capitalize() + ": " + v.capitalize())   #colon seperating key(k) and value(v) and capitalize 1st letter of each
                
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")        #new var called confirmation. store results of input                                                                                 statement
        print("")
        
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database")
        else:                                           #anything other than Y typed
            print("Document not deleted")            #print this and return to main menu
    
    
    
def main_loop():                
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")
        
        
        
conn = mongo_connect(MONGODB_URI)   #call our function. mongodb_uri as argument

coll = conn[DBS_NAME][COLLECTION_NAME]  #set collection name

main_loop()