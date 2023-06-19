from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://rajatjain852:rajat321@cluster0.drhks7r.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

# read data as dataframe
DATABASE_NAME='credit_card'
COLLECTION_NAME='credit_card_fault_data'
df=pd.read_csv(r"/home/admin1/Desktop/search/credi_card_fault_detection/notebooks/cred_card_data.csv")
# df=df.drop('Unnamed: 0',axis=1)
# convert data to json
json_record=list(json.loads(df.T.to_json()).values())

# dump data to database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
