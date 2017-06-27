from pymongo import MongoClient
import json

client = MongoClient(host='10.136.43.4', port=27017)

db = client['youtube_country_code']
with open('data.json') as d:
    d = json.load(d)
db.code.insert_many([i for i in d])
