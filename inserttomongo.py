from pymongo import MongoClient
import json

client = MongoClient(host='127.0.0.1', port=27017)

db = client['youtube_country_code']
with open('data.json') as d:
    d = json.load(d)
db.code.insert_many([i for i in d])
