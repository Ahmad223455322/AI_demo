import pandas as pd
from pymongo import MongoClient

host = "mongodb://localhost"
port = 27017
db = "test_vecka_2"
collection = "sensordata"

def _connect_mongo(host, port, db):
    conn = MongoClient(host, port)
    return conn[db]

def read_mongo(db, collection, query={}, host="mongodb://localhost", port=27017, username=None, password=None, no_id=False):
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df

_connect_mongo(host, port, db)

ourData = read_mongo(db, collection, query={}, host=host, port=port, username=None, password=None, no_id=False)


print(ourData)


