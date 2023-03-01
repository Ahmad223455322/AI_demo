import pandas as pd
from pymongo import MongoClient
from datetime import datetime

host = "mongodb://localhost"
port = 27017
db = "20221114"
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

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
ourData.to_csv(f"sensor_data_{year}{month}{day}_{hour}{minute}.csv", sep=',', encoding='utf-8')




















#Original code:
# import pandas as pd
# from pymongo import MongoClient


# def _connect_mongo(host, port, username, password, db):
#     """ A util for making a connection to mongo """

#     if username and password:
#         mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
#         conn = MongoClient(mongo_uri)
#     else:
#         conn = MongoClient(host, port)


#     return conn[db]


# def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
#     """ Read from Mongo and Store into DataFrame """

#     # Connect to MongoDB
#     db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

#     # Make a query to the specific DB and Collection
#     cursor = db[collection].find(query)

#     # Expand the cursor and construct the DataFrame
#     df =  pd.DataFrame(list(cursor))

#     # Delete the _id
#     if no_id:
#         del df['_id']

#     return df