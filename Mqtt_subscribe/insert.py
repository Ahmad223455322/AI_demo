import pymongo
import csv
import pandas
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)


# x = mycol.find_one()

# print(x)


# for x in mycol.find({},{ "address": 0 }):
#   print(x)



# myquery = { "address": "Park Lane 38" }


#den hittar boksatv som börjar med de som du söker efter, och returters resten till efter denna ordning
# myquery = { "address": { "$gt": "M" } }



# den returnerar bara som börjs med det du söker efter
# myquery = { "address": { "$regex": "^P" } }



# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)

cursor = mycol.find()

print ("total docs in collection:", mycol.count_documents( {} ))



mongo_docs = list(cursor)
mongo_docs = mongo_docs[:14]

for num,doc, in enumerate(mongo_docs):
        print(type(doc))
        print(type(doc["_id"]))
        print(num,"--",doc,"\n")


# iterate over the list of MongoDB dict documents
for num, doc in enumerate( mongo_docs ):
    
    # convert ObjectId() to str
    doc["_id"] = str(doc["_id"])

    # get document _id from dict
    doc_id = doc["_id"]


    # create a Series obj from the MongoDB dict
    series_obj = pandas.Series( doc, name=doc_id )

    # append the MongoDB Series obj to the DataFrame obj
    docs = mylist.append( series_obj )

    # export MongoDB documents to CSV
    csv_export = series_obj.to_csv(sep=",") # CSV delimited by commas

    with open("mongo.csv","w") as fil:
          data= ("\nCSV data:", csv_export) 
          writer = csv.writer(fil)

            # write a row to the csv file
          writer.writerow(data)
    
   

